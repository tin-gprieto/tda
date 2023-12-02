import sys

def print_vector(V):
    s = '|'
    for v in V:
        if(v < 10):
            s += (' ' + str(v) + ' ')
        else:
            s += str(v) + ' '
    s += '|'
    print(s)

def print_matrix(M):
    n = len(M)-1 
    while(n >= 0):
        print_vector(M[n])
        n -= 1
        
# Dado un numero n, calcular su número de fibonacci
# f(n) = f(n-1) + f(n-2)
# f(0) = 0, f(1) = 1
def fibonacci(n):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    i=2
    while (i <= n):
        fibonacci.append(fibonacci[i -1] + fibonacci[i - 2])
        i += 1
    return fibonacci[n]

# Dado un conjunto de charlas con inicio-final, maximizar la cantidad de charlas que se pueden dar en el día sin que se colapsen
def problema_scheduling_charlas():
    return

# Dada una escalera de n escalones, obtener todas las formas distintas de subirla, subiendo de 1 o 2 escalones
def problema_escalones(n):
    s = []
    s.append(1)
    s.append(1)
    i = 2
    while(i <= n):
        s.append(s[i -1] + s[i-2])
        i += 1
    return s[n]


def reconstruir_juan_el_vago(optimos):
    trabajo = ['-' for i in range(len(optimos))]
    n = len(optimos)-1
    while(n > 0):
        if(trabajo[n] == 'T'):
            trabajo[n-1]='NT'
        elif(trabajo[n] == 'NT'):
            trabajo[n-1] = '-'
        elif(optimos[n] > optimos[n-1]):
            trabajo[n] = 'T'
            trabajo[n-1] = 'NT'
        else:
            trabajo[n] = 'NT'
            trabajo[n-1] = 'T'
        print(trabajo)
        n -= 1
    if(trabajo[1] == 'T'):
            trabajo[0]='NT'
    elif(trabajo[1] == 'NT'):
        trabajo[0] = 'T'
    return trabajo
    
# Dada una lista de ofertas laborales por día con cierta ganancia, obtener la secuencia de dias que maximice la ganancia sin trabajar dos días seguidos
def problema_juan_el_vago(ofertas):
    optimos = []
    dias = len(ofertas)
    optimos.append(ofertas[0])
    optimos.append(max(ofertas[0], ofertas[1]))
    i = 2
    while (i < dias):
        optimos.append(max(optimos[i-1], optimos[i-2] + ofertas[i]))
        i += 1
    return optimos, reconstruir_juan_el_vago(optimos)

# Dado un tablero, obtener la cantidad de caminos posibles para llegar a (n,m) desde (0,0)
# obs: Solo recoriendo para abajo o derecha (sin ir en diagonal)
def problema_laberinto():
    return

# Dado un teclado de telefono, devolver la cantidad de caminos posibles de largo N
def problema_telefono():
    return

def primer_optimo_ciudad(costos_ciudad, es_inicial, costo_mudanza):
    if(es_inicial):
        return costos_ciudad[0]
    return costo_mudanza[0] + costos_ciudad
        
# Dada una lista con costos de operacion en Londres y Californiam, y dado un costo de mudanza M, minimizar los costos de operación
def problema_londres_california(londres, california, costo):
    
    if(len(londres) != len(california)):
        print('ERROR')
        return
    n = len(londres) - 1
    optimos_L = [ londres[0] ]
    optimos_C = [ california[0] ]
    
    i = 1
    while( i <= n):
        optimos_L.append(min(londres[i] + optimos_L[i-1], londres[i] + costo + optimos_C[i-1]))
        optimos_C.append(min(california[i] + optimos_C[i-1], california[i] + costo + optimos_L[i-1]))
                                   # se queda                       #se muda()
        i += 1
    return optimos_L, optimos_C, min(optimos_L[n], optimos_C[n])

# Dada una lista de objetos con cierta ganancia y peso, y una capacidad C de la mochila, obtener la secuencia de objetos para maximizar la ganancia
def problema_knapsnack(elementos, capacidad):
    M = [[0 for j in range(capacidad + 1)] for i in range(len(elementos) + 1)]
    
    for elemento_m in range(1, len(M)):
        valor = elementos[elemento_m - 1][0]
        peso = elementos[elemento_m - 1][1]
        for peso_m in range(1, capacidad + 1):
            if(capacidad - peso > 0):
                M[elemento_m][peso_m] = max(M[elemento_m-1][peso_m], M[elemento_m][capacidad - peso] + valor)
            else:
                M[elemento_m][peso_m] = M[elemento_m-1][peso_m]
    return M

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
            print(fibonacci(8))            
        case '-b':
            problema_scheduling_charlas()
        case '-c':
            print(problema_escalones(5))
        case '-d':
            print(problema_juan_el_vago([100, 20, 30, 70, 20]))
        case '-e':
            problema_laberinto()
        case '-f':
            problema_telefono()
        case '-g':
            print(problema_londres_california([8,9,2,18,4,15],[10,5,10,7,13,10], 5))
        case '-h':
            print_matrix(problema_knapsnack([(10,1),(3,2),(4,4),(1,1)],6))
        case '-i':
            problema_cambio()
        case '-j':
            problema_bellman_ford()
        case '-k':
            problema_subset_sum()
