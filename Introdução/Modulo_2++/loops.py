#Lab 1

secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("Digite seu número: "))

while number != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    number = int(input("Digite seu número: "))

print("Muito bem, trouxa! Você está livre agora.")

#Lab 2

import time

# Escreva um loop for que conte até cinco
   # Corpo do loop - exiba o número de iteração do loop e a palavra "Mississippi".
   # Corpo do loop - use: time.sleep(1)

# Escreva uma função print com a mensagem final.

for i in range(1 , 6):
    print(i , "Mississippi")
    time.sleep(1)

print("Pronto ou não, aqui vou eu!")

#Lab 3

palavra = input("Digite uma Palavra: ")

while palavra:
    if palavra == "chupacabra":
        break 
    palavra = input("Digite uma Palavra: ")

    
print("Você saiu do loop com sucesso")

# Lab 4

# Solicita que o usuário insira uma palavra
# e atribua-a à variável user_word.

user_word = input("Digite uma Palavra: ")
word_without_vowels = ""

for letter in user_word.upper():
    # Preenchao corpo do loop for.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

#Lab 5

blocks = int(input("Insira o número de blocos:"))  
 # Escreva seu código aqui.
altura = 0
nivel = 1

while blocks >= nivel:
    blocks -= nivel
    altura += 1
    nivel += 1

#

print("A altura da pirâmide:", altura)

#Lab 6

c0 = int(input("Digite um Número: "))
etapas = 0

while c0  != 1:
    print(c0)

    if c0 % 2 == 0:
       c0 = c0 / 2

    else:
        c0 = 3 * c0 + 1
    etapas += 1

print("Etapas:" , etapas)