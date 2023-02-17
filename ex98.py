def contagem(inicio, fim, intervalo):
    cont = inicio
    while cont < fim:
        print(cont, end=' ')
        cont = cont + intervalo



contagem(1,10,1)
print(" ")
contagem(20,100,2)
print(" ")
contagem(0,50,5)