num = 1

while (num <= 10):
    print(num)
    num = num + 1  ## ou num += 1
print("Fim do loop")

## --

nome = None # variável sem valor

while True:
    print("Digite seu nome, ou 'x' para sair: ")
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f"Bem-vindo, {nome}!")
print("Fim do programa")

