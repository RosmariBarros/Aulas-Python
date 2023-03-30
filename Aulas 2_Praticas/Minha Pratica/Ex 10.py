peça1 = int(input("Digite o código da peça1: "))
qtd_1 = int(input("Digite a quantidade da peça1: "))
vl_unitário1 = float(input("Digite o valor unitário da peça1: "))

peça2 = int(input("Digite o código da peça2: "))
qtd_2 = int(input("Digite a quantidade da peça2: "))
vl_unitário2 = float(input("Digite o valor unitário da peça2: "))

valor_total_peça1 = float(qtd_1 * vl_unitário1)
valor_total_peça2 = float(qtd_2 * vl_unitário2)

total_compra = valor_total_peça1 + valor_total_peça2

print(f"VALOR A PAGAR: R$ {total_compra:.2f}")


   




