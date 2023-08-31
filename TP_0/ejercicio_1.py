prueba_1 = [1.2, 1.15, 1.14, 1.12, 0.98, 1.02, 1.18, 1.23]
prueba_2 = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 0.67, 1.11]
prueba_3 = [0.98, 0.67, 1.11, 1.2, 1.25, 1.34, 1.42, 1.52] 

def obtener_altura_vecinos(alumnos, i):
    anterior = alumnos[i-1]
    alumno = alumnos[i]
    siguiente = alumnos[i+1]

    return (anterior, alumno, siguiente)

def busqueda_binaria_mas_bajo(alumnos, inicio, final):
    
    punto_medio = int((inicio+final)/2)
    
    (ant, mas_bajo, sig) = obtener_altura_vecinos(alumnos, punto_medio)
    
    if((ant > mas_bajo) and (mas_bajo < sig)):
        return punto_medio

    if((ant > mas_bajo)):
        return busqueda_binaria_mas_bajo(alumnos, punto_medio, final)
    else:
        return busqueda_binaria_mas_bajo(alumnos, inicio, punto_medio)

def indice_mas_bajo(alumnos):
    return busqueda_binaria_mas_bajo(alumnos, 0, len(alumnos)-1)

def validar_mas_bajo(alumnos, indice):
    if((indice > len(alumnos)-1) or (indice == 0)):
        return False

    (ant, mas_bajo, sig) = obtener_altura_vecinos(alumnos, indice)

    return ((ant > mas_bajo) and (mas_bajo < sig))


print(indice_mas_bajo(prueba_1)) 
print(indice_mas_bajo(prueba_2)) 
print(indice_mas_bajo(prueba_3)) 