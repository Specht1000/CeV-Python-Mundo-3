matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]
soma_par = 0
soma_impar = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite um valor para [{}] [{}]: ".format(i,j)))

print(matriz)
for i in range(0,3):
    for j in range(0,3):
        print("[{}]".format(matriz[i][j]), end='')
    print()

for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0:
            soma_par = soma_par + matriz[i][j]
print("Soma dos pares eh {}".format(soma_par))

for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 != 0:
            soma_impar = soma_impar + matriz[i][j]
print("Soma dos pares eh {}".format(soma_impar))
