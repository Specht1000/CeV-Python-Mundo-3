def fatorial(num, show=False):
    cont = 1
    for i in range(num, 0, -1):
            cont = cont * i
    if show == True:  
        for i in range(num, 0, -1):
            if i == 1:
                print("{} = {}".format(i, cont))
            else:
                print("{} x".format(i), end=' ') 
    else:
        return cont

print(fatorial(5, show=True))