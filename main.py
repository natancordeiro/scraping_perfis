"""
Este módulo armazena a chamada principal da automação. 
"""

# Importação
from engine.automacao import Automacao
import os, time

banner = """\033[34m
   _____                       _                ______                __                __  
  / ___/______________ _____  (_)___  ____ _   / ____/___ _________  / /_  ____  ____  / /__
  \__ \/ ___/ ___/ __ `/ __ \/ / __ \/ __ `/  / /_  / __ `/ ___/ _ \/ __ \/ __ \/ __ \/ //_/
 ___/ / /__/ /  / /_/ / /_/ / / / / / /_/ /  / __/ / /_/ / /__/  __/ /_/ / /_/ / /_/ / ,<   
/____/\___/_/   \__,_/ .___/_/_/ /_/\__, /  /_/    \__,_/\___/\___/_.___/\____/\____/_/|_|  
                    /_/            /____/                                                   

\033[0m"""

def main():
    """Executa a função principal do código."""
    os.system('cls')
    print(banner)
    time.sleep(1)
    automacao = Automacao()
    automacao.raspar_facebook()

if __name__ == "__main__":
    """Chama a função na inicialização do código."""
    main()
