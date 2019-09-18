import math

# Constante que define o numero máximo de iterações que o método irá realizar
MAX_ITER = 1000000

# Função que será analisada
def func(x):
    return (math.pow(x,3) - math.pow(x,2) + 2)  # Função x³ - x² + 2

# Calcula a raiz da função(x) dado o intevalo [a,b]


def posicaoFalsa(a, b):
    if func(a) * func(b) >= 0:
        print("Você assumiu valores errados para a e b")
        return -1

    c = a  # Inicia o resultado com o valor de a

    for i in range(MAX_ITER):
        # Procura o ponto que toca o eixo x
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        print(i)
        # Verifica se o ponto calculado é raiz
        if func(c) == 0:
            print("ae carai")
            break
        elif func(c) * func(a) < 0:
            b = int(c)
        else:
            a = int(c)
    print("O valor da raiz é : ", '%.4f' % c)


# Função principal
if __name__ == '__main__':
    a = int(input("Digite o valor de a:"))
    b = int(input("Digite o valor de b:"))
    posicaoFalsa(a, b)