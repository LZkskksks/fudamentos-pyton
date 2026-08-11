def posso_entrar_no_show_do_veigh():
    POSSUI_IGRESSO = True
    idade = int(input("Digite sua idade: "))
    nome_esta_na_lista = bool(input(f"se nome esta na lista?: "))

    posso_entrar = (nome_esta_na_lista or POSSUI_IGRESSO) and idade >= 18
    print(f"vou conseguir entrar no show? {posso_entrar}")

posso_entrar_no_show_do_veigh()