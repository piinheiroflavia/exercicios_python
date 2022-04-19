funcionario = 1
salario = 0

while funcionario < 3:
    salario = int(input('digite o valor do salário: '))
    
    if salario <= 500:
        bonificacao = salario*0.5
        soma_salario = salario + bonificacao
        print(soma_salario)
        print('bonificação: ',bonificacao)
        
    elif(salario >= 500 <=1200):
        bonificacao = salario*0.12
        soma_salario = salario + bonificacao
        print(soma_salario)
        print('bonificação: ',bonificacao)
        
    else:
         salario>=1200 
         bonificacao = salario
         soma_salario = salario + bonificacao
         print(soma_salario)
         print('bonificação: ',bonificacao)
      
funcionario +=1
