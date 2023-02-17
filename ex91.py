from random import randint
from operator import itemgetter

jogo = {'Jogador1': randint(1 ,6),
        'Jogador2': randint(1 ,6),
        'Jogador3': randint(1 ,6),
        'Jogador4': randint(1 ,6)
        }

for k, v in jogo.items():
    print("{} tirou o numero {}".format(k, v))

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print("{}º lugar foi o {} que tirou o numero {}".format(i+1, v[0], v[1]))
