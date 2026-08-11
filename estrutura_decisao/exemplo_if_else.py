def aluno_aprovado():
    nota_1 = float(input("digite a primeira nota: "))
    nota_2 = float(input("digite a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    if media >= 6:
        print("Aprovado")
        elif media