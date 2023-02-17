temp = []
princ = []
mai = 0
men = 0
while True:
    temp.append(str(input("Nome: ")).strip())
    temp.append(str(input("Idade: ")).strip())
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("[S/N]"))
    if resp in "Nn":
        break
print("{}".format(princ))
print("O maior peso foi de {}. ".format(mai), end='')
for p in princ:
    if p[1] == mai:
        print("Peso de {}".format(p[0]))
print("O menor peso foi de {}. ".format(men), end='')
for p in princ:
    if p[1] == men:
        print("Peso de {}".format(p[0]))