salario = float(input('Digite o valor do seu salário: '))

porcetagem = float(input('Digite o valor da porcentagem: '))

aumento = salario*porcetagem / 100

soma_total = aumento + salario

print('o novo salário é: %2.1f' %soma_total)
