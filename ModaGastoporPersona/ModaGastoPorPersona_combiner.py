#!/usr/bin/python3 

import sys 


subproblema = None
suma_conteos = 0

"""
Se reciben los pares <persona-gasto, 1> emitidos en el 'Mapper' 
y se devuelven las tuplas <persona-gasto, suma_conteos>, donde
'suma_conteos' almacena la frecuencia de cada par <persona, gasto>.
"""

for claveValor in sys.stdin:
    persona_gasto, contador = claveValor.split("\t", 1)  
    persona, gasto= persona_gasto.split("-", 1)
    contador=int(contador)

    if subproblema == None:
        subproblema = [persona,gasto]


    if subproblema == [persona,gasto]:
        suma_conteos = suma_conteos + contador


    else:
        print (("%s-%s\t%s") % (subproblema[0], subproblema[1], suma_conteos))

        subproblema = [persona,gasto]
        suma_conteos = contador

print (("%s-%s\t%s") % (subproblema[0], subproblema[1], suma_conteos))
