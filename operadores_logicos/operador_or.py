def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input(f"tem dinheiro?"))
    atorizado = tem_dinheiro or TEM_CARTAO
    print(f"vou comer MC-donalds hoje? {atorizado}")
    posso_comprar()
