#!/usr/bin/python3 

import sys

"""
Para cada patente citada se recibe como valor una lista de las que la citan,
ordena esa lista numéricamente y la convierte en un string de números separados por coma.
El formato de salida se corresponde con:
PatenteCitada1 PatenteCitante1.1, PatenteCitante1.2, ...
PatenteCitada2 PatenteCitante2.1, PatenteCitante2.2, PatenteCitante2.3, ...
PatenteCitada3 PatenteCitante3.1, PatenteCitante3.2, PatenteCitante3.3, ...
PatenteCitada4 PatenteCitante4.1, ...
 .
 .
 .
Donde la separación entre la clave y los valores debe ser un tabulado.
"""

subproceso = None
citing_list = []


for linea in sys.stdin:
    cited, citing = linea.split("\t" , 1)  #Se reciben los pares <cited, citing> emitidos por el 'Mapper'.

#Se divide en subprocesos. Cada subproceso será una patente citada con sus citantes. 
    if subproceso == None:                   #Cuando se inicia el 'Reducer' se cumple este 'if'.
        subproceso = cited                   #El primer subproceso es la primera patente citada.

    if subproceso == cited:                  #Se ejecuta el 'if' si la patente citada es el subproceso actual.  
        citing_list.append(citing[:-1])      #Cada vez que se ejecute este 'if', es decir que nos encontremos en la misma patente citada, 
                                             #se añadirá el número de la patente citante que corresponde a la lista.
                                             #Con 'citing[:-1]' se añade el valor de 'citing' evitando el salto de línea (\n).
    
    else:                                    #Se ejecuta el 'else' si cambia de patente citada.
        print ("%s\t" % (subproceso)+(','.join(map(str, citing_list))))      #Imprimimos la lista completada en el 'if' anterior
        
        #Pasamos al siguiente subproceso.
        citing_list = [citing[:-1]]
        subproceso = cited

#El anterior bucle no emite el último subproceso.    
print ("%s\t" % (subproceso)+(','.join(map(str, citing_list))))
