import random

valor = random.randint(1, 20)
print(valor)

# --

print("Gerar cinco números aleatórios entre 1 e 50: \n")
for i in range(5):
    n = random.randint(1, 50)
    print(f"Número gerado: {n}")

# --

valor = random.random()
print(f"Valor gerado: {round(valor * 10, 2)}") # Gera um número aleatório entre 0 e 1, multiplica por 10 e arredonda para 2 casas decimais. 

# --

valor = random.uniform(1, 100)
print(f"Valor: {round(valor, 4)}") 

# --

L = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

n = random.choice(L)
print(f"Número escolhido: {n}")

n = random.sample(L, 6)
print(f"Números extraídos: {n}") 

# Embaralhar a lista

print(f"Lista original: {L}")
print(f"Embaralhando a lista...")
n = random.shuffle(L)
print(f"Lista Embaralhada: {L}")
