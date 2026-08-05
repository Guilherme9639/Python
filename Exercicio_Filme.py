"""Permite avaliar uma lista de filmes com notas de 1 a 5."""

FILMES = [
    "Interestelar",
    "Fragmentado",
    "Divertida Mente",
    "A Lagoa Azul",
    "Vingadores",
]


def solicitar_avaliacao(filme: str) -> int:
    """Solicita uma avaliação válida ou zero para encerrar."""
    while True:
        resposta = input(
            f"Avalie '{filme}' de 1 a 5 ou digite 0 para encerrar: "
        )
        try:
            nota = int(resposta)
        except ValueError:
            print("Digite somente números inteiros.")
            continue

        if 0 <= nota <= 5:
            return nota
        print("A nota deve estar entre 1 e 5, ou ser 0 para encerrar.")


def main() -> None:
    avaliacoes: dict[str, int] = {}

    print("Bem-vindo à avaliação de filmes!")

    for filme in FILMES:
        nota = solicitar_avaliacao(filme)
        if nota == 0:
            print("Avaliação encerrada.")
            break

        avaliacoes[filme] = nota
        print(f"Você avaliou '{filme}' com {nota} estrela(s).")

    print("\nResumo das avaliações:")
    if not avaliacoes:
        print("Nenhum filme foi avaliado.")
    else:
        for filme, nota in avaliacoes.items():
            print(f"- {filme}: {nota}/5")


if __name__ == "__main__":
    main()
