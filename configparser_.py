# -*- coding: utf-8 -*- 
""" Created on Fri Feb  3 11:35:40 2023 @author: DELL """

##########################################################

## CONEXION CON LA BASE DE DATOS MYSQL ##

# Importamos la libreria de mysql mysql.connector que nos ayudara a establecer la conexion
import mysql.connector

# Importamos ConfigParser de la libreria configparser para lograr leer el archivo de configuracion 
from configparser import ConfigParser

# guardamos la direccion del archivo de configuracion en una variable
file = '/DataAnalyst/config.ini'
# guardamos la funcion ConfigParser() en una variable
config = ConfigParser()
# con la funcion .read() leemos el archivo de configuracion
config.read(file)


"""
# config.section() nos muestra las instancias dentro de nuestro archivo.ini
print(config.sections())
# config['instance'] nos muestra el nombre de la instancia que queramos
print(config['sql_join_holamundo'])
# list(config['instance']) nos muestra las variables de la instancia que solicitemos
print(list(config['sql_join_holamundo']))
# config['instance']['variable'] nos muestra el valor de la variable en la instancia que solicitemos
print(config['sql_join_holamundo']['server_'])
# config.get('instance', 'variable') nos muestra el valor de la variable en la instancia que solicitemos
print(config.get('sql_join_holamundo', 'user_'))
# config.items('intance') nos muestra una lista con las variables y correspondientes valores
print(config.items('sql_join_holamundo'))
"""
# con mysql.connector.conect() establecemos la conexion a la base de datos que expecifiquemos
conexion = mysql.connector.connect(
  user = config.get('sql_join_holamundo', 'user_'), 
  password = config.get('sql_join_holamundo', 'pwd_'), 
  host = config.get('sql_join_holamundo', 'server_'), 
  database = config.get('sql_join_holamundo', 'db_'),
  port = config.get('sql_join_holamundo', 'port_'),
  )

# con .cursor() establecemos un cursor que nos sirve para navegar en la base de datos (cursor_ctext.CMySQLCursor)
# Con dictionary=True los valores del cursor son devueltos en un diccionario
miCursor = conexion.cursor(dictionary=True)

# .execute nos permite ejecutar solicitudes de sql directas a la base de datos
miCursor.execute("SHOW DATABASES")

# .fetchall() nos muestra los resultados de una solicitud a la base de datos (lista de tuplas) 
databases_mysql = miCursor.fetchall()

miCursor.execute("SELECT * FROM bank")
bank = miCursor.fetchall()

# .close() cierra la conexion de la base de datos
conexion.close()


##########################################################
