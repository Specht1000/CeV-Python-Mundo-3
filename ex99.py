def numero(*num):
    cont  = maior = 0
    for valor in num:
        cont = cont + 1
        if valor >= maior:
            maior = valor
    print("Tamanho: {}".format(cont), end=' ')
    print("Maior: {}".format(maior))


numero(4, 7, 0, 9)
numero(1, 3, 6)
numero(67, 23, 48, 210, 194, 653)