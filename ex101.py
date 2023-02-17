from datetime import date

def voto(ano):
    idade_atual = date.today().year - ano
    if ano > date.today().year:
        print("Ano impossivel.")
    else:
        if idade_atual < 16:
            return "Não pode votar."
        elif idade_atual >= 16 and idade_atual < 18:
            return "Voto facultativo."
        elif idade_atual >= 18:
            return "Voto obrigatório."


resultado = voto(int(input("Em que ano você nasceu: ")))
print(resultado)