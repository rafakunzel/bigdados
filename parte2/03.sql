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
