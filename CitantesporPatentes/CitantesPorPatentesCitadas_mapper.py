#!/usr/bin/python3 

import sys

"""
Por cada línea se emiten los pares <cited, citing>.
"""

next(sys.stdin)                              #Se salta la primera línea que contiene la cabecera con la descripción de las columnas. 
for linea in sys.stdin:
    linea = linea.strip()
    citing, cited = linea.split("," , 1)     #Se divide cada línea en citante (citing) y citada (cited) tomando como separador ','.
    print ("%s\t%s" % (cited, citing))       #Se genera el par <cited, citing>.

"""
NOTA: Observese que el 'Mapper' emite los datos invirtiendo
el orden de las columnas del archivo de entrada.  
De este modo, el 'Reducer' recibe como clave intermedia la patente citada 
y como valor intermedio la patente que la cita.
"""
