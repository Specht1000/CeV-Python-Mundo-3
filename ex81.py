num = []
while True:
    n = int(input("Numero: "))
    a = str(input("[S/N]: ".upper()))
    num.append(n)
    if a in "Nn" or not "Ss":
        break
num.sort(reverse=True)
print("Ordem decrescente: {}".format(num))

if 5 in num:
    print("O numero 5 esta na lista")
else:
    print("O numero 5 NAO esta na lista")