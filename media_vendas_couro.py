#Calculo do preço de custo e preço final

v_couro = float(input('Digite o valor do couro:'))
v_solado = float(input('Digite o valor do solado:'))
v_cordoes = float(input('Digite o valor do cordões:'))
v_insumos = float(input('Digite o valor do insumo:'))
v_MaoObra = float(input('Digite o valor do mão de obra:'))
v_marketing = float(input('Digite o valor do marketing:'))
v_vendas = float(input('Digite o valor do custos de venda:'))

preco_custo = (v_couro*0.30)+(v_solado*0.20)+(v_cordoes*0.05)+(v_insumos*0.05)+(v_MaoObra*0.20)+(v_marketing*0.10)+(v_vendas*0.10)
print('O valor de custo unitário deste modelo de sapato',preco_custo)

#calculo do preco final
preco_lucro = preco_custo*1.30
preco_perdas = preco_lucro*1.15
preco_ipi_cofins = preco_perdas*1.15
preco_vendas = preco_ipi_cofins*1.25
preco_icm_inss = preco_vendas*1.30

#preco final, acrescido de todos os impostos e margens de lucro
preco_final = preco_icm_inss
print('O preço final ao consumidor deste modelo de sapato é:', preco_final)
