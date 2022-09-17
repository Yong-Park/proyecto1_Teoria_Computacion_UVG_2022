#librerias
from turtle import shape
import pandas as pd
import graphviz
import os

os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'

#variables
vc = "vacio"
lenguaje = []
q = []
q_list = []
afd_table = []
Nuevo = True
eps = "epsilon"
producto = []
afn_table = {} 
#para generar los valores de q0-q99
for i in range(100):
    value = "q"+str(i)
    q.append(value)

def afd_construction(afn, r, start, end):
    #recibiendo el inicio y el de aceptacion
    inicio = start
    final = end
    
    #guardar solo los lenguajes
    for l in r:
        if l != "(" and l !=")" and l !="*" and l !="?" and l !="|": 
            if l not in lenguaje:
                lenguaje.append(l)
    lenguaje.append(eps)
    #guardar los valores de q utilizados
    for l in afn:
        for q_search in q:
            if q_search in l:
                if q_search not in q_list:
                    q_list.append(q_search)

    #transofmrar el afd
    for i in q_list:
        state = i
        afn_table[state] = {}
        for j in lenguaje:
            path = j
            reaching_state = []
            for k in afn:
                if k[0] == state and k[1] == path:
                    reaching_state.append(k[2])
            afn_table[state][path] = reaching_state
                
    #mostrar tabla de e-afn
    print("==================")
    print("\nTabla afn")
    print(afn_table)               
    tab = pd.DataFrame(afn_table)
    print(tab.transpose())
    
    #mostrar su grafo
    f = graphviz.Digraph(comment = "afd")
    inicio_listo = True
    
    names = []
    for i in q_list:
        names.append(i)
    for name in names:
        if name == final:
            f.node(str(name), shape="doublecircle")
        else:
            f.node(str(name))
    f.node("", shape="plaintext")
    for l in afn:
        if inicio in l:
            if(inicio_listo):
                f.edge("",str(l[0]),label = "")
                inicio_listo = False
        f.edge(str(l[0]),str(l[2]),label = str(l[1]))
        
    f.render("afn", view = True)
    
    #convertirlo en su afd por medio de subconjuntos
    all_subconjuntos = []
    subconjuntos = []
    afd = {}
    largo_sub = 0
    
    #iniciar a llenar el primero para el afd
    subconjuntos.append(start)
    while largo_sub != len(subconjuntos):
        for i in subconjuntos:
            if afn_table[i][eps]:
                if afn_table[i][eps] not in subconjuntos:
                    subconjuntos.extend(afn_table[i][eps])
        largo_sub = len(subconjuntos)
    subconjuntos.sort()
    all_subconjuntos.append(subconjuntos)
    #agregarlo como el primer estado
    afd[str(subconjuntos)] = {}
    
    #realizar busqueda de siguietnes elementos
    for elements in all_subconjuntos:
        # print("elementos: " + str(elements))
        for variable in lenguaje:
            subconjuntos = []
            if variable != eps:
                for element in elements:
                    if afn_table[element][variable]:
                        subconjuntos.extend(afn_table[element][variable])
                #realizar el e-clousure
                for l in subconjuntos:
                    if afn_table[l][eps]:
                        if afn_table[l][eps] not in subconjuntos:
                            subconjuntos.extend(afn_table[l][eps])

                subconjuntos = list(dict.fromkeys(subconjuntos))
                subconjuntos.sort()
                if subconjuntos not in all_subconjuntos:
                    all_subconjuntos.append(subconjuntos)
                if str(subconjuntos) not in afd.keys():
                    afd[str(subconjuntos)] = {}
                afd[str(elements)][variable] = subconjuntos
    print("====================")
    print("\nTabla afd")
    print(afd)
    tab = pd.DataFrame(afd)
    print(tab.transpose())
    
    #mostrar su grafo
    f = graphviz.Digraph(comment = "afd")
    names = []
    for i in all_subconjuntos:
        names.append(i)
    for name in names:
        if final in list(name):
            f.node(str(name),shape="doublecircle")
        else:
            f.node(str(name))
        
    f.node("", shape="plaintext")
    for l in afd: #los nodos
        if inicio in l:
            f.edge("",str(l),label="")
        for v in afd[l]: #sus variables                
            f.edge(str(l),str(afd[l][v]),label = str(v))
        
        
    f.render("afd", view = True)


    
