use holamundo;

create table products (
	id int not null auto_increment, 
    name varchar (50) not null,
    created_by int not null,
    marca varchar(50) not null,
    primary key (id),
    foreign key (created_by) references user (id)
);

-- Cambiar nombre a una tabla existente --
rename table products to product;

-- Forma alternativa de ingresar registros en una tabla --
insert into product (name, created_by, marca)
values
	('ipad', 1, 'apple'),
    ('iphone', 1, 'apple'),
    ('watch', 2, 'apple'),
    ('macbook', 1, 'apple'),
    ('imac', 3, 'apple'),
    ('ipad mini', 2,'apple');
select * from product;

-- Seleccionar sin repetición los campos especificados de una tabla --
select distinct created_by from product;

-- Agregar un índice fulltext a la tabla creada --
alter table product add fulltext(name);

-- Seleccionar todos los registros de una tabla que contengan 'mini', es necesario una índice fulltext para ello
select * from holamundo.product where match(name) against('mini');

/* Selecciona y muestra todos los registros de la tabla user (left) e insertar los datos de la tabla product (right) que
coincidan con las condiciones especificadas se necesita una llave foránea para ello*/
select u.id, u.email, p.name 
from user u left join product p on u.id = p.created_by;

/* Selecciona y muestra todos los registros de la tabla user (right) e insertar los datos de la tabla product (left) que
coincidan con las condiciones especificadas se necesita una llave foránea para ello*/
select p.name, u.id, u.email from user u right join product p on u.id = p.created_by;
	
/* Realiza un cruce de tablas de acuerdo a las especificaiones y muestra las columnas y registros requeridos se necesita 
una llave
foránea para ello */
select u.id, u.email, p.name 
from user u inner join product p on u.id = p.created_by;

/* Realiza un cruce de una registro de una tabla con todos los registros de la otra tabla hasta completarse todos los 
registros y los muestra según las columnas específicadas */
select u.id, u.name, p.id, p.name from user u cross join product p;

/* Agrupa en un contador (id) la cantidad de registros que se encuentran según la columna 'marca' y los muestra en las 
columnas especificadas  */
select count(id), marca from product group by marca;

select * from product order by created_by;

/* Realiza un left join y de esa unión agrupa en un contador (id) la cantidad de registros que se encuentran según la 
columna 'p.created_by' y los muestra en las columnas especificadas */
select count(p.id), u.name from product p left join user u on u.id = p.created_by group by p.created_by;

/* Realiza un left join y de esa unión agrupa en un contador (id) la cantidad de registros que se encuentran según la 
columna 'p.created_by' y muestra los registros obtenidos en donde únicamente existan 'p.id' mayores o iguales a 2 en 
las columnas especificadas*/
select count(p.id), u.name from product p left join user u on u.id = p.created_by group by p.created_by
having count(p.id) >= 2;

/* Función CONCAT: Selecciona y muestra uniones de valores de diferentes columnas de una tabla en una columna especificada 
(con espacios manuales) */
select id, CONCAT(name, ' ', marca) AS productos, created_by from product where 1;

/* Función CONCAT_SW: Selecciona y muestra uniones de valores de diferentes columnas de una tabla en una columna especificada 
(con espacios automáticos) */
select id, CONCAT_WS(' ', name, marca, created_by) AS productos from product where 1;

/* Función LENGHT: nos muestra en una columna especificada, la longitud de una cadena de caracteres de una columna deseada */
select id, CONCAT_WS(' ', name, marca, created_by) AS productos, LENGTH(name) as longitud from product where 1;

/* Función LOWER(): Selecciona y muestra mayúsculas --> minúsculas */
select id, LOWER(CONCAT_WS(' ', name, marca, created_by)) AS productos from product where 1;

/* Función LOWER(): Selecciona y muestra minúsculas --> mayúsculas */
select id, UPPER(CONCAT_WS(' ', name, marca, created_by)) AS productos from product where 1;

/* Función REPLACE(columna, 'campo actual', 'campo modificado'): Selecciona y muestra una columna a modificar de un 
'campo actual' a un 'campo modificado' (No altera la tabla)*/
select id, replace(marca, 'apple', 'N0K1a') as 'marca modificada', UPPER(CONCAT_WS(' ', name, marca, created_by)) AS productos from product where 1;

/* Función TRIM(): Selecciona y muestra la eliminación de los espacios que se pudierar haber generado antes y 
después de registrar un campo */
select TRIM(name) from product where 1;

-- Cambiar formato de fecha
-- select DATE_FORMAT(fecha_nacimiento, "%d/%m/%Y") from `contactos` where 1
-- select DATE_FORMAT(fecha_nacimiento, "%d/%m/%y") from `contactos` where 1

-- Para solo seleccionar día, mes o año
-- select DAY(fecha_nacimiento) from `contactos` where 1
-- select MONTH(fecha_nacimiento) from `contactos` where 1
-- select YEAR(fecha_nacimiento) from `contactos` where 1


select * from product;

-- Eliminar tablas de una base de datos seleccionada --
drop table product;
drop table animales;
drop table user;

CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `id` INT NOT NULL,
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE);
