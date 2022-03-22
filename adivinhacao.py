numero = 35
chute_texto = input('Digite um número: \n')
chute = int(chute_texto)

acertou = chute == numero
maior = chute > numero
if(acertou):
  print('Você está certo!!')
else:
  if (maior):
    print('Você errou! o seu chute foi maior que o número secreto')
  else:
    print('Você errou! O chute foi menor que o número secreto')
