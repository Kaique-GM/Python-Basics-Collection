print("Números de 1 a 5 multiplicados por 2 com for: ")
for numero in range(1, 6):
    print(numero * 2)


print("Números de 1 a 5 multiplicados por 2 com while")
contador = 1

while contador <=5:
    print(contador * 2)
    contador +=1

#Controle de Loops

#Break
print("Break")

contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break

#Continue
print("Continue")


for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

#Pass

for i in range(5):
    pass