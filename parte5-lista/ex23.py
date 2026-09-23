numeros = [5, 10, 15, 20, 25]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número é:", maior)