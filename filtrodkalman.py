import numpy as np
import matplotlib.pyplot as plt

# Estado inicial [posición, velocidad]
x = np.array([[0], [1]])  # posición=0, velocidad=1

# Matriz de transición (movimiento constante)
F = np.array([[1, 1],
              [0, 1]])

# Matriz de observación (solo medimos posición)
H = np.array([[1, 0]])

# Covarianza inicial (incertidumbre alta)
P = np.eye(2) * 1000

# Ruido de medición (sensor)
R = np.array([[5]])

# Ruido del proceso (modelo)
Q = np.eye(2) * 0.01

# Simulación de datos
tiempo = np.arange(1, 21)  # 20 pasos de tiempo
posicion_real = tiempo     # posición real: aumenta 1 por paso
mediciones = [pos + np.random.normal(0, 2) for pos in posicion_real]

# Lista para estimaciones
estimaciones = []

# Filtro de Kalman
for z in mediciones:
    # -------- PREDICCIÓN --------
    x = F @ x
    P = F @ P @ F.T + Q

    # -------- CORRECCIÓN --------
    Z = np.array([[z]])
    y = Z - H @ x
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    x = x + K @ y
    P = (np.eye(2) - K @ H) @ P

    # Guardar estimación
    estimaciones.append(x[0, 0])

# Mostrar resultados en consola
for t, med, est in zip(tiempo, mediciones, estimaciones):
    print(f"t={t:2d}  Medición: {med:.2f}  → Estimación: {est:.2f}")

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(tiempo, posicion_real, label='Posición real', color='green', linewidth=2)
plt.scatter(tiempo, mediciones, label='Mediciones ruidosas', color='red')
plt.plot(tiempo, estimaciones, label='Estimación Kalman', color='blue', linestyle='--')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtro de Kalman - Estimación de posición')
plt.legend()
plt.grid(True)
plt.savefig('ejemplo_grafica.png', dpi=300)  # Guarda la gráfica
plt.show()
