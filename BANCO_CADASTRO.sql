CREATE DATABASE CADASTRO

GO
USE CADASTRO
GO

CREATE TABLE CLIENTE(
CODIGO INT IDENTITY(1,1) NOT NULL,
NOME VARCHAR(80) NOT NULL,
ENDERECO VARCHAR(100) NULL,
NUMERO INT NULL,
TELEFONE VARCHAR(20) NULL,
EMAIL VARCHAR(80) NULL,
CIDADE VARCHAR(40) NULL,
ESTADO VARCHAR(2) NULL,
CEP VARCHAR(8) NULL,
CONSTRAINT PK_CLIENTE PRIMARY KEY(CODIGO)

)