# 🛶 Búsqueda Ciega: Misioneros y Caníbales

**Tarea Individual DG_S4 - Inteligencia Artificial**  
**Escuela Politécnica Nacional - Facultad de Ingeniería de Sistemas**  
**Autor:** Erick Fabricio Toapanta Chanataxi  

## 📌 Descripción del Proyecto
Este repositorio contiene la abstracción matemática y la implementación computacional del clásico problema de los Misioneros y Caníbales. El objetivo principal es evaluar empíricamente el rendimiento de las estrategias de búsqueda no informada mediante algoritmos clásicos.

Se implementaron dos estrategias de búsqueda de estados:
- **BFS (Búsqueda en Anchura):** Implementada mediante una estructura FIFO (`collections.deque`).
- **DFS (Búsqueda en Profundidad):** Implementada mediante una estructura LIFO (Pila en Python).

## ⚙️ Requisitos
- Python 3.8 o superior.
- Librerías estándar de Python (`time`, `collections`). No requiere instalación de dependencias externas.

## 🚀 Ejecución y Uso
Para ejecutar el script de benchmarking y observar la comparativa de métricas en la terminal, utiliza el siguiente comando en la raíz del proyecto:

```bash
python busqueda_ciega.py
