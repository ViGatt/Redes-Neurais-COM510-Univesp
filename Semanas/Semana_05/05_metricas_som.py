import numpy as np

# 1. Dados de teste (3 amostras)
X = np.array([[1.0, 1.0], [0.1, 0.1], [0.5, 0.5]])

# 2. BMUs encontradas para cada dado (pesos dos vencedores)
bmus = np.array([[0.9, 0.9], [0.2, 0.2], [0.4, 0.4]])

# 3. ERRO DE QUANTIZAÇÃO: Média das distâncias
distancias_individuais = np.linalg.norm(X - bmus, axis=1)
quantization_error = np.mean(distancias_individuais)

print(f"Erro de Quantização do Mapa: {quantization_error:.4f}")