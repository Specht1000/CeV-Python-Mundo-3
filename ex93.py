jogador = {}
gols = []
jogador['nome'] = str(input("Nome do jogador: "))
tot = input("Total de jgoos: ")

for i in range(1,tot):
    gols.append(int(input("Quantos gols no jogo {}: ".format(i))))
jogador['gol'] = gols

soma = 0
for i in gols:
    soma = soma + i
print("Total de gols: {}".format(soma))

partidas = 1
for k, v in jogador.items():
    print("Na partida {}, {} fez {} gols.".format(partidas, jogador["nome"], jogador["gol"][partidas-1]))
    partidas = partidas + 1
