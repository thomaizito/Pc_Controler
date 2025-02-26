from inner import Main
from configurations import Lista_Arquivos_Programar, Lista_Arquivos_Estudar, Lista_Arquivos_Jogar


### Configurações ###
# Alguns aplicativos não conseguem ser abertos pelo cmd diretamente
# portanto o programa precisa ser adicionado 
# no arquivo configurations.py, pode ser um .lnk (atalho) ou diretamente no aplicativo .exe (executável)
#
# Se for linux, não é necessário, só precisa do comando de abertura do aplicativo
#
#
# 


start = Main(Lista_Arquivos_Estudar, Lista_Arquivos_Programar, Lista_Arquivos_Jogar)
start.start()