
-- MODELO DIMENSIONAL (ESQUEMA ESTRELA)

CREATE TABLE DimCliente (
    idDimCliente INTEGER PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE DimCombustivel (
    idDimCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

CREATE TABLE DimCarro (
    idDimCarro INTEGER PRIMARY KEY,
    kmCarro INTEGER,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INTEGER,
    idDimCombustivel INTEGER,
    FOREIGN KEY (idDimCombustivel) REFERENCES DimCombustivel(idDimCombustivel)
);

CREATE TABLE DimVendedor (
    idDimVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE DimTempo (
    idTempo INTEGER PRIMARY KEY,
    data DATE,
    hora TIME,
    dia INTEGER,
    mes INTEGER,
    ano INTEGER,
    diaSemana VARCHAR(10)
);

CREATE TABLE FatoLocacao (
    idLocacao INTEGER PRIMARY KEY,
    idDimCliente INTEGER,
    idDimCarro INTEGER,
    idDimVendedor INTEGER,
    idTempoLocacao INTEGER,
    idTempoEntrega INTEGER,
    qtdDiaria INTEGER,
    vlrDiaria DECIMAL(18, 2),
    FOREIGN KEY (idDimCliente) REFERENCES DimCliente(idDimCliente),
    FOREIGN KEY (idDimCarro) REFERENCES DimCarro(idDimCarro),
    FOREIGN KEY (idDimVendedor) REFERENCES DimVendedor(idDimVendedor),
    FOREIGN KEY (idTempoLocacao) REFERENCES DimTempo(idTempo),
    FOREIGN KEY (idTempoEntrega) REFERENCES DimTempo(idTempo)
);
