import numpy as np

def sinal_nodal(sinais_entrada, pesos_sinapticos):
    """
    Simula a Regra 2: O sinal nodal é a soma de todos 
    os sinais que entram no nó via elos incidentes.
    """
    # Multiplicação elemento a elemento e soma (Produto Escalar)
    soma_incidente = np.dot(sinais_entrada, pesos_sinapticos)
    return soma_incidente

# Exemplo de 3 neurônios enviando sinais para um nó central
sinais = np.array([0.5, -0.2, 0.8])
pesos  = np.array([0.7, 0.4, 0.9])

resultado = sinal_nodal(sinais, pesos)
print(f"Sinal resultante no Nó: {resultado:.2f}")