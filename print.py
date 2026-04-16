# Sintaxe:
# print("Texto a ser impresso") (objetos, argumentos)

mensagem = "Função print()"
print(mensagem)
aula = "Aula de Python"
nome = input("Digite seu nome: ")
print (" Eu me chamo " + nome + " e esta é uma " + aula)

# --

print("Imprime a mensagem e muda de linha")
print("Imprime a mensagem e permanece na mesma linha", end="")
print(" e continua na mesma linha")

# --

nome = "Mateus"
idade = 25
msg_formatada = "O nome dele é {0} e ele tem {1} anos".format(nome, idade) # O método format() é usado para formatar a string, substituindo os placeholders {0} e {1} pelos valores das variáveis nome e idade, respectivamente.    
print(msg_formatada)

# --

nome = "Fábio"
peso = 75.50
msg = f"Olá, meu nome é {nome} e eu peso {peso} kg."
print(msg)

valor = 123.456789
print(f"O valor é {valor:.2f}") # Formata o valor para 2 casas decimais

# --

nome = "Ana"
idade = 19
print(f"Nome: {nome}\tidade: {idade}") # \t é um caractere de tabulação para alinhar o texto