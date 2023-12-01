import sys

def es_numero_valido(sudoku, dim, fila, columna, valor):
    
    if(sudoku[fila][columna] != 0):
        return False
    
    # Verificar si el valor está en la fila
    if valor in sudoku[fila]:
        return False
    
    # Verificar si el valor está en la columna
    for i in range(dim):
        if sudoku[i][columna] == valor:
            return False
    
    return True

# Resolver un sudoku
def problema_sudoku(sudoku, dim, i, j, cantidad):
    if(cantidad >= dim*dim):
        return True
    
    for num in range(1, dim):
        if(es_numero_valido(sudoku, dim, i, j, num)):
            sudoku[i][j] = num
            if(j < dim):
                if(problema_sudoku(sudoku, dim, i, j+1, cantidad+1)):
                    return True
            if(i < dim):
                if(problema_sudoku(sudoku, dim, i+1, j, cantidad+1)):
                    return True
        sudoku[i][j] = 0    
    return False

# Dado un tablero de n*n y una posición inicial, determinar los movimientos de un caballo para que recorra el tablero completo
def problema_caballo():
    return

# Dado una cantidad n de dados, y un valor S, devolver todas las tiradas posibles para sumar S
def problema_sum_n_dados(n, S, dados_usados, solucion_parcial, soluciones):
    
    if(sumar_elementos(solucion_parcial) == S and dados_usados == n): # es solucion
        soluciones.append(solucion_parcial[:]) # agrego solucion
        return 
    
    if(sumar_elementos(solucion_parcial) > S or dados_usados == n): # pruebo si no es válida (excede o no alcanza con todos los dados)
        return #vuelvo
    
    for dado in range(1,7):
        solucion_parcial.append(dado) #avanzo
        problema_sum_n_dados(n, S , dados_usados + 1, solucion_parcial, soluciones) # llamo recursivamente
        solucion_parcial.remove(dado) # sino vuelvo atrás (pruebo con el siguiente)

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

def nodos_cubiertos(grafo, subset):
    cubiertos = set()
    for n in subset:
        cubiertos.add(n)
        for a in grafo[n]:
            cubiertos.add(a)
    print(f"s: {subset}, c: {cubiertos}")
    return cubiertos
    
# Dado un grafo, devolver un subconjunto k de nodos donde los nodos pertenecen a k o son adyacentes
def problema_dominating_set(grafo, nodos, subset, min_subset):
    
    if(len(nodos_cubiertos(grafo, subset)) == len(grafo)):
        if(len(subset) < len(min_subset)):
            min_subset = subset
        return True

    for n in range(len(nodos)):
        if(nodos[n] not in nodos_cubiertos(grafo, subset)):
            subset.add(nodos[n])
            if(problema_dominating_set(grafo, nodos, subset, min_subset)):
                return True
            subset = set()
    
    return False

# Dado un grafo, devolver el camino que recorra a todos los grafos sin volver a pasar por el mismo
def camino_hamiltoniano(grafo, nodo, camino):
    
    camino.append(nodo)
    
    if(len(camino) == len(grafo)):
        return True
    
    for ady in grafo[nodo]:
        if(ady not in camino):
            if(camino_hamiltoniano(grafo, ady, camino)):
                return True

    camino.pop()
    return False

def problema_camino_hamiltoniano(grafo):
    camino = []
    for v in grafo:
        if(camino_hamiltoniano(grafo, v, camino)):
            return camino
    return None
    
def adyacentes_diferentes_colores(grafo, nodo, coloreados):
    for c in list(coloreados.keys()):
        if( c in grafo[nodo] and coloreados[c] == coloreados[nodo]):
            return False
    return True

# Dado un grafo, determinar si existe k subgrafos que no sean adyacentes
# k = 2, grafo bipartito
def problema_k_coloreo(grafo, nodos, coloreados, colores):
    
    if(len(coloreados) == len(grafo)): #es solucion
        print(coloreados)
        return True
    
    for n in range(len(nodos)):
        for i in colores:
            coloreados.update({nodos[n] : i}) 
            if (adyacentes_diferentes_colores(grafo, nodos[n], coloreados)): # compruebo solucion parcial
                if(problema_k_coloreo(grafo, nodos[n+1:], coloreados, colores)): # llamada recursiva
                    return True 
            # vuelvo (pruebo con otro color)
            
    return False

def sumar_elementos(lista):
    sum=0
    for i in lista:
        sum += i
    return sum

# Dada una lista de enteros, devolver todos los subconjuntos que sumen N
def problema_subset_sum(lista, solucion, N):
    
    if(sumar_elementos(solucion) == N): # devuelvo si es solucion
        return True
    if(sumar_elementos(solucion) > N): # solucion parcial es válida ?
        return False

    for j in range(len(lista)):
        solucion.append(lista[j]) #avanzo
        if(problema_subset_sum(lista[j+1:], solucion, N)): #llamada recursivamente
            return True
        else:
            solucion.remove(lista[j]) #vuelvo
    
    return False #No hay solucion

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
    
    grafo = {
                'a' : ['c', 'b'],
                'b' : ['a','d', 'h'],
                'c' : ['a', 'g'],
                'd' : ['b', 'h'],
                'e' : ['g'],
                'g' : ['e', 'c'],
                'h' : ['b', 'd'],
            }
    
    match sys.argv[1]:
        case '-a':
            sudoku = [
                    [0,0,0,4],
                    [0,0,0,0],
                    [2,0,0,3],
                    [4,0,1,2],
                    ]
            problema_sudoku(sudoku, 4, 0, 0, 6)
            print(sudoku)             
        case '-b':
            problema_caballo()
        case '-c':
            soluciones = []
            problema_sum_n_dados(2, 10, 0, [], soluciones)
            print(soluciones)
        case '-d':
            problema_n_reinas()
        case '-e':
            problema_independent_set()
        case '-f':
            print(problema_camino_hamiltoniano(grafo))
        case '-g':
            problema_k_coloreo(grafo, list(grafo.keys()), {}, [0, 1, 2])
        case '-h':
            sol = []
            print(problema_subset_sum([4, 3, 5, 2, 6], sol, 11))
            print(sol)
        case '-i':
            problema_isomorfismo()
        case '-j':
            problema_materias()
        case '-k':
            problema_vertex_cover()
        case '-l':
            solucion = list(grafo.keys())
            problema_dominating_set(grafo, list(grafo.keys()), set(), solucion)
            print(solucion)