lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)

## --

palavra = "Python"

for letra in palavra:
    print(letra)

## --

for numero in range(1, 11):
    print(numero)

## --

nome = input("Digite seu nome: ")
for x in range(10):
    print(f"{x+1} {nome}")

## range(valor_inicial, valor_final, incremento)
for x in range(2, 20, 2): # imprime os números de 2 a 20, pulando de 2 em 2
    print(x)

for x in range(20, 1, -2): # imprime os números de 20 a 1, pulando de 2 em 2
    print(x)

pedras = ("Rubi", "Esmeralda", "Safira", "Diamante")

for pedra in pedras:
    if pedra == "Safira":
        continue # pula a iteração atual e continua com a próxima
    print(pedra)