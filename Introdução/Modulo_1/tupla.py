#Criação e acesso
print("Criação e acesso\n")

ponto = (3, 4)
print(ponto[0])  # Imprime 3

print(ponto[1])  # Imprime 4

#Métodos de tuplas
print("\nMétodos de tuplas\n")

minha_tupla = (1, 2, 3, 2, 4, 2)


print (minha_tupla.index(2))   # Saída: 1

print (minha_tupla.index(2, 2))   #Saída: 3

print (minha_tupla.index(2, 2, 4))   #Saída: 3