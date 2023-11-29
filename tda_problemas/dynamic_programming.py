import sys

# Dado un numero n, calcular su número de fibonacci
# f(n) = f(n-1) + f(n-2)
# f(0) = 0, f(1) = 1
def fibonacci():
    return 

# Dado un conjunto de charlas con inicio-final, maximizar la cantidad de charlas que se pueden dar en el día sin que se colapsen
def problema_scheduling_charlas():
    return

# Dada una escalera de n escalones, obtener todas las formas distintas de subirla, subiendo de 1 o 2 escalones
def problema_escalones():
    return

# Dada una lista de ofertas laborales por día con cierta ganancia, obtener la secuencia de dias que maximice la ganancia sin trabajar dos días seguidos
def problema_juan_el_vago():
    return

# Dado un tablero, obtener la cantidad de caminos posibles para llegar a (n,m) desde (0,0)
# obs: Solo recoriendo para abajo o derecha (sin ir en diagonal)
def problema_laberinto():
    return

# Dado un teclado de telefono, devolver la cantidad de caminos posibles de largo N
def problema_telefono():
    return

# Dada una lista con costos de operacion en Londres y Californiam, y dado un costo de mudanza M, minimizar los costos de operación
def problema_londres_california():
    return

# Dada una lista de objetos con cierta ganancia y peso, y una capacidad C de la mochila, obtener la secuencia de objetos para maximizar la ganancia
def problema_knapsnack():
    return

# Dado un sistema monetario y una cantidad C para devolver en cambio, obtener la cantidad y tipo de moneda para minimizar la cantidad de monedas
def problema_cambio():
    return

# Dado un grafo pesado, obtener el camino mínimo desde A hasta B (incluyendo aristas negativas != Dijkstra)
# No debe contar con ciclos negativos
def problema_bellman_ford():
    return

# Dada una lista de enteros, devolver todos los subconjuntos que sumen N
def problema_subset_sum():
    return

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("ERROR")
        sys.exit(1)
        
    match sys.argv[1]:
        case '-a':
            fibonacci()             
        case '-b':
            problema_scheduling_charlas()
        case '-c':
            problema_escalones()
        case '-d':
            problema_juan_el_vago()
        case '-e':
            problema_laberinto()
        case '-f':
            problema_telefono()
        case '-g':
            problema_londres_california()
        case '-h':
            problema_knapsnack()
        case '-i':
            problema_cambio()
        case '-j':
            problema_bellman_ford()
        case '-k':
            problema_subset_sum()
