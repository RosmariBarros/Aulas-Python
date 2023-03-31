import math

nome = str(input("Digite o nome do vendedor: "))
salário_fixo = float(input("Digite o seu salário fixo: "))
total_vendas = float(input("Digite o total de vendas mensais: R$ "))
percentual_comissão = float(input("Digite o percentual de comissão: "))

valor_comissão = total_vendas * percentual_comissão / 100 

total_a_receber = float(salário_fixo + valor_comissão)

print(f"TOTAL = R$ {total_a_receber:.2f}")




                         
                         
