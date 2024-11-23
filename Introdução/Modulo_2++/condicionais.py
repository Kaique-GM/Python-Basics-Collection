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

#Lab

labStr = input("Insira o nome da flor: ")

if labStr == "Spathiphyllum":
    print("Sim - Spathiphyllum é a melhor fábrica de todos os tempos!")

elif labStr == "spathiphyllum":
    print("Não, eu quero um grande Spathiphyllum!")
else:
    print("Spathiphyllum! Not, " + labStr)

#Lab 2
    
income = float(input("Entre com os rendimentos anuais "))

if income < 85528:
    tax = income * 0.18 - 556.02
# Escreve o resto do código aqui.
elif income > 85528:
    excedente =  income - 85528
    porcentagem = excedente * 0.32
    tax= 14839.2 + porcentagem
    
tax = round(tax, 0)

if tax < 0:
    print("A taxa é: 0.0 thalers") 
else:
    print("A taxa é:", tax, "thalers") 
    
    #Lab 3
    
year = int(input("Digite um ano: "))

if year < 1582:
  print("Não está dentro do período do calendário gregoriano")
else:
  # Escreve o bloco se-então aqui
    if year % 4 != 0:
        print("Ano Comum")
    elif year % 100 != 0:
        print("Ano Bissexto")
    elif year % 400 != 0:
        print("Ano Comum")
    else:
        print("Ano Bissexto")

    