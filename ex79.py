num = []
while True:
    n = int(input("Numero: "))
    a = str(input("[S/N]: ".upper()))
    num.append(n)
    if a in "Nn":
        break

print(num)