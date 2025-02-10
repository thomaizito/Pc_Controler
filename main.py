try:
    import os
except ModuleNotFoundError:
    print("Erro! Instale os pacotes necessários")
    exit()

class Apd:
    def __init__(self):
        self.op = None
    
    def start(self):
        try:
            self.op = int(input("Digite o que quer fazer (escreva em números)?\n 1. Codar\n 2. Jogar\n 3. Outro\n"))
            return self.op

        except ValueError:
            print("Digite um valor entre 1 a 3!")
            self.start()

class Main:
    def __init__(self):
        self.inner = int(Apd().start())
    
    def main(self):
        if not self.inner:
            raise ValueError('The func need an value!')

        match self.inner:
            case 1:
                return self.main1()
            case 2:
                return self.main2()
            case 3:
                print("Ok!")
                os.system("exit")
                return None
            case _:
                print("Coloque um valro válido!")
                self.main()
            
        exit()

    @staticmethod
    def main1():
        os.system('start opera')
        os.system('start cmd')
        os.system("code")
    
    @staticmethod
    def main2():
        os.system('start opera')


Main().main()