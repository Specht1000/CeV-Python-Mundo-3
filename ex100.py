from random import randint

def somar_pares(lista):
    soma_par = 0
    for valor in lista_numeros:
        if valor % 2 == 0:
            soma_par += valor
    print(soma_par)

def criar_lista():
    tamanho = randint(1, 10)
    print("Tamanho da lista: {}".format(tamanho))

    lista_numeros = []
    i = 0
    while i < tamanho:
        num = randint(1, 10)
        lista_numeros.append(num)
        i = i + 1
    print(lista_numeros)
    return lista_numeros


lista_numeros = criar_lista()
somar_pares(lista_numeros)
