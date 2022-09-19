
eps = "epsilon"
q = []
afn_control = []
afn = []

cadena = []
back = []

#para generar todos los posibles q0,q1,q2,...,q99
for i in range(100):
    value = "q"+str(i)
    q.append(value)

def construccion_thompson(output):
    last = ""
    first = ""
    print(output)
    lista = []
    chain = []
    for l in output:
        back.append(l)
        print("===========")
        print(afn)
        print("cadena: " + str(cadena))
        print(back)
        print(first, last)
        if back[len(back)-1] == "|":
            if len(cadena) > 1 and len(back) == 1:
                chain.append(q[0])
                chain.append(eps)
                chain.append(cadena[len(cadena)-2][0][0])
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                chain.append(cadena[len(cadena)-2][len(cadena[len(cadena)-2])-1][2])
                chain.append(eps)
                chain.append(q[1])
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                chain.append(q[0])
                chain.append(eps)
                chain.append(first)
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                chain.append(cadena[len(cadena)-1][len(cadena[len(cadena)-1])-1][2])
                chain.append(eps)
                chain.append(q[1])
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                cadena.pop(len(cadena)-1)
                cadena.pop(len(cadena)-1)

                cadena.append(lista)
                lista = []
                
                first = q[0]
                last = q[1]
                
                q.pop(0)
                q.pop(0)
                
                back.pop(len(back)-1)
            else:
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
                
                first = q[0]
                last = q[3]
                
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
            if len(back)>1:
                if len(back)>2:
                    if len(back[len(back)-2]) == 1 and len(back[len(back)-3]) == 1:
                        chain.append(q[0])
                        chain.append(back[len(back)-3])
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
                        
                        cadena.append(lista)
                        lista = []
                        
                        first = q[0]
                        last = q[2]
                        
                        q.pop(0)
                        q.pop(0)
                        q.pop(0)
                        
                        back.pop(len(back)-1)
                        back.pop(len(back)-1)
                        back.pop(len(back)-1)
                    
                else:
                    chain.append(last)
                    chain.append(back[len(back)-2])
                    chain.append(q[0])
                    lista.append(chain)
                    afn.append(chain)
                    chain = []
                    
                    cadena[len(cadena)-1].extend(lista)
                    lista = []
                    
                    last = q[0]
                    
                    q.pop(0)
                        
                    back.pop(len(back)-1)
                    back.pop(len(back)-1)
            else:
                chain.append(cadena[len(cadena)-2][len(cadena[len(cadena)-2])-1][2])
                chain.append(eps)
                chain.append(first)
                lista.append(chain)
                afn.append(chain)
                chain = []
                
                cadena[len(cadena)-1].extend(lista)
                lista = []
                
                q.pop(0)
                    
                back.pop(len(back)-1)
        
        elif back[len(back)-1] == "*":
            chain.append(q[0])
            chain.append(eps)
            chain.append(first)
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(q[0])
            chain.append(eps)
            chain.append(q[1])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(last)
            chain.append(eps)
            chain.append(first)
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            chain.append(last)
            chain.append(eps)
            chain.append(q[1])
            lista.append(chain)
            afn.append(chain)
            chain = []
            
            cadena[len(cadena)-1].extend(lista)
            lista = []
            
            first = q[0]
            last = q[1]
            
            q.pop(0)
            q.pop(0)
            
            back.pop(len(back)-1)
            
    print("afn:" + str(afn))
    # print("back:" + str(back))
    # print("cadena:" + str(cadena))
    
    return afn