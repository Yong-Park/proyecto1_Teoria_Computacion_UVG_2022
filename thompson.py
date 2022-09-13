#en este se enfoca en convertir el lenguaje r recibido en AFN mediante thompson

#variabels
from operator import contains
from queue import Empty

q = []
lista_lenguaje = []
abierto = False
afn = []
eps = "epsilon"

#para generar todos los posibles q0,q1,q2,...,q99
for i in range(100):
    value = "q"+str(i)
    q.append(value)

#en este se enfocara para ver cuales son los que se deben de trabajar primero, por ejemplo los que estan primero dentro de parentesis
def lenguaje_regular(r):
    cadena = []
    print(r)
    for l in r:
        if l == "(":
            abierto=True
            if len(cadena) != 0:
                lista_lenguaje.append(cadena)
                cadena=[]
        elif l == ")":
            abierto=False
            lista_lenguaje.append(cadena)
            cadena=[]
        else:
            if abierto == True:
                cadena.append(l)
            else:
                lista_lenguaje.append(l)
    print(lista_lenguaje)
    
    #comenza la construccion del afn
    counter = 0
    for c in lista_lenguaje:
        if len(c) > 1 and len(c) < 4:
            if "|" in c:
                cadena_recivida = union(c)
                lista_lenguaje[counter] = cadena_recivida
                afn.append(cadena_recivida)

        elif c == "*":
            cadena_recivida = kleene(lista_lenguaje[counter-1])
            lista_lenguaje[counter] = cadena_recivida
            afn.append(cadena_recivida)
        counter += 1
        
    #limitar las cosas
    counter = 0
    for c in lista_lenguaje:
        if len(c) >= 4:
            lista_lenguaje.pop(counter)
        counter += 1
    
    #realizar la concatenacion
    counter = 0
    for c in lista_lenguaje:
        if (counter-1)>= 0 and counter <len(lista_lenguaje)-2:
            cadena_recivida = concatenacion(lista_lenguaje[counter-1],c)
            lista_lenguaje[counter] = cadena_recivida
            afn.append(cadena_recivida)
        elif counter > len(lista_lenguaje)-3 and counter < len(lista_lenguaje)-1:
            cadena_recivida = concatenacion_v2(lista_lenguaje[counter+1],c)
            lista_lenguaje[counter] = cadena_recivida
            afn.append(cadena_recivida)
        counter +=1
             
    print("afn: " + str(afn))
    
def concatenacion(val,c):
    cadena_generada = []
    cadena =[]
    
    cadena.append(val[len(val)-1][2])
    cadena.append(c)
    cadena.append(q[0])
    cadena_generada.append(cadena)
    
    q.pop(0)
    
    # print("___")
    # print(cadena_generada)
    # print("___")
    
    return cadena_generada

def concatenacion_v2(val,c):
    cadena_generada = []
    cadena =[]
    cadena.append(q[0])
    cadena.append(c)
    cadena.append(val[0][0])
    cadena_generada.append(cadena)
    
    q.pop(0)
    
    # print("___")
    # print(cadena_generada)
    # print("___")
    
    return cadena_generada

#genera para la cadena de union
def union(c):
    cadena_generada = []
    cadena =[]
    #primera cadena superior
    cadena.append(q[0])
    cadena.append(eps)
    cadena.append(q[1])
    cadena_generada.append(cadena)
            
    cadena=[]
            
    cadena.append(q[1])
    cadena.append(c[0])
    cadena.append(q[2])
    cadena_generada.append(cadena)
            
    cadena=[]
            
    cadena.append(q[2])
    cadena.append(eps)
    cadena.append(q[3])
    cadena_generada.append(cadena)
            
    #segunda cadena inferior
    cadena=[]
            
    cadena.append(q[0])
    cadena.append(eps)
    cadena.append(q[4])
    cadena_generada.append(cadena)
            
    cadena=[]
            
    cadena.append(q[4])
    cadena.append(c[2])
    cadena.append(q[5])
    cadena_generada.append(cadena)
            
    cadena=[]
            
    cadena.append(q[5])
    cadena.append(eps)
    cadena.append(q[3])
    cadena_generada.append(cadena)
    
    q.pop(0)
    q.pop(0)
    q.pop(0)
    q.pop(0)
    q.pop(0)
    q.pop(0)
    
    # print("___")
    # print(cadena_generada)
    # print("___")
    
    return cadena_generada

def kleene(c):
    cadena_generada = []
    cadena =[]
    primero=c[0][0]
    ultimo=c[2][2]
    
    cadena.append(q[0])
    cadena.append(eps)
    cadena.append(primero)
    cadena_generada.append(cadena)
    
    cadena = []
    
    cadena.append(q[0])
    cadena.append(eps)
    cadena.append(q[1])
    cadena_generada.append(cadena)
    
    cadena = []
    
    cadena.append(ultimo)
    cadena.append(eps)
    cadena.append(primero)
    cadena_generada.append(cadena)
    
    cadena = []
    
    cadena.append(ultimo)
    cadena.append(eps)
    cadena.append(q[1])
    cadena_generada.append(cadena)
    
    q.pop(0)
    q.pop(0)
    
    # print("___")
    # print(cadena_generada)
    # print("___")
    
    return cadena_generada
    