print("************** Peso ideal **************")
height = float(input("Digite sua altura: "))
sex = input("Digite seu sexo (m/f): ")
if (sex.upper() == "M"):
    idealWeight = (72.7 * height) - 58
else:
    idealWeight = (62.1 * height) - 44.7
print("O peso ideal é: ", idealWeight)