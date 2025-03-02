from collections import deque
import time

# Definir el laberinto (5x5) - ' ' = camino, 'X' = pared, 'E' = salida
laberinto = [
    [' ', ' ', 'X', ' ', ' '],
    ['X', ' ', 'X', ' ', 'X'],
    [' ', ' ', ' ', ' ', ' '],
    ['X', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', 'X', 'E']
]

# Posición inicial del agente
inicio = (0, 0)
meta = (4, 4)

# Direcciones posibles: derecha, abajo, izquierda, arriba
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Algoritmo de búsqueda en anchura (BFS) para encontrar la ruta más corta
def encontrar_camino():
    cola = deque([(inicio, [inicio])])  # (posición actual, camino seguido)
    visitados = set()
    
    while cola:
        (x, y), camino = cola.popleft()
        
        if (x, y) == meta:
            return camino  # Devolver la ruta encontrada
        
        visitados.add((x, y))
        
        for dx, dy in direcciones:
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < 5 and 0 <= nuevo_y < 5 and laberinto[nuevo_x][nuevo_y] != 'X' and (nuevo_x, nuevo_y) not in visitados:
                cola.append(((nuevo_x, nuevo_y), camino + [(nuevo_x, nuevo_y)]))
    
    return None  # No se encontró camino

# Mostrar el laberinto con la ruta seguida
def mostrar_laberinto(ruta):
    for i in range(5):
        for j in range(5):
            if (i, j) in ruta and (i, j) != inicio and (i, j) != meta:
                print('.', end=' ')  # Ruta seguida
            elif (i, j) == inicio:
                print('A', end=' ')  # Agente
            else:
                print(laberinto[i][j], end=' ')
        print()
    print('-' * 10)

# Ejecutar la búsqueda y mostrar la ruta encontrada
ruta = encontrar_camino()
if ruta:
    for paso in ruta:
        time.sleep(1)
        mostrar_laberinto(ruta[:ruta.index(paso) + 1])
else:
    print("No se encontró un camino hacia la meta.")
