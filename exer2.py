print("**** Exibe o menor n�mero digitado ****")
n1 = int(input("Digite um n�mero: "))
n2 = int(input("Digite outro n�mero: "))
if (n1 > n2):
    print("{} � o menor n�mero.".format(n2))
else:
    if(n1 < n2):
        print("{} � o menor n�mero.".format(n1))
    else:
        print("Os valores digitados s�o iguais.")