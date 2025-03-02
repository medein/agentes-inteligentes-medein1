import random
import time

# Definir el entorno (una cuadrícula 5x5)
entorno = [[' ' for _ in range(5)] for _ in range(5)]
obstaculos = [(1, 3), (2, 2), (3, 4)]  # Posiciones de obstáculos

# Agregar obstáculos al entorno
for obs in obstaculos:
    entorno[obs[0]][obs[1]] = 'X'

# Posición inicial del agente
agente_x, agente_y = 0, 0
visitados = set()  # Conjunto para almacenar posiciones visitadas

# Direcciones posibles: derecha, abajo, izquierda, arriba
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Función para imprimir el entorno
def mostrar_entorno():
    for i in range(5):
        for j in range(5):
            if (i, j) == (agente_x, agente_y):
                print('A', end=' ')  # Agente
            elif (i, j) in visitados:
                print('.', end=' ')  # Área visitada
            else:
                print(entorno[i][j], end=' ')
        print()
    print('-' * 10)

# Bucle de exploración
def explorar():
    global agente_x, agente_y
    
    while len(visitados) < (5 * 5) - len(obstaculos):
        visitados.add((agente_x, agente_y))  # Registrar la posición visitada
        
        # Obtener posibles movimientos válidos
        movimientos_validos = []
        for dx, dy in direcciones:
            nuevo_x, nuevo_y = agente_x + dx, agente_y + dy
            if 0 <= nuevo_x < 5 and 0 <= nuevo_y < 5 and entorno[nuevo_x][nuevo_y] != 'X' and (nuevo_x, nuevo_y) not in visitados:
                movimientos_validos.append((nuevo_x, nuevo_y))
        
        if movimientos_validos:
            agente_x, agente_y = random.choice(movimientos_validos)
        else:
            # Si no hay movimientos nuevos, moverse aleatoriamente sin repetir inmediato
            agente_x, agente_y = random.choice([(agente_x + dx, agente_y + dy) for dx, dy in direcciones if 0 <= agente_x + dx < 5 and 0 <= agente_y + dy < 5 and entorno[agente_x + dx][agente_y + dy] != 'X'])
        
        mostrar_entorno()
        time.sleep(1)

# Ejecutar la exploración
explorar()
