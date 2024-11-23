#Entrada de dados do usuário

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")


print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")

print("/////////////////////////////////////////////////////////////")
#realizar uma conversão explícita utilizando funções como int() ou float().

idade = int(input("Insira sua idade: "))


if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

print("/////////////////////////////////////////////////////////////")
#Saída de dados

nome = "Juan"
idade = 25


print(f"Olá, meu nome é {nome} e tenho {idade} anos.")


