#!/usr/bin/python3 

import sys 

"""
Se devuelve la tupla <persona, gasto, freq> indicando para cada persona cuál 
es el gasto más frecuente (la moda) y el número de veces que aparece (freq).
"""

subproblema = None
suma_conteos = 0
freq = 0
result = None


for claveValor in sys.stdin:                               
    persona_gasto, contador = claveValor.split("\t", 1)   #Se reciben los pares <persona-gasto, 1> emitidos por el 'Mapper' en las variables 'persona_gasto' y 'contador', respectivamente.
    persona, gasto= persona_gasto.split("-", 1)           
    contador=int(contador)                                #Se convierte la variable 'contador' -tipo string- a entero para poder operar con el.        

#Se divide en subproblemas. Cada subproblema será una persona con su gasto modal. 
    if subproblema == None:                               #Cuando se inicia el 'Reducer' se cumple este 'if'.
        subproblema = [persona,gasto]                     #El primer subproblema es el primer par <persona, gasto>.


    if subproblema == [persona,gasto]:                    #Se ejecuta el 'if' si el par <persona, gasto> es del subrpoblema actual.               
        suma_conteos = suma_conteos + contador            #'Suma_conteos' almacena el número veces que aparece el mismo par <persona, gasto>.


    else:                                                 #Se ejecuta el 'else' si cambia el par <persona, gasto>.
        if subproblema[0] == persona:                     #Los datos entran en el 'Reducer' ordenados por persona. Por lo tanto, para una misma persona se halla el máximo valor de la variable 'suma_conteos'.
            if suma_conteos > freq:
                freq = suma_conteos                       #Y ese máximo valor es la frecuencia del gasto modal buscado.
                result = subproblema                      #Se guarda en la variable auxiliar 'result' el par <persona, gasto> correspondiente.
                
        else:                                             #Cuando cambiamos a la siguiente persona se ejecuta el 'else'.
            print (("%s\t%s\t%s") % (result[0], result[1], freq))       #Imprimimos la tupla <persona, gasto, freq> guardada en el 'if' anterior.
            freq = 0                                                    #Actualizamos la freq para repetir el proceso con la siguiente persona.
        
        #Pasamos al siguiente subproblema.
        subproblema = [persona,gasto]                                   
        suma_conteos = contador

#El anterior bucle no emite el último subproblema.      
print (("%s\t%s\t%s") % (result[0], result[1], freq))