# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:09:26 2023

@author: DELL
"""

import mysql.connector
from configparser import ConfigParser

file = "/DataAnalyst/config.ini"
config = ConfigParser()
config.read(file)
## Base de datos: holamundo ##
conexion = mysql.connector.connect(
    user=config.get("sql_join_holamundo", "user_"),
    password=config.get("sql_join_holamundo", "pwd_"),
    host=config.get("sql_join_holamundo", "server_"),
    database=config.get("sql_join_holamundo", "db_"),
    port=config.get("sql_join_holamundo", "port_"),
)

miCursor = conexion.cursor(dictionary=True)
miCursor.execute("SELECT * FROM goodyear")

## Nombre de variable de la tabla de base de datos ##
goodyear = miCursor.fetchall()

conexion.close()
del file, config, conexion, miCursor