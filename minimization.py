#librerias
import pandas as pd
import graphviz
import os

def minimization(afd, inicio, final):
    P0 = []
    end = []
    not_end = []
    transaction = []
    equivalents = []
    extra = []
    
    #guardar las cadenas segun son terminales o no
    for element in afd:
        if final in element:
            end.append(element)
        else:
            not_end.append(element)
    #estos son los 0-equivalentes
    P0.append(end)
    P0.append(not_end)
    
    #guardar los valores de las transaciones utilizadas
    for element in afd:
        for values in afd[element]:
            if values not in transaction:
                transaction.append(values)
    print(transaction)
    
    #comenzar con la rotacion de equivalentes 
    count = 1
    largo = 0
    while largo != len(P0):
        largo = len(P0)
        print(str(count) + "-equivalente")
        for x in P0:
            if len(x) > 1:
                #revisar
                for y in x:
                    for z in x:
                        if y != z:
                            times = 0
                            for val in transaction:
                                if afd[y][val] == afd[z][val]:
                                    times += 1
                                else:
                                    if afd[y][val] in x and afd[z][val] in x:
                                        times += 1
                                    
                            if times == 2:
                                if y not in equivalents:
                                    equivalents.append(y)
                                if z not in equivalents:
                                    equivalents.append(z)
                break
            equivalents.append(equivalents)
                                
                                
                        
                    
        print(equivalents)
        count +=1               
        
   