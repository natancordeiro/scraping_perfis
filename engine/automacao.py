"""
Este módulo é voltado para guardar o código do Web Scraping. 

Neste módulo é usando a classe Navegador, que herda as funcionalidades do Selenium.

O objetivo deste código é coletar os dados de figuras públicas através das redes sociais Facebook e Twitter.

Documentação Adicional: https://peps.python.org/pep-0008/ | https://selenium-python.readthedocs.io/index.html

Licença:
Este código está sujeito às políticas e regulamentos internos.

© 2023, Natan.
"""

# Importações do Python
import requests
import datetime
from openpyxl import Workbook, load_workbook
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Importações Internas
from engine.navegador import Navegador
from utilitarios.utilitarios import *

class Automacao:
    def raspar_facebook(self):
        """Função definida para raspar os dados de um perfil do Facebook."""

        # Salvando o input do usuário
        os.system('cls')
        url = input("Insira o nome do usuário ou cole o link do perfil: ")
        usuario_pesquisa = url.split("/")[-1].split("?")[0]

        # Verifica se deseja período
        filtrar_periodo = False
        if input("Deseja informar período? [s/n]: ") == "S".upper().split():
            período_inicio = "Informe o início do período que deseja filtrar - [DD/MM/YYYY]: "
            período_final = "Informe o final do período que deseja filtrar - [DD/MM/YYYY]: "

        # Instanciando o Navegador
        self.navegador = Navegador(salvar_cache=PATH['arquivo_cache'], tela_cheia=True)

        # Verficia de o Input foi uma URL ou o nome do Usuário
        if self.e_url(url):
            self.navegador.navegar(url)
        else: 
            self.navegador.navegar(LINKS['base_facebook'] + usuario_pesquisa)
        sleep(5)

        # Verifica se o form login está na tela
        if len(self.navegador.obter_elementos('XPATH', XPATHS['form_login'])) > 0:
            self.login_facebook(CREDENCIAIS['email_facebook'], CREDENCIAIS['senha_facebook'])

        self.navegador.esperar('css_selector', CSS['filtro'])
        sleep(1)

        # Enquanto tiver posts na tela, vai dar scroll
        elementos_postagens = []
        while len(self.navegador.obter_elementos('XPATH', XPATHS['posts'])) != len(elementos_postagens):
            elementos_postagens = self.navegador.obter_elementos('XPATH', XPATHS['posts'])
            for i, div in enumerate(elementos_postagens):

                # data de postagem | URL | Texto
                url_postagem = div.find_element(By.XPATH, XPATHS['url_postagem']).get_attribute("href")
                texto_postagem = div.find_element(By.XPATH, XPATHS['texto_postagem']).text

                data = div.find_element(By.XPATH, XPATHS['data_postagem']).text
                dia = data.split(" ")[0]
                mes = self.converte_nome_mes(data.split(" ")[2])
                if data.split(" ")[-1].isdigit():
                    ano = data.split(" ")[-1]
                else:
                    ano = datetime.datetime.now().year
                data_postagem = f"{dia}/{mes}/{ano}"
                nome_arquivo = f"\{usuario_pesquisa}\{dia}.{mes}.{ano}"
                
                # Verifica se tem imagem
                if len(div.find_elements(By.XPATH, '//a//img')) >= 1:
                    imagens = div.find_elements(By.XPATH, '//a//img')
                    for img in imagens:
                        imagem_url = img.get_attribute("src")
                        hora = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond)
                        self.baixar_conteudo(imagem_url,PATH['saida_facebook'] + nome_arquivo + f"\img\{hora}.png")
                        nome_arquivos_imagens = f"{nome_arquivo}, "

                # Verifica se tem vídeo
                if len(div.find_elements(By.XPATH, '//a[@aria-label="Ampliar"]')) >= 1:
                    video_url = self.obter_link_video(div)
                    hora = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond)
                    self.baixar_conteudo(video_url, nome_arquivo + f"\movie\{hora}.mp4")
                    nome_arquivos_video = f"{nome_arquivo}, "

                # Salva os dados na planilha
                self.adicionar_dados_excel(PATH['saida_facebook'] + nome_arquivo, 
                                           data_postagem, 
                                           url_postagem, 
                                           texto_postagem, 
                                           nome_arquivos_imagens, 
                                           nome_arquivos_video
                                           )

            self.navegador.rolar_para_elemento(elementos_postagens[-3])
            sleep(0.5)
    
        return True

    def raspar_twitter(self):
        """Função definida para raspar os dados de um perfil do Facebook."""
        pass

    def e_url(self, texto=str):
        """Verifica se a string é um Link de URL."""

        if "http://" or "www." or "https://" in texto:
            return True
        else:
            return False
        
    def login_facebook(self, usuario=str, senha=str):
        """Faz login no Facebook."""
        input_email = self.navegador.obter_elemento('XPATH', XPATHS['email'])
        input_senha = self.navegador.obter_elemento('XPATH', XPATHS['senha'])

        self.navegador.clicar_elemento(input_email)
        self.navegador.enviar_teclas(CREDENCIAIS['email_facebook'], espera_entre_as_teclas=0.2)
        self.navegador.espera_aleatoria(1, 2)

        self.navegador.clicar_elemento(input_senha)
        self.navegador.enviar_teclas(CREDENCIAIS['senha_facebook'])
        self.navegador.espera_aleatoria(1, 2)

        input_senha.send_keys(Keys.ENTER)

    def baixar_conteudo(self, link, nome_arquivo):
        try:
            response = requests.get(link)
            if response.status_code == 200:
                with open(nome_arquivo, 'wb') as arquivo:
                    arquivo.write(response.content)
                print(f'{nome_arquivo} baixado com sucesso.')
            else:
                print(f'Não foi possível baixar {nome_arquivo}. Status code: {response.status_code}')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    def obter_link_video(self, elemento):
        link = elemento.find_element(By.XPATH, '//a[@aria-label="Ampliar"]').get_attribute("href").replace("www", "mbasic")
        self.navegador.switch_to.new_window()
        self.navegador.navegar(link)
        janela = self.navegador.id_janela_atual()
        self.navegador.esperar('XPATH', '//a[@aria-label="Assistir ao vídeo"]')
        video_url = 'https://mbasic.facebook.com' + self.navegador.obter_elemento('XPATH', '//a[@aria-label="Assistir ao vídeo"]').get_attribute("href")
        self.navegador.navegar(video_url)
        while self.navegador.url_atual() == video_url:
            pass
        url = self.navegador.url_atual()
        self.navegador.mudar_foco(janela_padrao=True)
        self.navegador.fechar_janela(janela)
        return url

    def converte_nome_mes(self, nome_mes):
        meses = {
            'janeiro': 1,
            'fevereiro': 2,
            'março': 3,
            'abril': 4,
            'maio': 5,
            'junho': 6,
            'julho': 7,
            'agosto': 8,
            'setembro': 9,
            'outubro': 10,
            'novembro': 11,
            'dezembro': 12
        }
        
        # Converte o nome do mês para minúsculas e verifica se está no dicionário
        nome_mes = nome_mes.lower()
        if nome_mes in meses:
            return meses[nome_mes]
        else:
            return None 
    
    def adicionar_dados_excel(self, nome_planilha, data, url, texto, imagens, videos):
        if not os.path.exists(nome_planilha):
            wb = Workbook()
            ws = wb.active
            ws.append(["Data da Postagem", "URL da Postagem", "Texto da Postagem", "Nome dos Arquivos das Imagens", "Nome dos Arquivos dos Vídeos"])
        else:
            wb = load_workbook(nome_planilha)
            ws = wb.active
        
        ws.append([data, url, texto, imagens, videos])
        wb.save(nome_planilha)