#!/usr/bin/python3 

import sys 

"""
Por cada línea se emiten los pares <persona-gasto, 1>, 
donde el valor 1 actuará como contador en el 'Reducer'.
"""

for linea in sys.stdin:                            #Se leen los datos de entrada mediante la forma estándar 'stdin'. 
    linea = linea.strip()                                  
    persona, gasto =  linea.split("\t", 1)         #Se divide cada línea en persona y gasto tomando como separador \t.
    print ("%s-%s\t%d " %  (persona, gasto, 1))    #Se genera una tupla <persona-gasto, 1>.