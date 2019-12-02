salario=float(input('Qual é o salario do funcionario? R$ '))
print('Um funcionario que ganhava R${:.2f},com 15% de aumento passa a ganhar R${:.2f} '.format(salario, (salario+(salario * 15 / 100))))
