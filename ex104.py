def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO")
        if ok:
            break
    return valor


n = leiaInt("Digite um numero: ")
print("Voce digitou o numro {}.".format(n))
