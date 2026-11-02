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
    