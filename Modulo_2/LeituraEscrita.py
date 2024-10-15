#Escrita de arquivos

arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!\n")
arquivo.write("Teste!")
arquivo.close()

#Leitura de arquivos

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#With

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)