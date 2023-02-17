num = []
num_pares = []
num_impares = []

while True:
    n = int(input("Numero: "))
    a = str(input("[S/N]: ".upper()))
    num.append(n)
    if a in "Nn" or not "Ss":
        break

for i in num:
    if i % 2 == 0:
        num_pares.append(i)

for i in num:
    if i % 2 != 0:
        num_impares.append(i)

print("Numeros pares {}: ".format(num_pares))
print("Numeros pares {}: ".format(num_impares))