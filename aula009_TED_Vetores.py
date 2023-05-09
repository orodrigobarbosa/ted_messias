#Exercicio 1
numeros = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    #add os numeros lidos ao final do vetor
    numeros.append(numero)

# reversed() para escrever os numeros na ordem inversa
print("A ordem inversa dos números digitados é: ")
for numero in reversed(numeros):
    print(numero)