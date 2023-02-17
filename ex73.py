times = ("Gremio","Internacional","Ypiranga","Caxias","Avenida","Sao Jose","Brasil de Pelotas","Novo Hamburgo",
         "Juventude","Sao Luiz","Aimore","Esportivo")
print("Os cinco primeiro:")
for i,j in enumerate(times[:5]):
    print("{}º. {}".format(i+1, j))

print("")

print("Os cinco ultimos:")
for i,j in enumerate(times[8:12]):
    print("{}º. {}".format(i+9, j))

print(sorted(times))
print("Posição do Juventude é {}º colocado".format(times.index("Juventude")))

