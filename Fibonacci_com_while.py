#pergunta para o usuario
pergunta = int(input("Digite um número:"))
# começo do loop/loop para quando digita 0
while pergunta != 0:
    # laços condicionais
    if pergunta == 1:
        print (0)
    elif pergunta == 2:
        print (0)
        print (1)
    else:
        #variaveis
        num1 = 0
        num2 = 1
        num3 = num1 + num2
        #primeiros prints
        print (num1)
        print (num2)
        print (num1, "+", num2, "=", num3)
    # tentando a conta em while
    p=4
    while p <= pergunta:
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        # mostrar pro usuario o fibonacci
        print (num2, "+", num1 ,"=", num3)
        # (p recebe p mais 1) -> contador
        p = p + 1
     #pergunta para continuar ou nao continuar
    pergunta = int(input("Digite outro número ou digite \"0\" para encerrar:"))

print( "-" * 60 )
print ("\n\tFim do programa, Obrigada!")