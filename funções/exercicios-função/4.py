def voto(a):
    if a >= 70:
        print("opcional")
    elif a >= 16 and a < 18:
        print("opicional")
    elif a < 16:
        print("negado")
    else:
        print("obrigatório")

voto(int(input("digite sua idade:")))