"""
Este módulo é voltado para guardar os valores dos elementos que serão usados nas automações Web.

O objetivo deste código é simplificar a legibilidade do código, visto que muitos elementos tem XPATHs etensos, dificultando a leitura.
"""
import os

CREDENCIAIS = {
    'email_facebook': 'rafaelamesmo@icloud.com',
    'senha_facebook': '479612**',
    'email_twitter': '',
    'senha_twitter': '',
}

LINKS = {
    'base_facebook': 'https://www.facebook.com/',
}

PATH = {
    'arquivo_cache': os.getcwd() + '\cache',
}

CSS = {
    'filtro': 'div[aria-label="Filtros"]',
}
XPATHS = {
    'form_login': '//form[@id="login_popup_cta_form"]',
    'posts': '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[not(@class) and div]',
    'data_postagem': '/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[2]/div/div[2]/div/div[2]/span/span/span[2]',
    'url_postagem':  '/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[2]/div/div[2]/div/div[2]/span/span/span[2]/span/a',
    'texto_postagem': '/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[3]/div/div/div/div/span',
}