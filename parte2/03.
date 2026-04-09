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
truncate table produto; #esvazia a tabela 

CREATE TABLE clientes (
 id_cliente INT PRIMARY KEY,
 nome VARCHAR(255),
 email VARCHAR(255)
);

CREATE TABLE pedidos (
 id_pedido INT PRIMARY KEY,
 data_pedido DATE,
 valor_total DECIMAL(10, 2),
 id_cliente INT,
 id_produto INT,
 quantidade INT
);

alter table pedidos
add constraint fk_pedidos_clientes
foreign key (id_cliente) references clientes(id_cliente); #vincula id_cliente das tabelas (pedidos e cliente) 

alter table pedidos
add constraint fk_pedidos_produtos
foreign key (id_produto) references produtos(id_produto);
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
