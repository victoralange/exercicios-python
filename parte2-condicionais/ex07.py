numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))

if(numero1 > numero2):
    print(f"Maior número: {numero1}")
elif(numero2 > numero1):
    print(f"Maior número: {numero2}")
else:
    print(f"Os números são iguais.")