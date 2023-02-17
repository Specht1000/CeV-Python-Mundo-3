alunos = {}
alunos['aluno'] = str(input("Nome do aluno: "))
alunos['nota'] = float(input("Nota do aluno: "))

if alunos['nota'] >= 7.0:
    print("Aluno {} aprovado.".format(alunos['aluno']))
    alunos['situacao'] = "Aprovado"
else:
    print("Aluno {} reprovado.".format(alunos['aluno']))
    alunos['situacao'] = "Reprovado"

print(alunos)

for k, v in alunos.items():
    print("- {} é igual a {}".format(k, v))