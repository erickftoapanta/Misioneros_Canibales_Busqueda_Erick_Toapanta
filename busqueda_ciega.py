"""
Modulo de Busqueda Ciega: Misioneros y Canibales
Asignatura: Inteligencia Artificial
Escuela Politecnica Nacional - FIS
Autor: Erick Fabricio Toapanta Chanataxi
"""

from collections import deque
import time

ESTADO_INICIAL = (3, 3, 1)
ESTADO_OBJETIVO = (0, 0, 0)
ACCIONES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def es_valido(estado: tuple) -> bool:
    m_izq, c_izq, _ = estado
    m_der, c_der = 3 - m_izq, 3 - c_izq

    if not (0 <= m_izq <= 3 and 0 <= c_izq <= 3):
        return False

    if m_izq > 0 and c_izq > m_izq:
        return False
    if m_der > 0 and c_der > m_der:
        return False

    return True

def obtener_sucesores(estado: tuple) -> list:
    m_izq, c_izq, bote = estado
    sucesores = []

    for m, c in ACCIONES:
        if bote == 1: # Bote viaja de izquierda a derecha
            nuevo = (m_izq - m, c_izq - c, 0)
        else:         # Bote viaja de derecha a izquierda
            nuevo = (m_izq + m, c_izq + c, 1)

        # Solo agregamos el estado si nadie es devorado
        if es_valido(nuevo):
            sucesores.append(nuevo)

    return sucesores

def bfs(inicial=ESTADO_INICIAL, objetivo=ESTADO_OBJETIVO):
    t_inicio = time.perf_counter()
    frontera = deque([(inicial, [inicial])])
    visitados = {inicial}
    nodos_expandidos = 0

    while frontera:
        actual, camino = frontera.popleft()
        nodos_expandidos += 1

        if actual == objetivo:
            t_ejecucion = time.perf_counter() - t_inicio
            return camino, nodos_expandidos, t_ejecucion

        for sucesor in obtener_sucesores(actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                frontera.append((sucesor, camino + [sucesor]))

    return None, nodos_expandidos, time.perf_counter() - t_inicio


def dfs(inicial=ESTADO_INICIAL, objetivo=ESTADO_OBJETIVO):
    t_inicio = time.perf_counter()
    frontera = [(inicial, [inicial])]
    visitados = set()
    nodos_expandidos = 0

    while frontera:
        actual, camino = frontera.pop()

        if actual in visitados:
            continue

        visitados.add(actual)
        nodos_expandidos += 1

        if actual == objetivo:
            t_ejecucion = time.perf_counter() - t_inicio
            return camino, nodos_expandidos, t_ejecucion

        for sucesor in obtener_sucesores(actual):
            if sucesor not in visitados:
                frontera.append((sucesor, camino + [sucesor]))

    return None, nodos_expandidos, time.perf_counter() - t_inicio

def ejecutar_benchmarking():
    camino_bfs, nodos_bfs, t_bfs = bfs()
    camino_dfs, nodos_dfs, t_dfs = dfs()

    print("=" * 65)
    print("BENCHMARKING DE BUSQUEDA CIEGA: MISIONEROS Y CANIBALES")
    print("=" * 65)
    print(f"{'Métrica':<30} | {'BFS (Cola)':<14} | {'DFS (Pila)':<14}")
    print("-" * 65)
    print(f"{'Nodos Expandidos':<30} | {nodos_bfs:<14} | {nodos_dfs:<14}")
    print(f"{'Tiempo de Ejecución (s)':<30} | {t_bfs:<14.6f} | {t_dfs:<14.6f}")
    print(f"{'Longitud de la Solución':<30} | {len(camino_bfs)-1:<14} | {len(camino_dfs)-1:<14}")
    print("=" * 65)
    
    print("\nCamino optimo hallado por BFS (M, C, Bote en orilla izquierda):")
    for i, paso in enumerate(camino_bfs):
        print(f"Paso {i}: {paso}")

if __name__ == "__main__":
    ejecutar_benchmarking()

    
