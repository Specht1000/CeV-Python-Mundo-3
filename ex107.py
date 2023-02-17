import moeda

valor = 423
aumento = moeda.aumentar(valor, 10)
print("Aumento de {} eh {}".format(valor, aumento))
diminuto = moeda.diminuir(valor, 10)
print("Diminuto de {} eh {}".format(valor, diminuto))
dobro = moeda.dobro(valor)
print("Dobro de {} eh {}".format(valor, dobro))
metade = moeda.metade(valor)
print("Metade de {} eh {}".format(valor, metade))