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
from selenium.webdriver.common.by import By
from time import sleep

# Importações Internas
from engine.navegador import Navegador
from utilitarios.utilitarios import *

class Automacao:
    def raspar_facebook(self, url):
        """Função definida para raspar os dados de um perfil do Facebook."""
        self.navegador = Navegador(salvar_cache=PATH['arquivo_cache'], tela_cheia=True)

        # Verficia de o Input foi uma URL ou o nome do Usuário
        if self.e_url(url):
            self.navegador.navegar(url)
        else: 
            self.navegador.navegar(LINKS['base_facebook'] + url)
        sleep(5)

        # Verifica se o form login está na tela
        if len(self.navegador.obter_elementos('XPATH', XPATHS['form_login'])) > 0:
            self.login_facebook(CREDENCIAIS['email_facebook'], CREDENCIAIS['senha_facebook'])

        self.navegador.esperar('css_selector', CSS['filtro'])
        sleep(1)

        # Verificar se alguma data foi informadan(chamar função filtrar_data)

        while len(self.navegador.obter_elementos('XPATH', XPATHS['posts'])) != len(elementos_postagens):
            elementos_postagens = self.navegador.obter_elementos('XPATH', XPATHS['posts'])
            for div in elementos_postagens:
                # Verificar se não tem class:
                # Extrair dados

                # data de postagem | URL | Texto
                data_postagem = div.find_element(By.XPATH, XPATHS['data_postagem'])
                url_postagem = div.find_element(By.XPATH, XPATHS['url_postagem'])
                texto_postagem = div.find_element(By.XPATH, XPATHS['texto_postagem']).text

                # Salvar imagem ou vídeo


    
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
