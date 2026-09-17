soma = 0

while True:
    numeroDigitado = float(input("Digite um número: "))

    if(numeroDigitado == 0):
        break

    soma += numeroDigitado

print(f"Soma: {soma}")