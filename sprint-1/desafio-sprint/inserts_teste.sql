-- Inserções para tabela Cliente
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
VALUES 
(1, 'João Silva', 'Curitiba', 'Paraná', 'Brasil'),
(2, 'Maria Oliveira', 'São Paulo', 'São Paulo', 'Brasil'),
(3, 'Carlos Souza', 'Belo Horizonte', 'Minas Gerais', 'Brasil');

-- Inserções para tabela Combustivel
INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
VALUES 
(1, 'Gasolina'),
(2, 'Etanol'),
(3, 'Diesel');

-- Inserções para tabela Carro
INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
VALUES 
(1, 30000, 'Sedan', 'Toyota', 'Corolla', 2020, 1),
(2, 15000, 'Hatch', 'Hyundai', 'HB20', 2022, 2),
(3, 50000, 'SUV', 'Ford', 'EcoSport', 2019, 3);

-- Inserções para tabela Vendedor
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
VALUES 
(1, 'Ana', 2, 'Paraná'),
(2, 'Lucas', 1, 'São Paulo'),
(3, 'Juliana', 2, 'Minas Gerais');

-- Inserções para tabela Locacao
INSERT INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
VALUES 
(1, 1, 1, 1, '2023-01-10', '10:00:00', 5, 150.00, '2023-01-15', '10:00:00'),
(2, 2, 2, 2, '2023-02-05', '09:00:00', 3, 120.00, '2023-02-08', '09:00:00'),
(3, 3, 3, 3, '2023-03-12', '14:30:00', 7, 200.00, '2023-03-19', '14:30:00');
