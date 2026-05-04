import numpy as np

# 1. Entrada (Vetor de pesos de um dado)
x = np.array([0.5, 0.8, 0.1])

# 2. Grade de Neurônios (4 neurônios com pesos aleatórios)
pesos_neuroneos = np.random.rand(4, 3)

# 3. COMPETIÇÃO: Calcular a distância Euclidiana
distancias = np.linalg.norm(x - pesos_neuroneos, axis=1)

# Encontrar o vencedor (BMU)
vencedor_idx = np.argmin(distancias)

print(f"Distâncias: {distancias}")
print(f"O neurônio vencedor (BMU) é o índice: {vencedor_idx}")