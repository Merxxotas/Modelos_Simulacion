import numpy as np

# Distribución de ventas de paquetes de 10 kg por día
ventas = np.array([5, 10, 12, 15, 20])
probabilidades = np.array([0.25, 0.15, 0.35, 0.125, 0.125])

# Parámetros de costos
costo_croqueta = 800
precio_venta = 1500
ganancia_por_kg = precio_venta - costo_croqueta
prob_perdida_inventario = 0.45

# Simulación de Montecarlo
def simulacion_montecarlo(dias, donacion_por_kg):
    ganancias = []
    for i in range(dias):
        # Simular ventas del día
        paquetes_vendidos = np.random.choice(ventas, p=probabilidades)
        
        # Cálculo de croquetas vendidas y donadas
        kg_vendidos = paquetes_vendidos * 10
        kg_donados = paquetes_vendidos * donacion_por_kg
        
        # Ganancia diaria sin pérdidas
        ganancia_diaria = (kg_vendidos * ganancia_por_kg) - (kg_donados * costo_croqueta)
        
        # Considerar la probabilidad de pérdida de inventario
        ganancia_esperada = ganancia_diaria * (1 - prob_perdida_inventario)
        
        # Almacenar la ganancia del día
        ganancias.append(ganancia_esperada)
    
    # Promedio de ganancias sobre todos los días simulados
    return np.mean(ganancias)

# Parámetros de simulación
dias_simulados = 250

# Inciso a: calcular ganancia con 2 kg donados por cada 10 kg
ganancia_optima = simulacion_montecarlo(dias_simulados, donacion_por_kg=0.2)
print(f"Ganancia promedio con 2 kg donados: ${ganancia_optima:.2f}")

# Inciso b: ventas aumentan un 20% y donación aumenta a 4 kg por cada 10 kg
ventas_aumentadas = ventas * 1.2
ganancia_aumentada = simulacion_montecarlo(dias_simulados, donacion_por_kg=0.4)
print(f"Ganancia promedio con 4 kg donados: ${ganancia_aumentada:.2f}")
