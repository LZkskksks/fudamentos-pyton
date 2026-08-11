from operator import truediv


def pode_dirigir():
    idade = int(input("Qual a sua idade?"))
    TEM_HABILITACAO = True

    autorizado = idade >= 18 and TEM_HABILITACAO

    print(f"usuario pode dirigir {autorizado}")

    pode_dirigir()
