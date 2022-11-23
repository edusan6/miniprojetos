import math
import random as rd

numero = int(input("Digite um numero entre 0 a 10: "))
while numero <= 0 or numero >= 10:
    print("Por favor digite um numero entre 0 e 10")
    numero = int(input("Digite um numero entre 0 a 100: "))
rand = rd.randrange(1,11)
if numero == rand:
    print("Acertou")
else:
    print(f"Errou, o numero é {rand}")
