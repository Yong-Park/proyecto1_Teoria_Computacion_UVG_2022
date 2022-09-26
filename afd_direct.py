#librerias
from turtle import position, shape
import pandas as pd
import graphviz
import os

# os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

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

def afd_directo(afn, postfix):
    start = primeraPos(postfix) #Arreglo primera posicion
    final = ultimaPos(postfix) #Arreglo posicion fina
    
    #mostrar su grafo
    f = graphviz.Digraph(comment = "afd")
    inicio_listo = True
    
    
    used_nodes = set()
    indice = -1

    nodoInicial = "Inicio"
    f.node(nodoInicial)
    primerNodo = start[len(start) - 1]
    f.node(str(crearetiquetadeNodo(primerNodo)))
    used_nodes.add(str(crearetiquetadeNodo(primerNodo)))
    indice += 1

    # f.edge(nodoInicial)
    
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
        if start in l:
            if(inicio_listo):
                f.edge("",str(l[0]),label = "")
                inicio_listo = False
        f.edge(str(l[0]),str(l[1]),label = str(l[1]))
        
    f.render("afd direct", view = True)

def primeraPos(cadena):
    indice = 0
    letra_no = 1
    nullable = []
    arregloPrimeraPos = []
    for caracter in cadena:
        if caracter.isalpha():
            nuevapos = [letra_no]
            letra_no += 1
            indice += 1
            arregloPrimeraPos.append(nuevapos)
        
        elif caracter == "|":
            nuevapos = arregloPrimeraPos[indice - 2].copy() + arregloPrimeraPos[indice - 1].copy()
            arregloPrimeraPos.append(nuevapos)
            indice += 1

        elif caracter == "*":
            nuevapos = arregloPrimeraPos[indice - 1].copy()
            arregloPrimeraPos.append(nuevapos)
            indice += 1
        
        elif caracter == "?":
            nuevapos = arregloPrimeraPos[indice - 2].copy()
            arregloPrimeraPos.append(nuevapos)
            indice += 1
    
    return arregloPrimeraPos




def ultimaPos(cadena):
    indice = 0
    letra_no = 1
    nullable = []
    arregloUltimaPos = []
    for caracter in cadena:
        if caracter.isalpha():
            nuevapos = [letra_no]
            letra_no += 1
            indice += 1
            arregloUltimaPos.append(nuevapos)
        
        elif caracter == "|":
            nuevapos = arregloUltimaPos[indice - 2].copy() + arregloUltimaPos[indice - 1].copy()
            arregloUltimaPos.append(nuevapos)
            indice += 1

        elif caracter == "*":
            nuevapos = arregloUltimaPos[indice - 1].copy()
            arregloUltimaPos.append(nuevapos)
            indice += 1
        
        elif caracter == "?":
            nuevapos = arregloUltimaPos[indice - 1].copy()
            arregloUltimaPos.append(nuevapos)
            indice += 1
    return arregloUltimaPos

def crearetiquetadeNodo(node):
    label = 0
    for pos in node:
        label = label * 10 + pos
    
    return label