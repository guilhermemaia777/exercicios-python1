positivos = 0

numero = int(input("Digite um número: "))

while numero != 0:
    if numero > 0:
        positivos = positivos + 1

    numero = int(input("Digite outro número: "))

print("Quantidade de números positivos:", positivos)