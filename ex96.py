def calculo_area(l, c):
    return l*c


largura = int(input("Largura: "))
comprimento = int(input("Comprimento: "))
area = calculo_area(largura, comprimento)
print("Área = {}m²".format(area))