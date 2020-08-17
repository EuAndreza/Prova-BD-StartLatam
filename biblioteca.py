import sqlite3

conectar = sqlite3.connect('biblioteca.db')
cursor = conectar.cursor()

def criar_tabela():
	cursor.execute("""
		CREATE TABLE livros(
		codigo INTEGER NOT NULL PRIMARY KEY ,
		nome VARCHAR(100) NOT NULL);
		""")
def inserir_dados(x,y):
	cursor.execute(""" INSERT INTO livros(codigo,nome)VALUES(?,?)""",
		(x,y))
	conectar.commit()
def mostrar_dados():
	cursor.execute("""SELECT * FROM livros """)
	for linha in cursor.fetchall():
		print(linha)
def atualizar_dados(x,y):
	cursor.execute(""" UPDATE livros SET nome = ? WHERE codigo = ? """,
		(x,y))
	conectar.commit()

def deletar_livro(x):
	cursor.execute(""" DELETE FROM livros WHERE codigo = ?""",
		(x,))
	conectar.commit()

acesso = input('Seu banco de dados já existe? S para sim N para nao\n**').lower()
if acesso == 's':
	criar_tabela()
else:
	print('***BEM-VINDX***\n')

rep = 's'
while  rep == 's':
	pergunta = input("#Para inserir um livro digite IN\n#Para atualizar o livro digite UP\n#Para mostrar todos os "
	"livros cadastrados digite EX\n#Para apagar algum livro digite DEL\n**").lower()

	if pergunta == 'in':
		codigo = int(input('digite o codigo para o livro\n**'))
		nome = input('digite o nome do livro\n**')
		inserir_dados(codigo, nome)
		print('\nlivro inserido com sucesso\n')
		mostrar_dados()
		rep = input('\ndeseja fazer mais alguma coisa? S para sim N para nao\n**').lower()

	elif pergunta == 'up':
		mostrar_dados()
		codigo = int(input('digite o codigo do livro que deseja atualizar\n**'))
		nome = input('agora digite o novo nome para o livro\n**')
		atualizar_dados(nome, codigo)
		print('\nlivro atualizado com sucesso\n')
		mostrar_dados()
		rep = input('\ndeseja fazer mais alguma coisa? S para sim N para nao\n**').lower()

	elif pergunta == 'ex':
		mostrar_dados()
		rep = input('\ndeseja fazer mais alguma coisa? S para sim N para nao\n**').lower()

	elif pergunta == 'del':
		mostrar_dados()
		codigo = int(input('\ndigite o codigo do livro que deseja apagar\n**'))
		deletar_livro(codigo)
		print('\nlivro apagado com sucesso\n')
		mostrar_dados()
		rep = input('\ndeseja fazer mais alguma coisa? S para sim N para nao\n**').lower()
print('***OBRIGADA!***')

conectar.close()