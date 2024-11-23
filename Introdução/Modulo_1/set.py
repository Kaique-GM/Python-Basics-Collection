#Criação e operações básicas
print("Criação e operações básicas\n")

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

###########################################################

#Operações

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

#união

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

#interseção

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

#diferença

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}

#diferença simétrica

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}


#Métodos de conjuntos
print("\nMétodos de conjuntos\n")

frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()