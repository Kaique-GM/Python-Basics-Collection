print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "... Realmente?")

anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")

anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é:", something)

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Lab 1

a = float(input("Digite um Número: "))
b = float(input("Digite outro Número: "))

print("a + b = " + str(a + b))
print("a - b = " + str(a - b))
print("a * b = " + str(a * b))
print("a / b = " + str(a / b))

print("\nIsso é tudo, pessoal!")

#Lab 2

x = float(input("Digite o valor para x: "))

y = 1 / (x+ 1 / (x + 1 / (x + 1 / x )))

print("y =", y)

#Lab 3 

hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
mins = mins + dura # encontre um total de todos os minutos
hour = hour + mins // 60 # encontre um número de horas escondido em minutos e atualize a hora
mins = mins % 60 # minutos corretos para cair no intervalo (0..59)
hour = hour % 24 # horas corretas para cair no intervalo (0..23)
print(hour, ":", mins, sep='')


