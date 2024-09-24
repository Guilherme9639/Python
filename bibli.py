#Importação da biblioteca que vamos usar, fiz a instalação via vscode no terminal usando o seguinte comando pip install matplotlib

import matplotlib.pyplot as plt

# Classe para representar um livro

class Livro:

    def __init__(self, titulo, autor, ano_publicacao):

        self.titulo = titulo

        self.autor = autor

        self.ano_publicacao = ano_publicacao

 

    def __str__(self):

        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

 

# Criar uma lista de livros vazia e ano

biblioteca = []
anos = []

# Função para adicionar um livro à biblioteca

def adicionar_livro(titulo, autor, ano_publicacao):

    novo_livro = Livro(titulo, autor, ano_publicacao)

    biblioteca.append(novo_livro)

    print(f"O Tilulo '{titulo}', foi adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca

def listar_livros():

    print("Livros da Biblioteca: ")

    for livro in biblioteca:

        print(livro)

# Adicionar alguns livros à biblioteca

adicionar_livro( "Ao Farol" , "Virginia Wolf" , 1921)

adicionar_livro("A casa dos espíritos ", "Isabel Allende" , 1982)

adicionar_livro(" Memórias póstumas de Brás Cubas ","Machado de Assis" , 1881)

adicionar_livro("Cem Anos de Solidão","Gabriel Garcia Marquez" , 1967)

adicionar_livro("O Rei Lear","William Shakespeare" , 1606)

 

# Listar todos os livros na biblioteca

listar_livros()

# Criar um gráfico de livros por ano

anos = list(set(anos))# Remove duplicatas dos anos

anos.sort()

 

# Contagem de livros por ano

contagem_por_ano = [anos.count(ano) for ano in anos]

 

# Criar um gráfico de linha

plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')

plt.xlabel('Ano de Publicação')

plt.ylabel('Número de Livros')

plt.title('Distribuição dos livros mais famosos por ano conforme o site: https://www.culturagenial.com/melhor-livro-do-mundo/')

 

# Adicionar rótulos aos pontos de dados

for i, valor in enumerate(contagem_por_ano):

    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')

 

plt.grid(True)

 
plt.show()