matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite um valor para [{}] [{}]: ".format(i,j)))

print(matriz)
for i in range(0,3):
    for j in range(0,3):
        print("[{}]".format(matriz[i][j]), end='')
    print()