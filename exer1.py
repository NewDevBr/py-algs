print("*********** Verificar se um inteiro é positivo ou negativo ***********");
num = int(input("Digite um número: "))
if(num > 0):
    print("O valor digitado é um número positivo.")
else:
    if (num == 0):
        print("O valor digitado é um número neutro.")
    else:
        print("O valor digitado é um número negativo.")