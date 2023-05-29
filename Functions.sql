# es una rutina creada para procesar parámetros y retornar una salida #

# Sintaxis #
/*     
delimiter //
CREATE FUNCTION nombre_funcion (variable tipo) returns tipo
begin
	-- INICIO DE ACCIONES 
    declare numero int;
    select count(*) into numero from tabla;
    return numero;
    -- FIN ACCIONES
end//
delimiter ;
*/ 

# Creating functions 1 #
delimiter //
create function numero_letras (letra char) returns int
READS SQL DATA DETERMINISTIC
begin
	declare numero int;
    select count(*) into numero from user where name like concat('%',letra,'%');
    return numero;
end //
delimiter ;

-- Llamada a la función
SELECT numero_letras('l');
SELECT LEFT(name,1) as letra, numero_letras(left(name,1)) as numero_nombres_con_lretra from user;

# Creating functions 2 #
DELIMITER //
CREATE FUNCTION altura_precio (vprecio_venta INT) RETURNS varchar(20)
READS SQL DATA DETERMINISTIC
	BEGIN
		CASE 
			WHEN vprecio_venta < 20 THEN
				RETURN 'Bajo';
			WHEN vprecio_venta >= 20 THEN
				RETURN 'Alto';
		END CASE;
	END //
    DELIMITER ;

-- Llamamos a la función
SELECT name, altura_precio(edad) FROM user;

