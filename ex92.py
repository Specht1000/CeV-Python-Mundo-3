trabalhador = {}

trabalhador['nome'] = str(input("Nome: "))
trabalhador['ano de nascimento'] = int(input("Ano de nascimento: "))
trabalhador['clt'] = int(input("CLT(0 nao tem): "))

if trabalhador['clt'] != 0:
    trabalhador['ano da contratacao'] = int(input("Ano da contratacao: "))
    trabalhador['salario'] = str(input("Salario: R$ "))

idade_atual = 2022 - trabalhador['ano de nascimento']
trabalhador['ano_aposentadoria'] = idade_atual + 30

for k, v in trabalhador.items():
    print("O {} eh {}".format(k, v))

print(trabalhador)




