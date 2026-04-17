# São imutáveis, ou seja, não podem ser alteradas depois de criadas

halogenios = ("Flúor", "Cloro", "Bromo", "Iodo", "Astato")
gases_nobres = ("Hélio", "Neônio", "Argônio", "Criptônio", "Xenônio", "Radônio")
elementos = halogenios + gases_nobres

print(elementos)
print(len(elementos))
print(elementos[-1])
print(elementos[0:5])
print("Iodo" in elementos) # Verifica se o valor definido está na tupla ou não

t1 = (1, 2, 7, 3, 5, 1, 9, 3, 8, 2)
print(t1.count(5)) # Conta quantas vezes o valor definido aparece na tupla

# Operações não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop(), etc.

for elemento in elementos: # Imprime cada elemento da tupla em uma linha
    print(f"Elementos químicos: {elemento}")

grupo17 = list(halogenios) # Converte a tupla em lista
grupo17[0] = "Hidrogênio"
print(grupo17)

grupo1 = ["Lítio", "Sódio", "Potássio", "Rubídio", "Césio", "Frâncio"]
alcalinos = tuple(grupo1) # Converte a lista em tupla
print(type(alcalinos))   

print(sorted(alcalinos)) # Imprime a tupla em ordem alfabética





