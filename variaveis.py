media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = "Alice", 47
estado = True

# Função type() para verificar o tipo de uma variável
print(type(media))  # <class 'int'>
print(type(n1))     # <class 'float'>
print(type(nome))   # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(estado)) # <class 'bool'>
print(type(1+2j))   # <class 'complex'>

# Função isinstance() para verificar se uma variável é de um tipo específico
a = 10
b = 'Sol'
print(isinstance(a, int))
print(isinstance(b, (int, str)))

a = 40
c = 3
r = a * c
print(r)