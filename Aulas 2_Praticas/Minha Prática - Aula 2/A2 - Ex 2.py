A = float(input("Digite o primeiro numero: "))
B = float(input("Digite o segundo numero: "))
C = float(input("Digite o terceiro numero: "))

# Calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
area_tr = (A * C) / 2

# b) a área do círculo de raio C. (PI = 3.14159)
pi = 3.14159
area_circ = pi * C ** 2

# c) a área do trapézio que tem A e B por bases e C por altura.
area_trap = (A + B) / 2 * C

# d) a área do quadrado que tem lado B.
area_quad = B ** 2

# e) a área do retângulo que tem lados A e B.
area_ret = A * B

print(f"TRIANGULO: {area_tr:.3f}")
print(f"CIRCULO: {area_circ:.3f}")
print(f"TRAPEZIO: {area_trap:.3f}")
print(f"QUADRADO: {area_quad:.3f}")
print(f"RETANGULO: {area_ret:.3f}")
