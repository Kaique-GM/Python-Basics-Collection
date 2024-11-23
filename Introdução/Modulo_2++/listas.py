# #Lab 1

# hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.
# print(hat_list, "\n")

#  # Etapa 1: escreva uma linha de código que solicita ao usuário
# # que substitua o número do meio por um número inteiro inserido pelo usuário. 
# number = int(input("Digite um numero para substituir o número do meio: "))
# hat_list[2] = number
# print(hat_list, "\n")

# # Etapa 2: escreva uma linha de código que remova o último elemento da lista.
# print("================== del ==================")

# del hat_list[-1]
# print(hat_list, "\n")


#  # Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual
# print ( len(hat_list), "\n")
# print (hat_list) 

#Lab 2

# etapa 1
beatles = []
print("Etapa 1:", beatles)


# etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)


# etapa 3
# Stu Sutcliffe
# Pete Best
for i in range(2):
    nome = input("Insira os Nomes: ")
    beatles.append(nome)
    
print("Etapa 3:", beatles)


# etapa 4

del beatles[-1]
del beatles[-1]

print("Etapa 4:", beatles)

# passo 5
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)



# testando o tamanho da lista

print("o fabuloso", len(beatles))

