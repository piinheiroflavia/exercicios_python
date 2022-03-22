nome = input('Qual seu nome? \n')
nota_1 = float(input('Qual foi sua nota do 1º brimestre? \n'))
nota_2 = float(input('Qual foi sua nota do 2º brimestre? \n'))
nota_3 = float(input('Qual foi sua nota do 3º brimestre? \n'))
nota_4 = float(input('Qual foi sua nota do 4º brimestre? \n'))
aprovacao = 7.0
exame = 6.0
mensagem = ''
#calculos
soma = nota_1+nota_2+nota_3+nota_4
media_final = float(soma/4)
#mensagem reprovado, exane ou aprovado
if media_final >= aprovacao:
  mensagem ='Parabéns, Aprovado!!'
elif media_final >= exame:
  mensagem = 'Exame!'
else:
  mensagem = 'Reporvado'

print('Nome:', nome)
print('Média: ', media_final)
print('Status: ', mensagem)
