idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = "Pode perguntar do evento:" +str(resultado)

print(msg)

# Programa de disparo de alarme
porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
print("Alarme disparado?" + str(alarme))
print(msg)

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = "Tem dinheiro para comprar o produto?" + str(tem_dinheiro)
print(msg)