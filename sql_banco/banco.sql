CREATE DATABASE cotacoes;
USE cotacoes;

CREATE TABLE cotacoes_dolar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    valor DECIMAL(10, 4) NOT NULL,
    fonte VARCHAR(255) NOT NULL
);
