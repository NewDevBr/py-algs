print("*************** dias da semana ****************")
days = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
number = int(input('Digite a quantidade de dias no futuro: '))
number = (5 + number) % days.__len__()
number= days[number]
print("Será: ", number)