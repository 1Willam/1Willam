# Código con consultas y parámetros escrito para reutilizar #

-- Se utiliza delimitadores para delimitar el funcionamiento de cada bloque

-- Procedimiento : llamar a los registros de la tabla user que contenga en su columna un nombre con la letra que se ingrese
delimiter //
CREATE PROCEDURE usuarios_con_letra(in letra char) #Nombre del procedimiento, tipo de dato de entrada
begin
	select * from user where name like concat('%',letra,'%');
end // #terminamos la instrucción
delimiter ;

-- llamar procedimientos
CALL usuarios_con_letra('l');

-- borrar procedimientos
drop procedure usuarios_con_letra;

-- Segundo procedimiento 
delimiter //
create procedure usuarios_con_letra(in letra char(1),out numero int)
begin
select count(*) into numero from user where name like concat('%',letra,'%');
end//
delimiter ;

call usuarios_con_letra('j',@cantidad_j); # se una @ cuando su nombre contiene caracteres alfanuméricos
call usuarios_con_letra('u',@cantidad_u);
call usuarios_con_letra('a',@cantidad_a);
call usuarios_con_letra('n',@cantidad_n);
select @cantidad_j as usuarios_con_j, @cantidad_u, @cantidad_a, @cantidad_n;