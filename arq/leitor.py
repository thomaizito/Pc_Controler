class Read:
    def __init__(self):
        self.arq = None
        self.ret = None
    
    @staticmethod
    def valid(func):

        def inner(self, arq):
            if not arq:
                return False
            
            return func(self, arq)
        
        return inner
    
    @valid
    def reading(self, arq:str):
        try:
            self.arq = arq

            with open(arq) as arq:
                for linha in arq:
                    if not linha:
                        return False
                    self.ret = linha.rstrip()
                    
            return self.ret
        
        except Exception as e:
            print(f"ERRO! {e}")