salario = float(input('Digite o salario: '))
idade = int(input('Digite sua idade: '))

if (salario >= 1200) and (idade >= 18):
    bonificacao = float(salario + 500)
    print('Parabés você ganhou uma bonifiação de R$%3.2f reais' %bonificacao)
else:
    print('Não há bonificação')
