nome_cliente = input("Digite seu nome: ")
idade_cliente = int(input("Digite sua idade: "))
peso_cliente = float(input("Digite seu peso: "))
altura_cliente = float(input("Digite sua altura: "))

imc = float(peso_cliente/(altura_cliente*altura_cliente))

print ("Nome: %s" %nome_cliente)
print ("Idade: %d" %idade_cliente)
print ("Peso: %4.2f kg" %peso_cliente)
print ("Altura: %2.1f" %altura_cliente)
print ("IMC: %2.1f " %imc)

# %s é string
# %d é para inteiro
# %f é para número com ponto (decimal)
