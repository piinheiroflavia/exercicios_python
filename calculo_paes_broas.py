paes = float(input('digite a quantidade de pães: '))*1.10
broas = float(input('digite a quantidade de broas: '))*2.50

paes_broas = float(paes + broas)
guardar = float(paes_broas * 0.1)

print('quantidade total de pães e broas vendidos é %3.1f reais' %paes_broas)
print('valor a guardar é %3.1f reais' %guardar)
