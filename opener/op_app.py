from os import system
from time import sleep

class Opener:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2=l2
        self.l3=l3
    
    @staticmethod
    def open(programs:None, lista:list):
        try:
            for item in programs:
                system(f'start {item}')
                sleep(0.2)
                
            print(lista)
            for i in lista:
                print(i)
                system(f'start {i}')
            

        
        except Exception as e:
            print(f"Erro inexeperado! {e}")

    def study(self, *programs:None):
        try:
            if not programs:
                print("Coloque programas!")
                return False
            
            self.open(programs, self.l1)

        except Exception as e:
            print(F"ERRO! {e}") 

    def code(self, *programs:None):
        try:
            if not programs:
                print("Coloque programas!")
                return False
            
            self.open(programs, self.l2)
            
        except Exception as e:
            print(F"ERRO! {e}")
    
    def game(self, *programs:None):
        try:
            if not programs:
                print("Coloque um valor válido")
                return False

            self.open(programs, self.l3)

            return True
        
        except Exception as e:
            print(F"Erro! {e}")
    
    def other(self, *programs:None):
        try:
            if not programs:
                return None

            for i in programs:
                system(f"start {i}")

        except Exception as e:
            print(f"Erro inesperado! {e}")
            