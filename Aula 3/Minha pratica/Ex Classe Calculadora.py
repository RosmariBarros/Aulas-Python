# 1) Faca uma classe calculadora e coloque todas as operacoes em especie de funcao

class Calculadora:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def somar(self):
        return self.a+self.b
    def subtrair(self):
        return self.a-self.b
    def multiplicar(self):
        return self.a*self.b
    def dividir(self):
        return self.a/self.b
    
c = Calculadora(5,7)
print(c.somar())
print(c.subtrair())
print(c.multiplicar())
print(c.dividir())

    