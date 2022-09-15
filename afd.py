#librerias
from queue import Empty
import pandas as pd

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
    

def afd(afn, r, start):
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
    print("Tabla afn")
    print(afn_table)               
    tab = pd.DataFrame(afn_table)
    print(tab.transpose())
    
    #comenzando a convertirlo en afd
    new_states_list = []    
    all_states_list = []                      
    dfa = {}                                      
    keys_list = list(afn_table.keys())[0]
    path_list = list(afn_table[keys_list].keys())  
    
    dfa[keys_list] = {}
    #para la primera fila
    for x in path_list:
        if afn_table[keys_list][eps] is not Empty:
            if x is not eps:
                if not afn_table[keys_list][x]:
                    llave = []
                    llave.extend(afn_table[keys_list][eps])
                    dfa[keys_list][x] = afn_table[keys_list][eps]
                    if dfa[keys_list][x] not in new_states_list and dfa[keys_list][x] not in all_states_list:
                        new_states_list.append(dfa[keys_list][x])
                        all_states_list.append(dfa[keys_list][x])
        else:
            if x is not eps:
                if len(x) > 1:
                    dfa[keys_list][x] = afn_table[keys_list][x]
                else:
                    llave = []
                    llave.extend(afn[keys_list][x])
                    for bucle in range(len(q_list)):
                        for letra in llave:
                            if afn[letra][eps]:
                                if afn[letra][eps] not in llave:
                                    llave.extend(afn[letra][eps])
                    dfa[keys_list][x] = llave
                    if dfa[keys_list][x] not in new_states_list and dfa[keys_list][x] not in all_states_list:
                        new_states_list.append(dfa[keys_list][x])
                        all_states_list.append(dfa[keys_list][x])
        
            
    #generar el resta de filas
    q_list.pop(0)
    while len(new_states_list) != 0:
        # print("states:" + str(new_states_list[0]))
        # print(len(new_states_list[0]))
        dfa[str(new_states_list[0])] = {}
        for _ in range(len(new_states_list[0])):
            # print(new_states_list[0])
            # print(len(new_states_list[0]))
            if len(new_states_list[0]) > 1:
                for i in path_list:
                    if i is not eps:
                        temp = []
                        #print("columna:" + str(i))
                        for j in range(len(new_states_list[0])):
                            temp += afn_table[new_states_list[0][j]][i]
                            #print("new cadena:" + str(temp))
                        dfa[str(new_states_list[0])][i] = temp
                        if temp not in new_states_list and temp not in all_states_list:
                            new_states_list.append(temp)
                            all_states_list.append(temp)
            else:
                #print("states:" + str(new_states_list[0]))
                # print("================")
                # print(afn_table[str(new_states_list[0][0])])
                for i in path_list:
                    if afn_table[str(new_states_list[0][0])][eps]:
                        if i is not eps:
                            if not afn_table[str(new_states_list[0][0])][i]:
                                temp = []
                                temp.extend(afn_table[str(new_states_list[0][0])][eps])
                                #revisar si este tiene otros
                                largo = 0
                                while(largo != len(temp)):
                                    for y in temp:
                                        if afn_table[y][eps]:
                                            temp.extend(afn_table[y][eps])
                                    largo = len(temp)
                                
                                dfa[str(new_states_list[0])][i] = temp
                                if temp not in new_states_list and temp not in all_states_list:
                                    new_states_list.append(temp)
                                    all_states_list.append(temp)
                                    
                            else:
                                temp = []
                                temp.extend(afn_table[str(new_states_list[0][0])][i])
                                largo = 0
                                while(largo != len(temp)):
                                    for y in temp:
                                        if afn_table[y][eps]:
                                            temp.extend(afn_table[y][eps])
                                    largo = len(temp)
                                
                                dfa[str(new_states_list[0])][i] = temp
                                if temp not in new_states_list and temp not in all_states_list:
                                    new_states_list.append(temp)
                                    all_states_list.append(temp)

                    else:
                        if i is not eps:
                            temp = []
                            temp.extend(afn_table[str(new_states_list[0][0])][i])
                            largo = 0
                            while(largo != len(temp)):
                                for y in temp:
                                    if afn_table[y][eps]:
                                        temp.extend(afn_table[y][eps])
                                largo = len(temp)
                                                                
                            dfa[str(new_states_list[0])][i] = temp
                            if temp not in new_states_list and temp not in all_states_list:
                                    new_states_list.append(temp)
                                    all_states_list.append(temp)

        # print("state:" + str(new_states_list))
        lista = []
        if len(q_list) > 0:
            lista.append(q_list[0])
            # print("lista:" + str(lista))
            new_states_list.append(lista)
            q_list.pop(0)
        new_states_list.remove(new_states_list[0])
           
    print("\nTabla afd")
    print(dfa)
    tab = pd.DataFrame(dfa)
    print(tab.transpose())