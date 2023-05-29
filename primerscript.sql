# Crear base de datos o schema #
create database holamundo;

# Se puede crear bases de datos con caracteres especiales #
-- create database holamundo character set utf8mb4 collate utf8mb4_spanish_ci;

# Mostrar las bases de datos existentes #
show databases;
# Seleciconar una base de datos para trabajar sobre ella #
use holamundo;

# Crear un tabla de datos #
CREATE TABLE animales(
	id int,
    tipo varchar(255),
    estado varchar(255) default 'feliz',
    -- Seleccionar una llave primaria
    PRIMARY KEY (id)
);
-- insert into animales (tipo, estado) values ('chanchito','feliz');

# Alterar una tabla de datos #
alter table animales modify column id int auto_increment;

# Mostrar el código de creación de la tabla creada #
show create table animales;
CREATE TABLE `animales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

# Insertar registros en una tabla #
insert into animales (tipo, estado) values ('chanchito','feliz');
insert into animales (tipo, estado) values ('dragon','feliz');
insert into animales (tipo, estado) values ('felipe','triste');

# Seleccionar y mostrar los registros de una tabla #
select * from animales;
# Seleccionar y mostrar el registro que cumplan con algunas condiciones #
select * from animales where id=1;
select * from animales where estado='feliz' and tipo= 'felipe';

# Modificar un registro de una tabla #
update animales set estado='feliz' where id=3;

# Eliminar un registro de una tabla de datos #
delete from animales where estado='feliz';
-- Error Code: 1175. You are using safe update mode and you tried to update a 
-- table without a WHERE that uses a KEY column.  
-- To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.

delete from animales where id=3;
update animales set estado='triste' where tipo='dragon';
-- esto también arroja error 1175


-- -------------- --
