import sys

# Resolver un sudoku
def problema_sudoku():
    return 

# Dado un tablero de n*n y una posición inicial, determinar los movimientos de un caballo para que recorra el tablero completo
def problema_caballo():
    return

# Dado una cantidad n de dados, y un valor S, devolver todas las tiradas posibles para sumar S
def problema_sum_n_dados():
    return

# Dado un tablero de n*n, determinar la posición de n reinas para que ninguna colapse (no superpongan sus movimientos) con otra 
def problema_n_reinas():
    return

# Dado un grafo, devolver los nodos que no son adyacentes(comparten aristas) entre sí
def problema_independent_set():
    return

# Dado un grafo, devolver los nodos que cubran todos los vertices
def problema_vertex_cover():
    return

# Dado un grafo, devolver el camino que recorra a todos los grafos sin volver a pasar por el mismo
def problema_camino_hamiltoniano():
    return

# Dado un grafo, determinar si existe k subgrafos que no sean adyacentes
# k = 2, grafo bipartito
def problema_k_coloreo():
    return

# Dada una lista de enteros, devolver todos los subconjuntos que sumen N
def problema_subset_sum():
    return

# Dado dos grafos, probar si son isomórficos (que tengan la misma distribución nodos-aristas)
def problema_isomorfismo():
    return

# Dada una lista de materias con cátedras y horarios, devolver tdas las combinaciones de cursos sin que colapsen los horarios
def problema_materias():
    return

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("ERROR")
        sys.exit(1)
        
    match sys.argv[1]:
        case '-a':
            problema_sudoku(5)             
        case '-b':
            problema_caballo()
        case '-c':
            problema_sum_n_dados()
        case '-d':
            problema_n_reinas()
        case '-e':
            problema_independent_set()
        case '-f':
            problema_camino_hamiltoniano()
        case '-g':
            problema_k_coloreo()
        case '-h':
            problema_subset_sum()
        case '-i':
            problema_isomorfismo()
        case '-j':
            problema_materias()
        case '-k':
            problema_vertex_cover()