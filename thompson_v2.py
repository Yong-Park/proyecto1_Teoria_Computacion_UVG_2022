
eps = "epsilon"
q = []

afn = []

cadena = []
back = []
last = ""

#para generar todos los posibles q0,q1,q2,...,q99
for i in range(100):
    value = "q"+str(i)
    q.append(value)

def construccion_thompson(output):
    lista = []
    chain = []
    for l in output:
        back.append(l)
        if back[len(back)-1] == "|":
            chain.append(q[0])
            chain.append(eps)
            chain.append(q[1])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[1])
            chain.append(back[len(back)-2])
            chain.append(q[2])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[2])
            chain.append(eps)
            chain.append(q[3])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[0])
            chain.append(eps)
            chain.append(q[4])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[4])
            chain.append(back[len(back)-3])
            chain.append(q[5])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[5])
            chain.append(eps)
            chain.append(q[3])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            cadena.append(lista)
            lista = []
            
            q.pop(0)
            q.pop(0)
            q.pop(0)
            q.pop(0)
            q.pop(0)
            q.pop(0)
            
            back.pop(len(back)-1)
            back.pop(len(back)-1)
            back.pop(len(back)-1)
        
        elif back[len(back)-1] == "?":
            if len(back) == 2:
                chain.append(cadena[len(cadena) - 1][len(cadena[len((cadena))-1]) -1][2])
                chain.append(back[len(back)-2])
                chain.append(q[0])
                last = q[0]
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                cadena.append(lista)
                lista = []
                
                q.pop(0)
                
                back.pop(len(back)-1)
                back.pop(len(back)-1)
            else:
                chain.append(last)
                chain.append(eps)
                chain.append(cadena[len(cadena) - 1][0][0])
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                cadena.append(lista)
                lista = []
                
                back.pop(len(back)-1)
        
        elif back[len(back)-1] == "*":
            chain.append(q[0])
            chain.append(eps)
            chain.append(cadena[len(cadena) - 1][0][0])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[0])
            chain.append(eps)
            chain.append(q[1])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(cadena[len(cadena) - 1][5][2])
            chain.append(eps)
            chain.append(cadena[len(cadena) - 1][0][0])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(cadena[len(cadena) - 1][5][2])
            chain.append(eps)
            chain.append(q[1])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            cadena.append(lista)
            lista = []
            
            q.pop(0)
            q.pop(0)
            
            back.pop(len(back)-1)
            
    # print("afn:" + str(afn))
    # print("back:" + str(back))
    # print("cadena:" + str(cadena))
    
    return afn