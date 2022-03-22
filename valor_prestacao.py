valor_compra = float(input('digite o valor de sua compra: '))
valor_prestacao = float(input('digite em quantas vezes foi parcelado: '))
valor = float(valor_compra/valor_prestacao)

print('o valor das suas prestações é %3.1f' %valor)
