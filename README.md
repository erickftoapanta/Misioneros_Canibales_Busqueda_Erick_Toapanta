# Búsqueda Ciega: Misioneros y Caníbales

Repositorio para la Tarea Individual DG_S4 de Inteligencia Artificial - Escuela Politécnica Nacional.
Autor: Erick Toapanta

## ¿De qué trata este script?
Este es el código de mi tarea donde modelo el problema de los Misioneros y Caníbales. Implementé dos algoritmos de búsqueda a ciegas para encontrar la solución y comparar su rendimiento empírico:
- **BFS (Búsqueda en anchura):** Usando `collections.deque` como cola.
- **DFS (Búsqueda en profundidad):** Usando una lista estándar de Python como pila.

El script incluye un benchmarking que evalúa los nodos expandidos, el tiempo que tarda cada algoritmo en segundos y la cantidad de pasos (viajes en bote) que toma llegar a la meta.

## Representación de los estados
Abstraje el problema usando una tupla `(M, C, B)` que representa a los individuos en la **orilla izquierda**:
- `M`: Cantidad de misioneros (0 a 3)
- `C`: Cantidad de caníbales (0 a 3)
- `B`: Posición del bote (1 si está en la izquierda, 0 si está en la derecha)

- **Estado inicial:** `(3, 3, 1)` (Todos a la izquierda)
- **Estado objetivo:** `(0, 0, 0)` (Todos cruzaron)

## Cómo ejecutarlo localmente
El código usa librerías estándar de Python (`time`, `collections`), por lo que no necesitas instalar entornos virtuales ni dependencias extra (nada de pip install).

1. Clona este repositorio:
```bash
git clone https://github.com/erickftoapanta/Misioneros_Canibales_Busqueda_Erick_Toapanta.git
