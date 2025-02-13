# Controlar o computador atravez do python!
try:
    
    from opener.op_app import Opener
    from os import system
    from arq.verify import Verif

except ModuleNotFoundError as e:
    print(f"Erro! Instale os pacotes necessários, {e}")
    exit()

class Main:
    def __init__(self):
        pass
    
    @staticmethod
    def verif(func):
        def inner(self):
            choices = ["s"]
            verificador = Verif()

            if verificador.verify():
                return func(self)
            
            choice = input("Você quer reiniciar o pc para maior desempenho? (S/N) ").lower()

            if not choice:
                print("Coloque um valor válido")
                return inner
            elif choice not in choices:
                return func(self)
            
            system('shutdown -r -t 0')

        return inner
        
    @verif
    def start(self):
        try:
            abridor = Opener()
            escolha = int(input("O que você quer fazer?\n 1. Programar\n 2. Estudar\n 3. Jogar\n 4. Navegar na internet\n 5. Outro\n"))

            match escolha:
                case 1:
                    abridor.code('code', 'github desktop', 'opera', 'cmd')

                case 2:
                    abridor.study('opera')
                
                case 3:
                    abridor.game('steam', 'opera', 'discord')
                    
        except Exception as e:
            print(f"Erro! {e}")

sla = Main()
sla.start()