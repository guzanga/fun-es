print("------------------")
print("senai legal")
print("------------------")

#def cria uma função, neste caso quero que ele imprima 20 tracinhos
def linha():
    print("-" * 20)

linha()
print("sesilegal")
linha()

#aqui foi utilizado txt para pdr colacar uma mensagem sem ter d chamar dua vezes uma mesma função, facilitando o seu dia
def linha(txt):
    print("-" * 20)
    print(txt)
    print("-" * 20)

linha("sesilegal")
linha("senailegal")

#esta uma função que realiza uma soma de dois numeros
def soma(a,b):
    s = a + b
    print("soma", s)

soma(1, 300)
soma(a = 20,  b = 40)

#posso colocar quantos numeros eu quiser que realizara a soma
def soma(*valores):
    S = 0
    for C in valores:
        S += C
    return S

print(soma(1,1))

#
def soma(a,b):
    g = a + b
    print("soma", g)

    return g

A = soma(1,300)

#ex de exercicio base

def parouimpar(num):
    if num %2 == 0:
        print("é par")
    else:
        print("é impar")

parouimpar(int(input("digite um numero")))
