
horas_de_viagem = int(input("Digite o tempo da viagem (em horas): ")) 
velocidade_media = int(input("Digite a velocidade média (em Km/h): "))

distancia_percorrida = horas_de_viagem * velocidade_media

combustivel_necessario = distancia_percorrida / 12
print(f"{combustivel_necessario:.3f}")
