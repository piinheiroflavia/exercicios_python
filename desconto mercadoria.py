preco = float(input('Digite o preço da mercadoria: '))
porcetagem = float(input('Digite o percentual de desconto: '))

valor_desconto = preco*porcetagem / 100

valor_a_pagar = preco - valor_desconto

print('O seu valor a pagar é de R$ %3.2f reais' %valor_a_pagar)
