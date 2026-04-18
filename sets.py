# Set

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))
print('Marte' not in planeta_anao)

for astro in planeta_anao:
    print(astro.upper(), end=' ')

# --

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(astros, end=' ')
astro_set = set(astros) # Converte a lista astros em um conjunto, removendo os elementos duplicados
print(astro_set)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
print(astros1 | astros2) # Imprime a união dos conjuntos astros1 e astros2
print(astros1.union(astros2)) # Imprime a união dos conjuntos astros1 e astros2 usando o método union()

print(astros1 & astros2) # Imprime a interseção dos conjuntos astros1 e astros2
print(astros1.intersection(astros2)) # Imprime a interseção dos conjuntos astros1 e astros2 usando o método intersection()

print(astros1 ^ astros2) # Imprime a diferença simétrica dos conjuntos astros1 e astros2
print(astros1.symmetric_difference(astros2)) # Imprime a diferença simétrica dos conjuntos

astros1.add('Urano')
astros1.add('Sol')
astros1.remove('Io')
astros1.discard('Plutão') # O método discard() remove um elemento do conjunto se ele estiver presente, mas não gera um erro se o elemento não estiver presente
astros1.pop() # O método pop() remove e retorna um elemento arbitrário do conjunto. Se o conjunto estiver vazio, ele gera um erro
astros1.clear() # O método clear() remove todos os elementos do conjunto, deixando-o vazio
print(astros1)
