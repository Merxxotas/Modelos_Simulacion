import random

# Distribución de ventas de paquetes de 10 kg por día
ventas = [5, 10, 12, 15, 20]
probabilidades = [0.25, 0.15, 0.35, 0.125, 0.125]

# Parámetros de costos
costo_croqueta = 800
precio_venta = 1500
ganancia_por_kg = precio_venta - costo_croqueta
prob_perdida_inventario = 0.45

# Función para determinar la cantidad de paquetes vendidos en un día
def obtener_paquetes_vendidos():
    A = random.random()
    if A < 0.25:
        return 5
    elif A < 0.40:
        return 10
    elif A < 0.75:
        return 12
    elif A < 0.875:
        return 15
    else:
        return 20

# Simulación de Montecarlo
def simulacion_montecarlo(dias, donacion_por_kg):
    ganancias = []
    for i in range(dias):
        # Simular ventas del día usando el método basado en if
        paquetes_vendidos = obtener_paquetes_vendidos()
        
        # Cálculo de croquetas vendidas y donadas
        kg_vendidos = paquetes_vendidos * 10
        kg_donados = paquetes_vendidos * donacion_por_kg
        
        # Ganancia diaria sin pérdidas
        ganancia_diaria = (kg_vendidos * ganancia_por_kg) - (kg_donados * costo_croqueta)
        
        # Considerar la probabilidad de pérdida de inventario
        if random.random() < prob_perdida_inventario:
            ganancia_diaria *= 0.55  # Solo se queda con el 55% de las ganancias
        
        # Almacenar la ganancia del día
        ganancias.append(ganancia_diaria)
    
    # Promedio de ganancias sobre todos los días simulados
    return sum(ganancias) / len(ganancias)

# Parámetros de simulación
dias_simulados = 250

# Inciso a: calcular ganancia con 2 kg donados por cada 10 kg
ganancia_optima = simulacion_montecarlo(dias_simulados, donacion_por_kg=0.2)
print(f"Ganancia promedio con 2 kg donados: ${ganancia_optima:.2f}")

# Inciso b: ventas aumentan un 20% y donación aumenta a 4 kg por cada 10 kg
def obtener_paquetes_vendidos_aumentado():
    A = random.random()
    if A < 0.25:
        return 5 * 1.2
    elif A < 0.40:
        return 10 * 1.2
    elif A < 0.75:
        return 12 * 1.2
    elif A < 0.875:
        return 15 * 1.2
    else:
        return 20 * 1.2

# Usar la nueva función para simular con el aumento en ventas
def simulacion_montecarlo_ventas_aumentadas(dias, donacion_por_kg):
    ganancias = []
    for i in range(dias):
        paquetes_vendidos = obtener_paquetes_vendidos_aumentado()
        kg_vendidos = paquetes_vendidos * 10
        kg_donados = paquetes_vendidos * donacion_por_kg
        ganancia_diaria = (kg_vendidos * ganancia_por_kg) - (kg_donados * costo_croqueta)
        
        if random.random() < prob_perdida_inventario:
            ganancia_diaria *= 0.55
            
        ganancias.append(ganancia_diaria)
    
    return sum(ganancias) / len(ganancias)

# Simulación con el aumento de ventas y la nueva donación
ganancia_aumentada = simulacion_montecarlo_ventas_aumentadas(dias_simulados, donacion_por_kg=0.4)
print(f"Ganancia promedio con 4 kg donados: ${ganancia_aumentada:.2f}")

