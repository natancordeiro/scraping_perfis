"""
Este módulo é voltado para guardar os valores dos elementos que serão usados nas automações Web.

O objetivo deste código é simplificar a legibilidade do código, visto que muitos elementos tem XPATHs etensos, dificultando a leitura.
"""
import os

LINKS = {
    'google': f'https://www.google.com'
}

PATH = {
    'arquivo_cache': os.getcwd() + '\cache',
}

XPATHS = {
    'xpath': '/div/div//div/div[2]/div/div[2]/div[2]',
}