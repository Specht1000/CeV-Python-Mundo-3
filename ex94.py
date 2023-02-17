pessoas = {}
new_pessoas = []
soma = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas['idade'] 
    pessoas['sexo'] = str(input("Sexo[M/F]: ".upper()))
    if pessoas['sexo'] not in 'MmFf':
        print("Erro na descrição do sexo")
    new_pessoas.append(pessoas.copy())
    continuar = str(input("Deseja continuar [S/N]: ".upper()))
    if continuar in 'Nn':
        break

print(new_pessoas)
print("Numero de pessoas cadastradas é {}".format(len(new_pessoas)))
media = soma / len(new_pessoas)
print("A média da idade das pessoas é {}".format(media))
for p in new_pessoas:
    if p['idade'] >= media:
        print("{} tem a idade acima da media com {}".format(p['nome'], p['idade']))



