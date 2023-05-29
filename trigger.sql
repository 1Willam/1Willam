# Función de MySQL que se ejecuta cuando se dan ciertas condiciones
-- usos --
-- Creación de registros (logs) de acciones
-- Actalizaciones de fechas en casos de algunas modificaciones
-- Creaciones de relaciones en caso de tener alguna restricción a esa función para nuestro usuario

# sintaxis #
/*

delimiter //
create trigger nombre_gatillo momento evento on tabla_que_recibe_evento
for each row --Para que se realice en cada registro que se esté utilizando 
begin
	insert into cualquier_tabla(campo) value ('valor');
end //
delimiter ;

*/

-- Creación de tabla para ejemplo
CREATE TABLE `acciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `accion` VARCHAR(60) NULL,
  `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP, # CURRENT_TIMESTAMP es un valor por defecto (fecha actual del día)
  PRIMARY KEY (`id`));
  
-- Creación de trigger en tabla user 
DELIMITER //
Create trigger log_tabla_user after insert on user
for each row begin
	insert into acciones (accion) value (concat('Se creo un registro en user de nombre',NEW.name, ' y id:', NEW.id ));
end //
DELIMITER ;