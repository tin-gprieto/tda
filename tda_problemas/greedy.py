import sys
import networkx as nx
import heapq 

# Camino minimo de A a B de un grafo con aristas con peso
def dijkstra():
    return 

# Arbol de tendido minimo - subconjunto de aristas con peso minimo que cubra todos los vertices
def prim():
    return 

# Arbol de tendido minimo - subconjunto de aristas con peso minimo que cubra todos los vertices
def kruskal():
    return 

# Dado un conjunto de charlas con inicio-final, maximizar la cantidad de charlas que se pueden dar en el día sin que se colapsen
def problema_scheduling_charlas():
    return

# Dado un conjunto de tareas con una duración y una fecha límite (deadline), maximizar la cantidad de tareas.
# tips: 
#   F_i(final de la tarea): S_i(inicio) + T_i (duración)
#   L_i(latencia): F_i - D_i(deadline) ---> Minimizar la máxima latencia
def problema_scheduling_latencia():
    return

# Dada una lista de productos y una tasa de inflación por dia, obtener el orden de productos a comprar.
# Se debe comprar un producto por día y se deben comprar todos los productos.
def problema_inflacion():
    return

# Dada una lista de n números naturales, generar un grafo de n nodos cuyos grados (cantidad de aristas) sean los indicados por la lista.
def problema_generar_grafo():
    return

# Dado un conjunto de n empleados con k proyectos con cierta ganancia, maximizar la ganancia.
# Hay un máximo de 2 proyectos por empleado y cada proyecto debe realizarse por ciertos empleados en particular
def problema_empleados():
    return

# Dada una palabra, se busca comprimir en base a la frecuencia de los caracteres del mismo.
# tip: armando un arbol y utilizando un heap según la frecuencia
def problema_arbol_huffman(palabra):
    return


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("ERROR")
        sys.exit(1)
        
    match sys.argv[1]:
        case '-prim':
            prim()
        case '-kruskal':
            kruskal()
        case '-dijkstra':
            dijkstra()
        case '-a':
            problema_scheduling_charlas()
        case '-b':
            problema_scheduling_latencia()
        case '-c':
            problema_inflacion()
        case '-d':
            problema_generar_grafo()
        case '-e':
            problema_empleados()
        case '-f':
            problema_arbol_huffman('paralelo')