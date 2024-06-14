-- Tabela territorialidades
CREATE TABLE territorialidades (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL
);

-- Tabela estudos
CREATE TABLE estudos (
    id SERIAL PRIMARY KEY,
    territorialidade_id INT NOT NULL,
    media_anos_estudo FLOAT NOT NULL,
    fundamental_completo_18_mais FLOAT NOT NULL,
    fundamental_completo_25_mais FLOAT NOT NULL,
    medio_completo_18_20 FLOAT NOT NULL,
    medio_completo_25_mais FLOAT NOT NULL,
    superior_completo_25_mais FLOAT NOT NULL,
    ano INT NOT NULL,
    FOREIGN KEY (territorialidade_id) REFERENCES territorialidades(id)
);

-- Tabela renda
CREATE TABLE renda (
    id SERIAL PRIMARY KEY,
    territorialidade_id INT NOT NULL,
    renda_per_capita FLOAT NOT NULL,
    ano INT NOT NULL,
    FOREIGN KEY (territorialidade_id) REFERENCES territorialidades(id)
);
