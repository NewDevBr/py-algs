print("*************** dias da semana ****************")
days = ['Domingo', 'Segunda', 'Ter�a', 'Quarta', 'Quinta', 'Sexta', 'S�bado']
number = int(input('Digite a quantidade de dias no futuro: '))
number = (5 + number) % days.__len__()
number= days[number]
print("Ser�: ", number)