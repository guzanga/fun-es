l = []

while True:
    n = input("Digite os números da lista. Para sair, digite '0': ")
    if n == '0':
        break

    if not n.isdigit():
        print("Digite um número válido.")

    else:
        l.append(int(n))

print('\nLista com os numeros digitados: ', l)

def maior():
    m = max(l)
    return m

x = maior()
print('O maior valor digitado na lista foi: ', x)
