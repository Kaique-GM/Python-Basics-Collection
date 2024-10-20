# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
if number1 > number2:
    largest_number = number1
else: largest_number = number2

if largest_number > number3:
    largest_number = largest_number
else:
    largest_number = number3
 
# Imprimir o resultado
print("O maior número é:", largest_number)