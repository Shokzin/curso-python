""" import math as m
from math import sqrt

print(m.sqrt(16)) # Raiz quadrada de 16

print(sqrt(25)) # Raiz quadrada de 25 """

import mod_func as mf
import numpy as np

if __name__ == "__main__":
    mf.mensagem()

    num = int(input("Digite um número para calcular o fatorial: "))

    print(f"\nCalcular fatorial do numero:")
    fat = mf.fatorial(num)
    print(f"O fatorial é {fat}")

    
    print(f"\nCalcular sequencia de fibonacci:")
    fib = mf.fibo(num)
    print(f"O número de Fibonacci é {fib}")

# -- Importando o módulo numpy para criar um array

    L = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(L)
