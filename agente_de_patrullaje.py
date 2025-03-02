import random
import time

# Definir el entorno de patrullaje (una cuadrícula 5x5)
entorno = [[' ' for _ in range(5)] for _ in range(5)]
obstaculos = [(2, 2), (3, 1)]  # Posiciones de obstáculos

# Agregar obstáculos al entorno
for obs in obstaculos:
    entorno[obs[0]][obs[1]] = 'X'

# Posición inicial del agente
agente_x, agente_y = 0, 0

# Direcciones posibles: derecha, abajo, izquierda, arriba
direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direccion_actual = 0  # Iniciamos moviéndonos a la derecha

# Función para imprimir el entorno
def mostrar_entorno():
    for i in range(5):
        for j in range(5):
            if (i, j) == (agente_x, agente_y):
                print('A', end=' ')  # Agente
            else:
                print(entorno[i][j], end=' ')
        print()
    print('-' * 10)

# Bucle de patrullaje
def patrullar():
    global agente_x, agente_y, direccion_actual
    
    while True:
        # Calcular la siguiente posición
        nuevo_x = agente_x + direcciones[direccion_actual][0]
        nuevo_y = agente_y + direcciones[direccion_actual][1]
        
        # Verificar si la nueva posición es válida
        if 0 <= nuevo_x < 5 and 0 <= nuevo_y < 5 and entorno[nuevo_x][nuevo_y] != 'X':
            agente_x, agente_y = nuevo_x, nuevo_y
        else:
            # Si hay un obstáculo o está fuera de la cuadrícula, cambiar dirección aleatoriamente
            direccion_actual = random.randint(0, 3)
        
        mostrar_entorno()
        time.sleep(1)

# Ejecutar el patrullaje
patrullar()
