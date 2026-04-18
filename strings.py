nome = "Anakin"
sobrenome = "Skywalker"
print(nome + " " + sobrenome)
letra = nome[3]
print(letra)
print(len(nome))

# --

frase = "May the Force be with you"
palavras = frase.split() # Divide a string em uma lista de palavras
print(palavras)

for palavra in palavras: # Imprime cada palavra da lista de palavras
    print(palavra)

for letra in frase: # Imprime cada letra da string
    print(letra)

print(frase[13:25]) # Imprime os caracteres da posição 13 até a posição 24

# --

email = input("Digite seu email: ")
arroba = email.find("@") # Encontra a posição do caractere "@" na string
print(arroba)
usuario = email[0:arroba] # Extrai o nome de usuário do email
dominio = email[arroba + 1:] # Extrai o domínio do email
print(usuario)
print(dominio)

# --

produtos = "Carbonato de sódio e óxido de zinco"
print("sódio" in produtos) # Verifica se a palavra "sódio" está presente na string produtos
print("magnésio" not in produtos)

# --

item = "hipoclorito"
pos = item.find("clor") # Encontra a posição da substring "clor" na string item
print(pos) # Imprime 4, indicando que a substring "clor" começa na posição 4 da string item
pos = item.find("flu")
print(pos) # Imprime -1, indicando que a substring "flu" não foi encontrada na string item

# --

objeto_celeste = "galáxia esPiral M31"
print(objeto_celeste.upper()) # Imprime a string em letras maiúsculas
print(objeto_celeste.lower()) # Imprime a string em letras minúsculas
print(objeto_celeste.capitalize()) # Imprime a string com a primeira letra em maiúscula e o restante em minúscula
print(objeto_celeste.title()) # Imprime a string com a primeira letra de cada palavra em maiúscula

# --

suplemento = "cloreto de magnésio"
n_suplemento = suplemento.replace("magnésio", "zinco") # Substitui a palavra "magnésio" por "zinco" na string suplemento
print(n_suplemento)

# --

frase = "            ômega 3 é bom para a saúde!            "
print(frase.strip()) # Remove os espaços em branco no início e no final da string
# lstrip() remove os espaços em branco apenas no início da string (left - esquerda)
# rstrip() remove os espaços em branco apenas no final da string (right - direita)

fruta = "Abacate"
print(fruta)
print(fruta.center(20)) # Imprime a string centralizada em um campo de largura 20 caracteres, preenchendo os espaços em branco com espaços
# ljust() alinha a string à esquerda e rjust() alinha a string à direita, ambos preenchendo os espaços em branco com espaços
# rjust() alinha a string à direita e ljust() alinha a string à esquerda, ambos preenchendo os espaços em branco com espaços
print(fruta.center(20, "-")) # Imprime a string centralizada em um campo de largura 20 caracteres, preenchendo os espaços em branco com hífens

# --

p = "Anakin Skywalker"
print(p.startswith("Ana")) # Verifica se a string p começa com a substring "Ana"
print(p.endswith("walker")) # Verifica se a string p termina com a substring "walker

# Docstrings (strings de documentação) são usadas para documentar funções, classes e módulos em Python. Elas são definidas usando aspas triplas (""" """) e podem conter informações sobre o propósito da função, seus parâmetros, valor de retorno e exemplos de uso.

texto = """
Docstring é uma espécie de documentação
que podemos inserir dentro de um modulo, função
ou classe no Python, entre outros locais.
    Respeita deslocamento do texto e é    multilinhas
"""

print(texto)
