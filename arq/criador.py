class Write:
    def __init__(self):
        self.arq = None
        self.v = None
    
    @staticmethod
    def valid(func):
        def inner(self, arq, v):
            if not arq:
                print("Coloque um arquivo válido!")
                return False
            elif not v:
                print("Coloque valores válidos!")
                return False
            return func(self, arq, v)
        return inner
            
    @valid
    def writing(self, arq, value): # Adicionar qualquer arquivo
        try:
            self.arq = arq
            self.v = value

            with open(self.arq, 'w') as arq: # Adicionar e criar o arquivo no sistema
                
                if not isinstance(self.v, str):
                    for i in self.v:
                        arq.write(f"{i}\n")
                    return True
                arq.write(self.v)
            
            print("Salvo!")

        except Exception as e:
            print(f"Erro! {e}")