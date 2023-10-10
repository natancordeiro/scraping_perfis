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
from selenium.webdriver.common.by import By
from time import sleep

# Importações Internas
from engine.navegador import Navegador
from utilitarios.utilitarios import *

class Automacao:
    def raspar_facebook(self):
        """Função definida para raspar os dados de um perfil do Facebook."""

        # Salvando o input do usuário
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
                data_format = f"{dia}.{mes}.{ano}"
                
                # Verifica se tem imagem
                if len(div.find_elements(By.XPATH, '//a//img')) >= 1:
                    imagens = div.find_elements(By.XPATH, '//a//img')
                    for index, img in enumerate(imagens):
                        nome_arquivo = f"{usuario_pesquisa}\imagem_{data_format}_{i}_{index}.png"
                        self.baixar_imagem(img.get_attribute("src"), nome_arquivo)

                # Verifica se tem vídeo
                if len(div.find_elements(By.XPATH, '//a[@aria-label="Ampliar"]')) >= 1:
                    # Baixar vídeo do post
                    pass
            
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
        input_email = self.navegador.obter_elemento('NAME', 'email')
        input_senha = self.navegador.obter_elemento('NAME', 'pass')

    def filtrar_data(self):
        pass

    def baixar_imagem(self, link, nome_arquivo):
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
    