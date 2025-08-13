# 🛰️ Filtro de Kalman en Python

Este repositorio contiene un ejemplo sencillo del **Filtro de Kalman** en 1D para estimar posición y velocidad, usando **Python**, **NumPy** y **Matplotlib**.
El objetivo es mostrar cómo este algoritmo puede combinar mediciones ruidosas de un sensor con un modelo matemático para obtener estimaciones más precisas.

---

## 📌 Descripción
En este ejemplo simulamos un objeto moviéndose a velocidad constante:
- **Posición real:** trayectoria perfecta sin ruido (conocida solo en la simulación).
- **Mediciones ruidosas:** simuladas como lo haría un sensor real con error.
- **Estimación Kalman:** resultado filtrado y más estable que sigue de cerca la posición real.

---

## 📦 Requisitos
- Python 3.x
- NumPy
- Matplotlib

Instalar dependencias:
```bash
pip install numpy matplotlib
