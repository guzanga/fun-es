def ficha(a, b= 0):
    print("\nesta é a ficha de jogador dele")
    print("\nnome do jogador:",a)
    print("gols marcados:",b)

nome = str(input("digite o nome do jogador"))
gol = int(input("digite quantos gols ele marcou"))

ficha(nome)