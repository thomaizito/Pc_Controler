from datetime import date, datetime
from arq.leitor import Read
from arq.criador import Write

# ARQUIVO PARA VERIFICAR SE O PC JÁ FOI REINICIADO

class Verif:
    def __init__(self) -> bool:
        self.arq = r"./arq/flag.txt"
        self.final = False
        self.current_date = date.today()
        self.past_date = 0
        self.leitor = Read()
        self.criador = Write()
    
    @staticmethod
    def convert(date_ram:date):
        try:
            date = datetime.strptime(date_ram, r"%d/%m/%y").date()
            return date
        except Exception as e:
            print(f"Erro! {e}")

    def reading(self):
        date_past_ram = self.leitor.reading(self.arq)
        if not date_past_ram:
            self.writing()

        self.past_date = self.convert(date_past_ram)
        
        return self.past_date

    def verify(self):
        self.reading()

        if self.past_date == self.current_date:
            return True
        return False


    def writing(self):
        data_str = self.current_date.strftime(r"%d/%m/%y")
        self.criador.writing(self.arq, data_str)
    

