num = []
for i in range(1,5):
    num.append(int(input("Numeros: ")))

print(num)
print("Maior numero: {} na posicao {}".format(max(num), num.index(max(num))))
print("Menor numero: {} na posicao {}".format(min(num), num.index(min(num))))
