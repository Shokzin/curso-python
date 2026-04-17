# Lista: representa uma sequência de valores

# Sintxe: nome_lista = [valores]

""" notas = [5, 7, 8, 6, 9]
print(notas)

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 2, 5, 9, 10]
valores = n1 + n2
print(valores)

valores[0] = 100
print(valores[0]) # Imprime o novo primeiro valor da lista
print(valores[-1]) # Imprime o último valor da lista
print(valores[0:5]) # Imprime 5 valores a partir da posição 0
print(valores[2:]) # Imprime todos os valores a partir da posição 2
print(valores[:4]) # Imprime 4 valores a partir da posição 0

print(len(valores)) # Imprime a quantidade de elementos da minha lista
print(sorted(valores)) # Imprime a lista em ordem crescente
print(sorted(valores, reverse=True)) # Imprime a lista em ordem decrescente
print(sum(valores)) # Imprime a soma dos valores da lista
print(min(valores)) # Imprime o valor mínimo da lista
print(max(valores)) # Imprime o valor máximo da lista 

# --

valores.append(11) # Insere um valor no final da lista
print(valores) 
valores.pop() # Remove o valor final da lista
print(valores)

valores.pop(0) # Se definida a posição dentro dos parenteses, remove o valor da posição da lista
print(valores)

print(12 in valores) # Verifica se o valor definido está na lista ou não """

# --

# planetas = list() //  Cria uma lista Vazia

planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Saturno", "Urano", "Netuno"]
for planeta in planetas:
    print(planeta)
