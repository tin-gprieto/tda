import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

s = []
t = []

def esta_visitado(vertice):
    return (vertice in s) or (vertice in t)

def obtener_grupo_opuesto(grupo):
    if(grupo is s):
        return t
    if(grupo is t):
        return s

#devuelve verdadero si ningun adyacente esta en el mismo grupo
def marcar_vertice(grafo, vertice, grupo):

    adyacentes = grafo.adyacentes(vertice)
    coincide_grupo = False
    i = 0
    
    while((not coincide_grupo) and (i<len(ady))):
        if(adyacentes[i] in grupo):
            coincide_grupo = True
        else:
            i += 1

    #lo marca si no tiene coincidencia con sus adyacentes
    if(not coincide_grupo):
        grupo.append(vertice)

    return (not coincide_grupo)

#obtiene las nuevas visitas para la lista, solamente agrega las adyacencias no visitadas
def obtener_nuevas_visitas(grafo, para_visitar, vertice):
    nuevas_visitas = []

    for ady in grafo.adyacentes(vertice):
        #chequeo que no este visitado ni este para visitar
        if( (not esta_visitado(ady) ) and (not (ady in para_visitar)) ):
            nuevas_visitas.append(ady)
    
    return nuevas_visitas

def evaluar_grafo(grafo, para_visitar, grupo_a_marcar):
    
    if(not para_visitar):
        return True

    vertice = para_visitar.pop()
    
    if(not(esta_visitado(vertice))):
        marcado = marcar_vertice(grafo, vertice, grupo_a_marcar)
        if(not marcado):
            return False
    
    para_visitar.append(obtener_nuevas_visitas(grafo, para_visitar, vertice))

    return evaluar_grafo(grafo, para_visitar, obtener_grupo_opuesto(grupo_a_marcar))
    

def es_bipartito(grafo):

    if (not grafo):
        return True
    
    para_visitar = [].append(grafo.vertices().copy().pop())

    return evaluar_grafo(grafo, para_visitar, s)
