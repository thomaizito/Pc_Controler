from os import system
from time import sleep

class Opener:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2=l2
        self.l3=l3
    
    @staticmethod
    def open(lista:list):
        try:
            for i in lista:
                system(f'start {i}')
        except Exception as e:
            print(f"Erro inexeperado! {e}")

    def study(self):
        try:
            if not self.l1:
                return False
            
            self.open(self.l1)

        except Exception as e:
            print(F"ERRO! {e}") 

    def code(self):
        try:
            if not self.l2:
                return False
            
            self.open(self.l2)
            
        except Exception as e:
            print(F"ERRO! {e}")
    
    def game(self):
        try:
            if not self.l3:
                return False

            self.open(self.l3)

            return True
        
        except Exception as e:
            print(F"Erro! {e}")
    

    def other(self):
        return True
            