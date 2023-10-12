"""
Este módulo é voltado para guardar os valores dos elementos que serão usados nas automações Web.

O objetivo deste código é simplificar a legibilidade do código, visto que muitos elementos tem XPATHs etensos, dificultando a leitura.
"""
import os

CREDENCIAIS = {
    'email_facebook': 'SEU_EMAIL_AQUI', # <- COLOQUE SEU E-MAIL DO FACEBOOK AQUI
    'senha_facebook': 'SUA_SENHA_AQUI' # <- COLOQUE SUA SENHA DO FACEBOOK AQUI
}

LINKS = {
    'base_facebook': 'https://mbasic.facebook.com/',
    'login_facebook': 'https://mbasic.facebook.com/login'
}

PATH = {
    'arquivo_cache': os.getcwd() + '\cache',
    'saida_facebook': os.getcwd() + '\\resultados',
    }

XPATHS = {
    'ver_mais_stories': '//a[span[text()="Ver mais stories"]]',
    'email': '//input[@name="email"]',
    'senha': '//input[@name="pass"]',
}
