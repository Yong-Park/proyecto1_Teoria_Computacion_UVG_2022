import pandas as pd

vc = "vacio"
lenguaje = []
q = []
q_list = []
afd_table = []
Nuevo = True
eps = "epsilon"
producto = []
afn_table = {} 

for i in range(100):
    value = "q"+str(i)
    q.append(value)
    

def afd(afn, r, start):
    for l in r:
        if l != "(" and l !=")" and l !="*" and l !="?" and l !="|": 
            if l not in lenguaje:
                lenguaje.append(l)
    lenguaje.append(eps)
    
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
    tab = pd.DataFrame(afn_table)
    print(tab.transpose())

    return 1