# Simples, Composto, Encadeado

n1 = n2 = 0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")