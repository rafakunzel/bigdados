-- Criação de banco de dados relacionais
CREATE DATABASE online_vendas;
USE online_vendas;
CREATE TABLE Produto (
id_produto int primary key not null auto_increment,
nome_produto varchar(100),
categoria varchar(50),
preco decimal(10,2),
estoque int
);
Select * From produto;

conectar sql no python 
import mysql.connector
#conectar o sql no python
conexao = mysql.connector.connect(
 host="127.0.0.1",
 user="root",
 password="",
 database="online_vendas"
)
# 2. Criar um objeto cursor para executar as queries
cursor = conexao.cursor()
# 3. Definir a query
query = "SELECT * FROM produto"
# 4. Executar a query
cursor.execute(query)
# 5. Obter os resultados
resultados = cursor.fetchall()
# 6. Exibir os resultados
for linha in resultados:
 print(linha)
