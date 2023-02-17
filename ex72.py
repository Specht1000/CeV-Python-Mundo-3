nomes = ("um","dois","tres","quatro","cinco","seis","sete","oito","nove", "dez")
a = int(input("Numero de 1 - 10: "))

if 0 <= a <= 9:
    print(nomes[a-1])
