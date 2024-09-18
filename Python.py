#para saber uma nota de um aluno por exemplo,, podemos fazer da seguinte forma#

prova = int(input("Digite o valor da prova:"))
trabalho = int(input("Digite o valor do trabalho:"))
valores_individuais = int(input("Digite o valor dos valores individuais:"))
media = (prova + trabalho + valores_individuais)/3

if media >= 6:
    situacao = "Aluno Aprovado"
else:
    situacao = "Aluno Reprovado"
    
    print(f" A media das notas é:{media}")
    print(f" A situação do aluno é:{situacao}")