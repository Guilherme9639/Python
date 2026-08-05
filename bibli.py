"""Gerencia uma pequena biblioteca e exibe livros por ano de publicação."""

from collections import Counter
from dataclasses import dataclass

import matplotlib.pyplot as plt


@dataclass(frozen=True)
class Livro:
    titulo: str
    autor: str
    ano_publicacao: int

    def __str__(self) -> str:
        return (
            f"{self.titulo}, de {self.autor} "
            f"({self.ano_publicacao})"
        )


def listar_livros(livros: list[Livro]) -> None:
    print("Livros da biblioteca:")
    for livro in livros:
        print(f"- {livro}")


def criar_grafico(livros: list[Livro]) -> None:
    """Exibe a quantidade de livros cadastrados por ano."""
    contagem = Counter(livro.ano_publicacao for livro in livros)
    anos = sorted(contagem)
    quantidades = [contagem[ano] for ano in anos]

    plt.bar(anos, quantidades, color="#35689a")
    plt.xlabel("Ano de publicação")
    plt.ylabel("Quantidade de livros")
    plt.title("Livros cadastrados por ano de publicação")
    plt.xticks(anos, rotation=45)
    plt.tight_layout()
    plt.show()


def main() -> None:
    biblioteca = [
        Livro("Ao Farol", "Virginia Woolf", 1927),
        Livro("A Casa dos Espíritos", "Isabel Allende", 1982),
        Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
        Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
        Livro("O Rei Lear", "William Shakespeare", 1606),
    ]

    listar_livros(biblioteca)
    criar_grafico(biblioteca)


if __name__ == "__main__":
    main()
