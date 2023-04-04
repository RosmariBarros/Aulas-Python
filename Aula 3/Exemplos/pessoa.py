
#Primeiro inicializa as variaveis

# Processamento

# Output



class Pessoa():
    
    def __init__(self) -> None:
        pass
            
    def nome(self, nome):
        print(f"Meu nome é {nome}")
    
    def idade(self, idade):
        print("Idade : ", idade)
    
    def cpf(self, CPF):
        print("CPF: ", CPF)
        


pessoa = Pessoa()

pessoa.nome("Samuel")
pessoa.idade(20)
pessoa.cpf("000.000.000")
