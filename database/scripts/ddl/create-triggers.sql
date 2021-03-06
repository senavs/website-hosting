-- ENDERECO
CREATE TRIGGER IF NOT EXISTS TR_ENDERECO_BEFORE_INSERT_VALIDA_DADOS
   BEFORE INSERT ON "ENDERECO"
BEGIN
    SELECT
        CASE
            WHEN NEW.NU_CEP NOT LIKE "________" THEN
                RAISE (ABORT, "NUMERO DE CEP INVALIDO")
        END;
END;

CREATE TRIGGER IF NOT EXISTS TR_ENDERECO_BEFORE_UPDATE_VALIDA_DADOS
   BEFORE UPDATE ON "ENDERECO"
BEGIN
    SELECT
        CASE
            WHEN NEW.NU_CEP NOT LIKE "________" THEN
                RAISE (ABORT, "NUMERO DE CEP INVALIDO")
        END;
END;

-- FUNCIONARIO
CREATE TRIGGER IF NOT EXISTS TR_FUNCIONARIO_BEFORE_INSERT_VALIDA_DADOS
   BEFORE INSERT ON "FUNCIONARIO"
BEGIN
    SELECT
        CASE
            WHEN NEW.NU_CPF NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE CPF INVALIDO")
            WHEN NEW.NU_TELEFONE NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE TELEFONE INVALIDO")
            WHEN NEW.NO_EMAIL NOT LIKE '%_@__%.__%' THEN
                RAISE (ABORT,'EMAIL INVALIDO')
        END;
END;

CREATE TRIGGER IF NOT EXISTS TR_FUNCIONARIO_BEFORE_UPDATE_VALIDA_DADOS
   BEFORE UPDATE ON "FUNCIONARIO"
BEGIN
    SELECT
        CASE
            WHEN NEW.NU_CPF NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE CPF INVALIDO")
            WHEN NEW.NU_TELEFONE NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE TELEFONE INVALIDO")
            WHEN NEW.NO_EMAIL NOT LIKE '%_@__%.__%' THEN
                RAISE (ABORT,'EMAIL INVALIDO')
        END;
END;

-- HOSPEDE
CREATE TRIGGER IF NOT EXISTS TR_HOSPEDE_BEFORE_INSERT_VALIDA_DADOS
   BEFORE INSERT ON "HOSPEDE"
BEGIN
    SELECT
        CASE
            WHEN NEW.NU_CPF NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE CPF INVALIDO")
            WHEN NEW.NU_TELEFONE NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE TELEFONE INVALIDO")
            WHEN NEW.NO_EMAIL NOT LIKE '%_@__%.__%' THEN
                RAISE (ABORT,'EMAIL INVALIDO')
        END;
END;

CREATE TRIGGER IF NOT EXISTS TR_HOSPEDE_BEFORE_UPDATE_VALIDA_DADOS
   BEFORE UPDATE ON "HOSPEDE"
BEGIN
    SELECT
        CASE
            WHEN NEW.NU_CPF NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE CPF INVALIDO")
            WHEN NEW.NU_TELEFONE NOT LIKE "___________" THEN
                RAISE (ABORT, "NUMERO DE TELEFONE INVALIDO")
            WHEN NEW.NO_EMAIL NOT LIKE '%_@__%.__%' THEN
                RAISE (ABORT,'EMAIL INVALIDO')
        END;
END;

-- HOSPEDAGEM
CREATE TRIGGER IF NOT EXISTS TR_HOSPEDAGEM_BEFORE_INSERT_VALIDA_DADOS
   BEFORE INSERT ON "HOSPEDAGEM"
BEGIN
    SELECT
        CASE
            WHEN NEW.DT_ENTRADA NOT LIKE "__/__/____" THEN
                RAISE (ABORT, "DATA DE ENTRADA INVALIDA")
            WHEN NEW.ID_HOSPEDE_TITULAR IN (NEW.ID_HOSPEDE_ACOMPANHANTE_1, NEW.ID_HOSPEDE_ACOMPANHANTE_2, NEW.ID_HOSPEDE_ACOMPANHANTE_3) THEN
                RAISE (ABORT, "PESSOA CADASTRADA MAIS DE UMA VEZ NA MESMA HOSPEDAGEM")
            WHEN NEW.ID_HOSPEDE_ACOMPANHANTE_1 IN (NEW.ID_HOSPEDE_TITULAR, NEW.ID_HOSPEDE_ACOMPANHANTE_2, NEW.ID_HOSPEDE_ACOMPANHANTE_3) THEN
                RAISE (ABORT, "PESSOA CADASTRADA MAIS DE UMA VEZ NA MESMA HOSPEDAGEM")
            WHEN NEW.ID_HOSPEDE_ACOMPANHANTE_2 IN (NEW.ID_HOSPEDE_ACOMPANHANTE_1, NEW.ID_HOSPEDE_TITULAR, NEW.ID_HOSPEDE_ACOMPANHANTE_3) THEN
                RAISE (ABORT, "PESSOA CADASTRADA MAIS DE UMA VEZ NA MESMA HOSPEDAGEM")
            WHEN NEW.ID_HOSPEDE_ACOMPANHANTE_3 IN (NEW.ID_HOSPEDE_ACOMPANHANTE_1, NEW.ID_HOSPEDE_ACOMPANHANTE_2, NEW.ID_HOSPEDE_TITULAR) THEN
                RAISE (ABORT, "PESSOA CADASTRADA MAIS DE UMA VEZ NA MESMA HOSPEDAGEM")
		END;
END;

CREATE TRIGGER IF NOT EXISTS TR_HOSPEDAGEM_AFTER_INSERT_PEENCHE_VALOR_HOSPEDAGEM
   AFTER INSERT ON "HOSPEDAGEM"
BEGIN
    UPDATE "HOSPEDAGEM"
    SET "VL_HOSPEDAGEM" = (
        SELECT SUM(NEW.NU_NOITE * T2.VL_DIARIA)
        FROM QUARTO T1
        LEFT JOIN TIPO_QUARTO T2 ON T1.ID_TIPO_QUARTO = T2.ID_TIPO_QUARTO
        WHERE T1.ID_QUARTO = NEW.ID_QUARTO
    ) WHERE ID_HOSPEDAGEM = NEW.ID_HOSPEDAGEM;
END;