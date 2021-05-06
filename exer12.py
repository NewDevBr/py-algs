print("********* Média ponderada de notas *********")
numerator, denominator = 0, 0
for x in range(1,4):
    nota = (float(input("Digite a {}ª nota: ".format(x))))
    peso = (float(input("Digite o peso da {}ª nota: ".format(x))))
    numerator += nota * peso
    denominator += peso
weightAverage = numerator / denominator
if (weightAverage >= 0 and weightAverage < 5):
    print("Conceito: R")
elif (weightAverage < 6):
    print("Conceito: D")
elif (weightAverage < 7):
    print("Conceito: C")
elif (weightAverage < 8):
    print("Conceito: B")
else:
    print("Conceito: A")
print("A média ponderada é: ", weightAverage)