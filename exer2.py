print("**** Exibe o menor número digitado ****")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if (n1 > n2):
    print("{} é o menor número.".format(n2))
else:
    if(n1 < n2):
        print("{} é o menor número.".format(n1))
    else:
        print("Os valores digitados são iguais.")