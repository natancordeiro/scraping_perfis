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
    'base_facebook': 'https://mbasic.facebook.com/',
}

PATH = {
    'arquivo_cache': os.getcwd() + '\cache',
    'saida_facebook': os.getcwd() + '\\resultados',
    }

XPATHS = {
    'ver_mais_stories': '//a[span[text()="Ver mais stories"]]',
    'email': '//div/input[@name="email"]',
    'senha': '//div/input[@name="pass"]',
}
