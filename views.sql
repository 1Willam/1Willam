# Son consultas que se representan como una tabla virtual a partir de un conjunto de tablas en una base de datos relacional #

# Sintaxis #
/*

create view nombre_vista as
select campo1, campo2
from tabla
where campo ='valor';

*/

-- Creando vista
-- Se debe crear un nombre diferente a una tabla ya creada
create view vista_alumnos_sin_salon as
select * from user where edad >= 20;