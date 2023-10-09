"""
Este módulo armazena a chamada principal da automação. 
"""

# Importação
from engine.automacao import Automacao

def main():
    """Executa a função principal do código."""
    automacao = Automacao()
    automacao.raspar_facebook("https://www.facebook.com/gil.cordeiro.1293")

if __name__ == "__main__":
    """Chama a função na inicialização do código."""
    main()
