import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

s = []
t = []

def esta_visitado(vertice):
    return (vertice in s) or (vertice in t)


def cheaquear_adyacentes(grafo, vertice, grupo):

    ady = grafo.adyacentes(vertice)
    coincidencia = False
    i = 0
    
    while((not coincidencia) and (i<len(ady))):
        if(ady[i] in grupo):
            coincidencia = True
        else:
            i += 1
    return (not coincidencia)


def clasificar_vertice(grafo, anterior, actual):
    
    #anterior sin clasificar (primer nodo)
    if(not(esta_visitado(anterior))):
        s.append(anterior)
    
    #vertice ya visitado
    if(esta_visitado(actual)):
        # que no comparta grupo con su vecino
        if((actual in s) and (anterior in s)):
            return False
        if((actual in t) and (anterior in t)):
            return False
        return True

    #marcar vertice
    if(anterior in s):
        t.append(actual)
        return cheaquear_adyacentes(grafo, actual, t)
    if(anterior in t):
        s.append(actual)
        return cheaquear_adyacentes(grafo, actual, s)

    

def evaluar_grafo(grafo, vertice):

    for vecino in grafo.adyacentes(vertice):
        result = clasificar_vertice(grafo, vertice, vecino);
        if(result == False):
            break
    
    return result
    

def es_bipartito(grafo):

    if (not grafo):
        return True

    result = evaluar_grafo(grafo, grafo.vertices().pop())
    
    s = []
    t = []
    
    return result
