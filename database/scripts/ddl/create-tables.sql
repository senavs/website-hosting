CREATE TABLE IF NOT EXISTS "ENDERECO" (
	"ID_ENDERECO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NU_CEP" CHAR(8) NOT NULL,
	"NO_ENDERECO" VARCHAR(64) NOT NULL,
	"NO_COMPLETO" VARCHAR(32) NOT NULL,
	"NU_NUMERO" INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "FUNCIONARIO" (
	"ID_FUNCIONARIO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NU_CPF" CHAR(11) NOT NULL UNIQUE,
	"NO_FUNCIONARIO" VARCHAR(64) NOT NULL,
	"NU_TELEFONE" CHAR(11) NOT NULL,
	"NO_EMAIL" VARCHAR(32) NOT NULL,
	"ID_ENDERECO" INTEGER NOT NULL,

	FOREIGN KEY ("ID_ENDERECO") REFERENCES "ENDERECO" ("ID_ENDERECO")
);

CREATE TABLE IF NOT EXISTS "HOSPEDE" (
	"ID_HOSPEDE" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NU_CPF" CHAR(11) NOT NULL UNIQUE,
	"NO_HOSPEDE" VARCHAR(64) NOT NULL,
	"NU_TELEFONE" CHAR(11) NOT NULL,
	"NO_EMAIL" VARCHAR(32) NOT NULL,
	"ID_ENDERECO" INTEGER NOT NULL,

	FOREIGN KEY ("ID_ENDERECO") REFERENCES "ENDERECO" ("ID_ENDERECO")
);

CREATE TABLE IF NOT EXISTS "TIPO_QUARTO" (
	"ID_TIPO_QUARTO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NO_TIPO_QUARTO" VARCHAR(16) NOT NULL UNIQUE,
	"VL_DIARIA" REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS "QUARTO" (
	"ID_QUARTO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NU_QUARTO" INTEGER NOT NULL UNIQUE,
	"IN_DISPONIVEL" BOOLEAN NOT NULL, -- BOOLEAN 0/1
	"ID_TIPO_QUARTO" INTEGER NOT NULL,

	FOREIGN KEY ("ID_TIPO_QUARTO") REFERENCES "TIPO_QUARTO" ("ID_TIPO_QUARTO")
);

CREATE TABLE IF NOT EXISTS "TIPO_PAGAMENTO" (
	"ID_TIPO_PAGAMENTO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NO_TIPO_PAGAMENTO" VARCHAR(16) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "HOSPEDES" (
	"ID_HOSPEDES" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"ID_HOSPEDE_TITULAR" INTEGER NOT NULL,
	"ID_HOSPEDE_ACOMPANHANTE_1" INTEGER,
	"ID_HOSPEDE_ACOMPANHANTE_2" INTEGER,
	"ID_HOSPEDE_ACOMPANHANTE_3" INTEGER,
	"ID_HOSPEDE_ACOMPANHANTE_4" INTEGER,

	FOREIGN KEY ("ID_HOSPEDE_TITULAR") REFERENCES "HOSPEDE" ("ID_HOSPEDE"),
	FOREIGN KEY ("ID_HOSPEDE_ACOMPANHANTE_1") REFERENCES "HOSPEDE" ("ID_HOSPEDE"),
	FOREIGN KEY ("ID_HOSPEDE_ACOMPANHANTE_2") REFERENCES "HOSPEDE" ("ID_HOSPEDE"),
	FOREIGN KEY ("ID_HOSPEDE_ACOMPANHANTE_3") REFERENCES "HOSPEDE" ("ID_HOSPEDE"),
	FOREIGN KEY ("ID_HOSPEDE_ACOMPANHANTE_4") REFERENCES "HOSPEDE" ("ID_HOSPEDE")
);

CREATE TABLE IF NOT EXISTS "HOSPEDAGEM" (
	"ID_HOSPEDAGEM" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"ID_FUNCIONARIO" INTEGER NOT NULL,
	"ID_QUARTO" INTEGER NOT NULL,
	"ID_HOSPEDES" INTEGER NOT NULL,
	"ID_TIPO_PAGAMENTO" INTEGER NOT NULL,
	"DT_ENTRADA" CHAR(10) NOT NULL,
	"NU_NOITE" INTEGER NOT NULL,
	"VL_HOSPEDAGEM" REAL,

	FOREIGN KEY ("ID_FUNCIONARIO") REFERENCES "FUNCIONARIO" ("ID_FUNCIONARIO"),
	FOREIGN KEY ("ID_QUARTO") REFERENCES "QUARTO" ("ID_QUARTO"),
	FOREIGN KEY ("ID_HOSPEDES") REFERENCES "HOSPEDES" ("ID_HOSPEDES"),
	FOREIGN KEY ("ID_TIPO_PAGAMENTO") REFERENCES "TIPO_PAGAMENTO" ("ID_TIPO_PAGAMENTO")
);