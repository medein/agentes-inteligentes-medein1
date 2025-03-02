import time
import heapq

# Definir el entorno con valores de recompensa
entorno = [
    [3, 1, -1, 4, 2],
    [2, -2, 5, -1, 3],
    [1, 3, 4, 2, 5],
    [0, -1, 2, 4, -2],
    [5, 2, 3, 1, 10]  # Meta con alta recompensa
]

# Posición inicial y meta
inicio = (0, 0)
meta = (4, 4)

# Direcciones posibles: derecha, abajo, izquierda, arriba
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Algoritmo de búsqueda de la mejor ruta (Máxima recompensa)
def encontrar_mejor_ruta():
    heap = [(-entorno[inicio[0]][inicio[1]], [inicio])]  # Usamos valores negativos para Max-Heap
    mejor_ruta = None
    mejor_recompensa = float('-inf')
    
    while heap:
        recompensa_actual, camino = heapq.heappop(heap)
        x, y = camino[-1]
        
        if (x, y) == meta and -recompensa_actual > mejor_recompensa:
            mejor_recompensa = -recompensa_actual
            mejor_ruta = camino
        
        for dx, dy in direcciones:
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < 5 and 0 <= nuevo_y < 5 and (nuevo_x, nuevo_y) not in camino:
                nueva_recompensa = recompensa_actual - entorno[nuevo_x][nuevo_y]
                heapq.heappush(heap, (nueva_recompensa, camino + [(nuevo_x, nuevo_y)]))
    
    return mejor_ruta, mejor_recompensa

# Mostrar el entorno con la ruta seguida
def mostrar_entorno(ruta):
    for i in range(5):
        for j in range(5):
            if (i, j) in ruta and (i, j) != inicio and (i, j) != meta:
                print('.', end=' ')  # Ruta seguida
            elif (i, j) == inicio:
                print('A', end=' ')  # Agente
            elif (i, j) == meta:
                print('M', end=' ')  # Meta
            else:
                print(entorno[i][j], end=' ')
        print()
    print('-' * 10)

# Ejecutar la búsqueda y mostrar la mejor ruta
mejor_ruta, recompensa = encontrar_mejor_ruta()
if mejor_ruta:
    print(f"Mejor recompensa obtenida: {recompensa}")
    for paso in mejor_ruta:
        time.sleep(1)
        mostrar_entorno(mejor_ruta[:mejor_ruta.index(paso) + 1])
else:
    print("No se encontró una ruta óptima.")
