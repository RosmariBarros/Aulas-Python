
"""_summary_
    Documentacao
"""

class Geladeira():
    
    def __init__(self) -> None:
        self.contador = 0
    
    def ligar_luzes(self):
        print("liguei as luzes")
        
    def abrir_portar(self):
        print("abrir a porta")
    
    def fechar_portar(self):
        print("fechar a porta")
    

geladeira = Geladeira()

geladeira.abrir_portar()
geladeira.ligar_luzes()
geladeira.fechar_portar()