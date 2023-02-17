def ficha(n = "<desconhecido>", g = 0):
    if g == 1:
        print("O jogador {} fez {} gol.".format(n, g))
    elif g < 0:
        print("ERRO")
    else:
        print("O jogador {} fez {} gols".format(n, g))
        

nome = str(input("Nome do jogador: "))
gols = int(input("Nº de gols: "))
ficha(nome, gols)