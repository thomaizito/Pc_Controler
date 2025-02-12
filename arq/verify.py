from datetime import date, datetime
from leitor import Read
from criador import Write

# ARQUIVO PARA VERIFICAR SE O PC JÁ FOI REINICIADO

class Verif:
    def __init__(self) -> bool:
        self.arq = "flag.txt"
        self.final = False
        self.current_date = date.today()
        self.past_date = 0
    
    @staticmethod
    def convert(date_ram:date):
        try:
            date = datetime.strptime(date_ram, r"%d/%m/%y").date()
            return date
        except Exception as e:
            print(f"Erro! {e}")

    def reading(self):
        leitor = Read()
        date_past_ram = leitor.reading(self.arq)
        self.past_date = self.convert(date_past_ram)
        
        return self.past_date

    def verify(self):
        self.reading()

        if self.past_date == self.current_date:
            return True
        return False


    def writing(self):
        escrever = Write()
        data_str = self.current_date.strftime(r"%d/%m/%y")
        escrever.writing(self.arq, data_str)
