
class write:
    def __init__(self, arquivo:None, value:None):
        self.arq = arquivo
        self.v = value
    
    def writing(self): # Adicionar qualquer arquivo
        try:
            if not self.arq: # Verificar se o arquivo existe!
                print("Erro! Insira um arquivo válido!")
                return False
            
            with open(self.arq, 'w') as arq: # Adicionar e criar o arquivo no sistema
                for i in self.v:
                    arq.write(f'{i}\n')
                

            return True
        
        except Exception as e:
            print(f"Erro! {e}")

ar = "flag.txt"

writ = write("flag.txt", [2, 3, 4])
writ.writing()