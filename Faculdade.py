#Estruturas Condicionais com Python#

idade = int(input("Coloque aqui a sua idade: "))

if idade < 18:
  print("Menor de idade")

elif idade >= 18 and idade < 65:
  print("Adulto")

else:
  print("Idoso")