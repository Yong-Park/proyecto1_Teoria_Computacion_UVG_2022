
def simulacion_afn(afn, cadena, inicio, final):
    point = inicio
    end = final
    caminos = []
    eps = "epsilon"
    
    caminos.append(point)
    print("===================")
    for l in cadena:
        print(caminos)
        print(l)
        #obtener todos los posibles caminos
        i = 0
        while i < len(cadena):
            for p in caminos:
                for c in afn:
                    if c == p:
                        if afn[c][eps]:
                            for x in afn[c][eps]:
                                caminos.append(x)
                            i = 0
                            caminos.remove(p)
            i += 1
        #desde estos caminos ver cual si cumple
        print("caminos: " + str(caminos))
        for camino in caminos:
            if afn[camino][l]:
                caminos.clear()
                caminos.extend(afn[camino][l])
                break
    print("termino")
    print(caminos)
            
    


def simulacion_afd(afd, cadena, inicio, final):
    point = inicio
    end = final
    #encontrar su cadena
    for c in afd:
        if point in c:
            point = c
            break
    #realizar el ciclo para ver si la cadena es aceptada
    # print("============================")
    # print(point)
    for l in cadena:
        print(l)
        for c in afd:
            if c == str(point):
                point = afd[c][l]
                # print(point)
                break
            
    #revisar si es aceptada o no
    if end in point:
        print("cadena aceptada")
    else:
        print("cadena rechazada")