# Dicionários

elemento = {
    "Z": 3,
    "nome": "Lítio",
    "grupo": "Metais alcalinos",
    "densidade": 0.534,
}

print(f"Elemento: {elemento['nome']}")
print(f"Densidade: {elemento['densidade']}")
print(f"O dicionário possui {len(elemento)} elementos.") # Imprime o número de elementos no dicionário elemento

# Atualizar uma entrada
elemento["grupo"] = "Alcalinhos"
print(elemento)

# Adicionar uma nova entrada

elemento["periodo"] = 1 # Adiciona uma nova entrada ao dicionário elemento
print(elemento)

# Excluir uma entrada
del elemento["periodo"] # Exclui a entrada "periodo" do dicionário elemento
print(elemento)

elemento.clear() # Limpa todas as entradas do dicionário elemento
print(elemento)

del elemento # Exclui o dicionário elemento completamente
print(elemento) # Isso causará um erro, pois o dicionário elemento foi excluído

# --

print(elemento.items()) # Imprime uma lista de tuplas contendo as chaves e valores do dicionário elemento
for i in elemento.items(): # Imprime cada chave e valor do dicionário elemento
    print(i)

print(elemento.keys()) # Imprime uma lista de chaves do dicionário elemento
for i in elemento.keys(): # Imprime cada chave do dicionário elemento
    print(i)

print(elemento.values()) # Imprime uma lista de valores do dicionário elemento
for i in elemento.values(): # Imprime cada valor do dicionário elemento
    print(i)

for i, j in elemento.items(): # Imprime cada chave e valor do dicionário elemento usando desempacotamento de tuplas
    print(f"Chave: {i}, Valor: {j}")    