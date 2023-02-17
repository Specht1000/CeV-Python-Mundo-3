from random import randint
lista = []
num_jogos = int(input("Numero de jogos: "))
cont = 0
while True:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont = cont + 1
    if cont >= num_jogos:
        break
print("{}".format(lista))