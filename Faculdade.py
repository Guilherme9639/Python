#Estruturas Condicionais com Python#

idade = int(input("Coloque aqui a sua idade: "))

if idade < 18:
  print("Menor de idade")

elif idade >= 18 and idade < 65:
  print("Adulto")

else:
  print("Idoso")


#Exercicio de fixação#

idade = int(input("Coloque aqui a sua idade: "))

if idade < 12:
  print("Recomendamos o filme intantil Filme1")

elif 12 <= idade < 18:
  print("Recomendamos o filme2")

else:
  print("Recomendamos filme 3")
