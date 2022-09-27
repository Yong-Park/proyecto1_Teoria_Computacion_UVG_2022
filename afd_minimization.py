#librerias
import pandas as pd
import graphviz
import os


def minimizeAfd(afd, subconjuntos, end):
    reachables = delUnreachables(afd)[0]
    new_afd = delUnreachables(afd)[1]
        
    print("reachables")
    print(reachables)
    print("new_afd")
    print(new_afd.transpose())

    #Find Nondistinguishable states


def delUnreachables(afd):
    counter = 0
    bResults = []
    aResults = []
    tab = pd.DataFrame(afd)
    print(tab.transpose())

    dictionary_items = afd.items()
    for item in dictionary_items:
        if counter == 0:
            bResults.append(item[1]['b'])
            aResults.append(item[1]['a'])
            
    Results = [bResults, aResults]
    reachables = []
    print(type(dictionary_items))
    for item in dictionary_items: 
        print("===========================================") 
        if counter == 0:    
            reachables.append(item[0])
        else:
            if item[0] in str(Results[0]):
                reachables.append(item[0])
            else:
                if item[0] in str(Results[1]):
                    reachables.append(item[0])
                else:
                    del tab[item[0]]
        counter = counter + 1

    return reachables, tab


    