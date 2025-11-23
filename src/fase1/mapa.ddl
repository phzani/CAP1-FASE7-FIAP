-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-04-22 18:28:38 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE T_APLICACAO_PRODUTO 
    ( 
     id_aplicacao INTEGER  NOT NULL , 
     id_plantacao INTEGER , 
     data_hora    TIMESTAMP , 
     quantidade   NUMBER 
    ) 
;

ALTER TABLE T_APLICACAO_PRODUTO 
    ADD CONSTRAINT T_APLICACAO_PRODUTO_PK PRIMARY KEY ( id_aplicacao ) ;

CREATE TABLE T_CULTURA 
    ( 
     id_cultura   INTEGER  NOT NULL , 
     nome_cultura VARCHAR2 (100) 
    ) 
;

ALTER TABLE T_CULTURA 
    ADD CONSTRAINT T_CULTURA_PK PRIMARY KEY ( id_cultura ) ;

CREATE TABLE T_LEITURA_SENSOR 
    ( 
     id_leitura         INTEGER  NOT NULL , 
     id_sensor_aplicado INTEGER , 
     data_hora          TIMESTAMP , 
     valor              NUMBER 
    ) 
;

ALTER TABLE T_LEITURA_SENSOR 
    ADD CONSTRAINT T_LEITURA_SENSOR_PK PRIMARY KEY ( id_leitura ) ;

CREATE TABLE T_PLANTACAO 
    ( 
     id_plantacao INTEGER  NOT NULL , 
     id_produtor  INTEGER , 
     localizacao  VARCHAR2 (150) 
    ) 
;

ALTER TABLE T_PLANTACAO 
    ADD CONSTRAINT T_PLANTACAO_PK PRIMARY KEY ( id_plantacao ) ;

CREATE TABLE T_PLANTIO 
    ( 
     id_plantio   INTEGER  NOT NULL , 
     id_plantacao INTEGER  NOT NULL , 
     id_cultura   INTEGER  NOT NULL , 
     data_inicio  DATE , 
     data_fim     DATE 
    ) 
;

ALTER TABLE T_PLANTIO 
    ADD CONSTRAINT T_PLANTIO_PK PRIMARY KEY ( id_plantio ) ;

CREATE TABLE T_PRODUTOR 
    ( 
     id_produtor INTEGER  NOT NULL , 
     nome        VARCHAR2 (100) , 
     documento   VARCHAR2 (20) 
    ) 
;

ALTER TABLE T_PRODUTOR 
    ADD CONSTRAINT T_PRODUTOR_PK PRIMARY KEY ( id_produtor ) ;

CREATE TABLE T_SENSOR 
    ( 
     id_sensor   INTEGER  NOT NULL , 
     tipo_sensor VARCHAR2 (50) 
    ) 
;

ALTER TABLE T_SENSOR 
    ADD CONSTRAINT T_SENSOR_PK PRIMARY KEY ( id_sensor ) ;

CREATE TABLE T_SENSOR_APLICADO 
    ( 
     id_sensor_aplicado INTEGER  NOT NULL , 
     id_sensor          INTEGER , 
     id_plantacao       INTEGER 
    ) 
;

ALTER TABLE T_SENSOR_APLICADO 
    ADD CONSTRAINT T_SENSOR_APLICADO_PK PRIMARY KEY ( id_sensor_aplicado ) ;

ALTER TABLE T_APLICACAO_PRODUTO 
    ADD CONSTRAINT T_APLICACAO_PRODUTO_T_PLANTACAO_FK FOREIGN KEY 
    ( 
     id_plantacao
    ) 
    REFERENCES T_PLANTACAO 
    ( 
     id_plantacao
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE T_LEITURA_SENSOR 
    ADD CONSTRAINT T_LEITURA_SENSOR_T_SENSOR_APLICADO_FK FOREIGN KEY 
    ( 
     id_sensor_aplicado
    ) 
    REFERENCES T_SENSOR_APLICADO 
    ( 
     id_sensor_aplicado
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE T_PLANTACAO 
    ADD CONSTRAINT T_PLANTACAO_T_PRODUTOR_FK FOREIGN KEY 
    ( 
     id_produtor
    ) 
    REFERENCES T_PRODUTOR 
    ( 
     id_produtor
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE T_PLANTIO 
    ADD CONSTRAINT T_PLANTIO_T_CULTURA_FK FOREIGN KEY 
    ( 
     id_cultura
    ) 
    REFERENCES T_CULTURA 
    ( 
     id_cultura
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE T_PLANTIO 
    ADD CONSTRAINT T_PLANTIO_T_PLANTACAO_FK FOREIGN KEY 
    ( 
     id_plantacao
    ) 
    REFERENCES T_PLANTACAO 
    ( 
     id_plantacao
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE T_SENSOR_APLICADO 
    ADD CONSTRAINT T_SENSOR_APLICADO_T_PLANTACAO_FK FOREIGN KEY 
    ( 
     id_plantacao
    ) 
    REFERENCES T_PLANTACAO 
    ( 
     id_plantacao
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE T_SENSOR_APLICADO 
    ADD CONSTRAINT T_SENSOR_APLICADO_T_SENSOR_FK FOREIGN KEY 
    ( 
     id_sensor
    ) 
    REFERENCES T_SENSOR 
    ( 
     id_sensor
    ) 
    NOT DEFERRABLE 
;



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             8
-- CREATE INDEX                             0
-- ALTER TABLE                             15
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
