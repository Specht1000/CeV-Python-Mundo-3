def aumentar(num, pc):
    res = num + (num * pc/100)
    return res

def diminuir(num, pc):
    res = num - (num * pc/100)
    return res

def dobro(num):
    res = num * 2
    return res

def metade(num):
    res = num / 2
    return res

def moeda(num, cifrao = "R$"):
    return f'{cifrao}{num:.2f}'.replace(".", ",")
