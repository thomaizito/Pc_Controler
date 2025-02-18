# Controlar o computador atravez do python!
try:
    from time import sleep
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
            choices_true = ["s"]
            choices_false = ['n']
            verificador = Verif()

            if verificador.verify():
                return func(self)
            
            choice = input("Você quer reiniciar o pc para maior desempenho? (S/N) ").lower()

            if not choice:
                print("Digite um valor válido")
            
            elif choice in choices_true:
                print("Reiniciando o pc")
            
            elif choice in choices_false:
                return func(self)

            else:
                print("Digite um valor válido")
                return inner
            

            system('shutdown -r -t 5')

        return inner
        
    @verif
    def start(self):
        try:
            abridor = Opener()
            escolha = int(input("O que você quer fazer?\n 1. Programar\n 2. Estudar\n 3. Jogar\n 4. Navegar na internet\n 5. Outro\n"))

            match escolha:
                case 1:
                    abridor.code('code', 'github desktop', 'opera')

                case 2:
                    abridor.study('opera')
                
                case 3:
                    abridor.game('steam', 'discord', 'opera')
                
                case 4:
                    abridor.other("opera")
                
                case 5:
                    exit()

                case _:
                    print("Digite um valor válido")
                    self.start
            
            sleep(5)

            system('taskkill /F /IM cmd.exe')

        except Exception as e:
            print(f"Erro! {e}")