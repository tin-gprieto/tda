import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

s = []
t = []

def esta_visitado(vertice):
    return (vertice in s) or (vertice in t)

def obtener_grupo_opuesto(vertice):
    if(vertice in s):
        return t
    if(vertice in t):
        return s
    
def coinciden_en_grupo(actual, anterior):
    return(((actual in s) and (anterior in s)) or ((actual in t) and (anterior in t)))

def cheaquear_adyacentes(grafo, vertice, grupo):

    ady = grafo.adyacentes(vertice)
    coincide_grupo = False
    i = 0
    
    while((not coincide_grupo) and (i<len(ady))):
        if(ady[i] in grupo):
            coincide_grupo = True
        else:
            i += 1
    
    #lo marca si no tiene coincidencia con sus adyacentes
    if(not coincide_grupo):
        grupo.append(vertice)
    
    return (not coincide_grupo)


def clasificar_vertice(grafo, anterior, actual):
    
    #vertice ya visitado
    if(esta_visitado(actual)):
        # que no comparta grupo con su adyacente anterior
        if(coinciden_en_grupo(actual, anterior)):
            return False
        return True

    #marcar vertice
    return cheaquear_adyacentes(grafo, actual, obtener_grupo_opuesto(anterior, actual)) 

    

def evaluar_grafo(grafo, vertice):

    for vecino in grafo.adyacentes(vertice):
        result = clasificar_vertice(grafo, vertice, vecino);
        if(result == False):
            break
    
    return result
    

def es_bipartito(grafo):

    es_bipartito = True
    
    if (not grafo):
        return es_bipartito
    
    primer_nodo = grafo.vertices().copy().pop()
    s.append(primer_nodo)
    es_bipartito = evaluar_grafo(grafo, primer_nodo)
    
    return es_bipartito