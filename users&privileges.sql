-- Mostrar los usuarios y privilegios --
-- Se debe tener todos los permisos y privilegios para poder administrar usuarios
select * from mysql.user;

-- Crear usuarios y concederles permisos de conexión
grant usage on holamundo.animales to gestor identified by '123456';
grant usage on *.* to gestor@localhost identified by '123456';
grant usage on *.* to gestor@192.168.1.150 identified by '123456';
grant select, delete, update on *.* to gestor;
grant all privileges on *.* to gestor;

-- Eliminar usuarios y sus permisos
drop user gestor@192.168.1.150;
drop user gestor@localhost;

-- Ver los permisos que tiene el usuario
show grants;
