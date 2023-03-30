import math

raio = float(input("Digite o raio: "))
n = 3.14159

# Com biblioteca
area = n * math.pow(raio, 2)

# Sem biblioteca
area1 = n * (raio ** 2)

print(f"A= {area:.4f}")
print(f"A= {area1:.4f}")