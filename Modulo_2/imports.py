#Importar módulos

import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

print(" ")

#Apenas o sqrt do math

from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0


print(" ")
#datetime e random

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual