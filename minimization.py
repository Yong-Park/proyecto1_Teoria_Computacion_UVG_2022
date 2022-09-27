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
    afd_minimizado = {}
    
    #guardar las cadenas segun son terminales o no
    for element in afd:
        if final in element:
            end.append(element)
        else:
            not_end.append(element)
    #estos son los 0-equivalentes
    P0.append(not_end)
    P0.append(end)
    
    #guardar los valores de las transaciones utilizadas
    for element in afd:
        for values in afd[element]:
            if values not in transaction:
                transaction.append(values)
    # print(transaction)
    
    contador = 1
    largo = 0
    while(largo != len(P0)):
        largo = len(P0)
        # print(str(contador) + "-equivalentes")
        #comenzar con la rotacion de equivalentes 
        for x in P0:
            position = 0
            if len(x) > 1:
                equivalents = []
                extra = []
                equivalents.append(x[position])
                for y in x:
                    if x[position] != y:
                        counter = 0
                        for val in transaction:
                            if afd[x[position]][val] == afd[y][val]:
                                counter += 1
                            else:
                                # print("=============")
                                # print(afd[x[position]][val])
                                # print(afd[y][val])
                                # print (x)
                                # print("=============")
                                if str(afd[x[position]][val]) in x and str(afd[y][val]) in x:
                                    counter +=1
                        # print("counter: " + str(counter))
                        if counter == 2:
                            if y not in equivalents:
                                equivalents.append(y)
                        else:
                            if y not in extra:
                                extra.append(y)
                    # print("equivalent: " + str(equivalents))
                    # print("extra: " + str(extra))
                
                if len(equivalents) > 0:
                    P0.append(equivalents)
                if len(extra) > 0:
                    P0.append(extra)
                P0.remove(x)
        contador += 1
        # print(P0)
        
    print("\nTabla afd minimizado")
    print(P0)
            
    #construcion de su tabla
    for x in P0:
        afd_minimizado[x[0]] = {}
        for val in transaction:
            if str(afd[x[0]][val]) in x:
                afd_minimizado[x[0]][val] = x[0]
            else:
                afd_minimizado[x[0]][val] = afd[x[0]][val]
                
    tab = pd.DataFrame(afd_minimizado)
    print(tab.transpose())
    
     #mostrar su grafo
    f = graphviz.Digraph(comment = "afd minimzado")
    names = []
    for i in P0:
        names.append(i[0])
    for name in names:
        if final in (name):
            f.node(str(name),shape="doublecircle")
        else:
            f.node(str(name))
        
    f.node("", shape="plaintext")
    for l in afd_minimizado: #los nodos
        if inicio in l:
            f.edge("",str(l),label="")
        for v in afd_minimizado[l]: #sus variables                
            f.edge(str(l),str(afd_minimizado[l][v]),label = str(v))
        
        
    f.render("afd minimizado", view = True)
        
                                
        
   