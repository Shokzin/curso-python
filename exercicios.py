# Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazendando esses valores em uma lista.
# Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repetição for.

bebidas = []

for i in range(5):
    print(f"Digite suas 5 bebidas favoritas: ")
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f"\nBebidas escolhidas: ")
for bebida in bebidas:
    print(bebida)