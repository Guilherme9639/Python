#Exercicio de criação de uma classificação de filmes#

filmes = ["Interinstelar", "Fragmentado", "Divertidamente", "Lagoa Azul", "Vingadores"]

print("Bem vindo a classificação de filmes!")
print("Você tem até 5 filmes para classificar.")
print("Caso deseje sair sair da avaliação, digite 0 a qualquer momento.")

for filme in filmes:
    classificacao = input(f"Digite aqui um valor de 1 a 5 para classificar o filme '{filme}' ou 0 para parar. ")

    if classificacao == "0":
        print("Que pena que você não irá classificar mais os filmes, até logo!")
        break
classificacao = int(classificacao)
#para transformar o numero de classificação em inteiro caso alguem coloque falor float.

if classificacao < 1 or classificacao > 5:
        print("Por favor, digite uma classificação válida de 1 a 5.")
else:
        print(f"Você classificou '{filme}' com '{classificacao}' estrelas. \n")

print("Obrigado por classificar os filmes, volte sempre!")