import random

def simular_flujo_agua():
    A = random.random()
    if A < 0.15:
        return 0
    elif A < 0.50:  # 0.15 + 0.35
        return 1
    elif A < 0.80:  # 0.50 + 0.30
        return 2
    else:
        return 3

def simular_represa(meses):
    capacidad_maxima = 4
    demanda_energia = 2
    agua_actual = 1  # Agua inicial
    total_vertido = 0
    veces_energia_insuficiente = 0
    
    for i in range(meses):
        # Simular el flujo de agua entrante
        flujo = simular_flujo_agua()
        
        # Calcular el agua total antes de vertido
        agua_total = agua_actual + flujo
        
        # Calcular el agua vertida por exceso
        vertido = max(0, agua_total - capacidad_maxima)
        total_vertido += vertido
        
        # Ajustar el agua total después del vertido
        agua_total = min(agua_total, capacidad_maxima)
        
        # Generar energía
        energia_generada = min(demanda_energia, agua_total)
        if energia_generada < demanda_energia:
            veces_energia_insuficiente += 1
        
        # Actualizar el agua para el próximo mes
        agua_actual = agua_total - energia_generada
    
    return total_vertido, veces_energia_insuficiente

# Configuración de la simulación
num_simulaciones = 10000
meses = 15 * 12  # 15 años

# Realizar múltiples simulaciones
resultados_vertido = []
resultados_energia_insuficiente = []

for i in range(num_simulaciones):
    vertido, energia_insuficiente = simular_represa(meses)
    resultados_vertido.append(vertido)
    resultados_energia_insuficiente.append(energia_insuficiente)

# Calcular resultados promedio
promedio_vertido = sum(resultados_vertido) / num_simulaciones
promedio_energia_insuficiente = sum(resultados_energia_insuficiente) / num_simulaciones

# Imprimir resultados
print(f"Promedio de unidades vertidas en 15 años: {promedio_vertido:.2f}")
print(f"Promedio de veces con energía insuficiente en 15 años: {promedio_energia_insuficiente:.2f}")
