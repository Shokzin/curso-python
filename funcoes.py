# Funções
#Modularização, Reuso de código, Legibilidade 

def mensagem():
    print('Curso de Python')
    print('Anakin Skywalker')

mensagem() # Chama a função mensagem para executar seu código

# --

# Função com argumentos (parâmetros)

def soma(a, b):
    print(a + b)

soma(12, 7)

#

def mult(x, y):
    return x * y

a = 5
b = 8
c = mult(a, b)
print(f'O produto de {a} e {b} é: {c}')

#

def div(k, j):
    if j == 0:
        return "Erro: divisão por zero"
    else:
        return k / j

if __name__ == '__main__':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    res = div(a, b)
    print(f'O resultado da divisão de {a} por {b} é: {res}')

#

def quadrado(val):
    quadrados = []
    for x in val: # Para cada elemento x na lista val, calcula o quadrado de x e adiciona à lista quadrados
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7, 9, 12]
    res = quadrado(valores)
    for f in res:
        print(f)
