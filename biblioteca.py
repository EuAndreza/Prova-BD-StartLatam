import sqlite3

conectar = sqlite3.connect('biblioteca.db')
cursor = conectar.cursor()

def criar_tabela():
	cursor.execute("""
		CREATE TABLE livros(
		codigo INTEGER NOT NULL PRIMARY KEY ,
		nome VARCHAR(100) NOT NULL);
		""")
	return 'tabela criada com sucesso'

def inserir_dados(x,y):
	cursor.execute(""" INSERT INTO livros(codigo,nome)VALUES(?,?)""",
		(x,y))
	conectar.commit()
	return 'dados inseridos com sucesso'

def mostrar_dados():
	cursor.execute("""SELECT * FROM livros """)
	for linha in cursor.fetchall():
		print(linha)

def atualizar_dados(x,y):
	cursor.execute(""" UPDATE livros SET nome = ? WHERE codigo = ? """,
		(x,y))
	conectar.commit()
	return 'atualizado com sucesso'

def deletar_livro(x):
	cursor.execute(""" DELETE FROM livros WHERE codigo = ?""",
		(x,))
	conectar.commit()
	return 'deletado com sucesso'