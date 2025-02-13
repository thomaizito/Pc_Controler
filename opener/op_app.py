from os import system

class Opener:
    def __init__(self):
        pass
    
    def study(self, *programs:None):
        try:
            if not programs:
                print("Coloque programas!")
                return False
            
            for i in programs:
                system(f"start {i}")
            return True

        except Exception as e:
            print(F"ERRO! {e}") 

    def code(self, *programs:None):
        try:
            if not programs:
                print("Coloque programas!")
                return False
            
            for i in programs:
                system(f"start {i}")
            return True

        except Exception as e:
            print(F"ERRO! {e}")
    
    def game(self, *programs:None):
        try:
            if not programs:
                print("Coloque um valor válido")
                return False
            
            for i in programs:
                if i.lower() == "steam":
                    system(r'"C:\Program Files (x86)\Steam\Steam.exe"')
                    continue    
                
                elif i.lower() == "discord":
                    system(r'"C:\Users\thomas\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\"Discord Inc"\Discord.lnk""')
                    continue

                system(f"start {i}")
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
            