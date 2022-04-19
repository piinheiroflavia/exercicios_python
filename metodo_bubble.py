lista = []
num = int(input("Digite a quantidade de notas: "))

for i in range(num):
  value = float(input("Digite a nota %d: " %i))
  lista.append(value)

for i in range(num -1):
  for notas in range(num - i - 1):
    if (lista[notas] > lista [notas + 1]):
      temp = lista[notas]
      lista[notas] = lista[notas+1]
      lista[notas+1] = temp

print('A ordem das notas são: ', lista)
