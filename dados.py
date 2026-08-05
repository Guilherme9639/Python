"""Exemplo de persistência com SQLite usando somente dados fictícios."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("contatos.db")

CONTATOS_EXEMPLO = [
    ("Ana Silva", "ana.silva@example.com", "(11) 90000-0001"),
    ("Bruno Souza", "bruno.souza@example.com", "(21) 90000-0002"),
    ("Carla Lima", "carla.lima@example.com", "(31) 90000-0003"),
]


def criar_tabela(conexao: sqlite3.Connection) -> None:
    """Cria a tabela de contatos caso ela ainda não exista."""
    conexao.execute(
        """
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefone TEXT NOT NULL
        )
        """
    )


def inserir_contatos(
    conexao: sqlite3.Connection,
    contatos: list[tuple[str, str, str]],
) -> None:
    """Insere os contatos sem duplicar endereços de e-mail."""
    conexao.executemany(
        """
        INSERT OR IGNORE INTO contatos (nome, email, telefone)
        VALUES (?, ?, ?)
        """,
        contatos,
    )


def listar_contatos(conexao: sqlite3.Connection) -> list[tuple]:
    """Retorna todos os contatos em ordem alfabética."""
    cursor = conexao.execute(
        "SELECT id, nome, email, telefone FROM contatos ORDER BY nome"
    )
    return cursor.fetchall()


def main() -> None:
    with sqlite3.connect(DB_PATH) as conexao:
        criar_tabela(conexao)
        inserir_contatos(conexao, CONTATOS_EXEMPLO)

        print("Contatos cadastrados:")
        for contato_id, nome, email, telefone in listar_contatos(conexao):
            print(f"{contato_id}: {nome} | {email} | {telefone}")


if __name__ == "__main__":
    main()
