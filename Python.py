"""Calcula a média de um estudante a partir de três avaliações."""


def ler_nota(descricao: str) -> float:
    """Solicita uma nota válida entre 0 e 10."""
    while True:
        try:
            nota = float(input(f"Digite a nota de {descricao} (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um valor numérico válido.")


def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def main() -> None:
    notas = [
        ler_nota("prova"),
        ler_nota("trabalho"),
        ler_nota("atividades individuais"),
    ]
    media = calcular_media(notas)
    situacao = "Aprovado" if media >= 6 else "Reprovado"

    print(f"Média final: {media:.2f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    main()
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
