def notas(*n, sit=False):
    resultados = {}
    resultados['tamanho'] = len(n)
    resultados['maior'] = max(n)
    resultados['menor'] = min(n)
    resultados['media'] = sum(n) / len(n)
    if sit == True:
        if resultados['media'] >= 7.0:
            resultados['situacao'] = "Aprovado"
        else:
            resultados['situacao'] = "Reprovado"
    return resultados


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
resp = notas(8.8, 7.8, 8.2, 7.6, sit=True)
print(resp)
resp = notas(6.1, 4.3, 3.5, 1,2, 7,5, sit=True)
print(resp)