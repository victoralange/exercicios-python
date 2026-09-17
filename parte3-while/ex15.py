numerosPositivos = 0

while True:
    numero = float(input("Digite um número: "))

    if(numero == 0):
        break

    if(numero > 0):
        numerosPositivos += 1

print(f"Foram digitados {numerosPositivos} números positivos.")