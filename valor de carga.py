qtd_caminhoes = 4
caminhoes = 0

while caminhoes < qtd_caminhoes:
  print('---------------------------------------------------')
  print('Código de carga é entre 10 e 40.')
  print('Código de estado entre 1 e 5.')
  print('O peso da carga é em toneladas.')
  print()
  caminhoes = int(input('Digite qual é seu número do caminhão: '))
  cod_carga = int(input('Digite o código de carga: '))
  
  if (cod_carga >= 10 and cod_carga <= 20):
      
      peso = float(input('Digite a tonelada da carga: '))
      pesoQuilo = peso*1000
      precoCarga = float(pesoQuilo*100)
    
  elif (cod_carga >= 21 and cod_carga <= 30):
      peso = float(input('Digite o peso da carga: '))
      pesoQuilo = peso*1000
      precoCarga = float(pesoQuilo*250)

  elif (cod_carga >= 31 and cod_carga <= 40):
      peso = float(input('Digite o peso da carga: '))
      pesoQuilo = peso*1000
      precoCarga = float(pesoQuilo*340)
    
  else:
    print('Carga Inválido')
    
  cod_estado = int(input('Digite o código de Estado: '))
  print()
  print()
  
  if cod_estado == 1:
    imposto = 35
    v_imposto = float(precoCarga*0.35)
    s_total = float(precoCarga+v_imposto)
    
    print ('O imposto de acordo com seu estado é de',imposto,'%')
    print('Seu preço por quilo saí a R$ %4.2f' %precoCarga)
    print('O valor total transportado pelo caminhão: R$ %4.2f' %s_total)
    
  elif cod_estado == 2:
    imposto = 25
    v_imposto = float(precoCarga*0.25)
    s_total = float(precoCarga+v_imposto)
    
    print ('O imposto de acordo com seu estado é de',imposto,'%')
    print('Seu preço por quilo saí a R$ %4.2f' %precoCarga)
    print('O valor total transportado pelo caminhão: R$ %4.2f' %s_total)

  elif cod_estado == 3:
    imposto = 15
    v_imposto = float(precoCarga*0.15)
    s_total = float(precoCarga+v_imposto)
    
    print ('O imposto de acordo com seu estado é de',imposto,'%')
    print('Seu preço por quilo saí a R$ %4.2f' %precoCarga)
    print('O valor total transportado pelo caminhão: R$ %4.2f' %s_total)
    
  elif cod_estado == 4:
    imposto = 5
    v_imposto = float(precoCarga*0.05)
    s_total = float(precoCarga+v_imposto)
    
    print ('O imposto de acordo com seu estado é de',imposto,'%')
    print('Seu preço por quilo saí a R$ %.2f' %precoCarga)
    print('O valor total transportado pelo caminhão: R$ %2.2f' %s_total)
    
  elif cod_estado == 5:
    s_total = float(precoCarga)
    print('Isento do imposto')
    print('O valor total transportado pelo caminhão: R$ %4.2f' %s_total)
    
  else:
    print('Estado Inválido')

  print()
caminhoes += 1
