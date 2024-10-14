#Definição e chamada de funções

def saudacao():
    print("Olá, mundo!")

saudacao()  # Imprime "Olá, mundo!"

print(" ")
#Parâmetros e argumentos

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"

print(" ")
#Valores de retorno

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Imprime 7

print(" ")
#Funções anônimas (lambda)

quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25

print(" ")
#Escopo das variáveis (local vs. global)

def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
#print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.

print(" ")
#Funções definidas pelo usuário

def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma/quantidade

    return media

print("Media: ", calcular_media(10,20,30,40))

print(" ")

def somar_3(x):
    return x + 3

somar = lambda x: x + 3

print("Somar 3 a um número: ", somar(5))

print(" ")

#Documentação de funções (docstrings)

def area_retangulo(base, altura):
    
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

print(" ")
#Funções com número variável de argumentos

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22


