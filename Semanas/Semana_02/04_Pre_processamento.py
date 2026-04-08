import numpy as np

def normalizacao_min_max(dados):
    minimo = np.min(dados)
    maximo = np.max(dados)
    return (dados - minimo) / (maximo - minimo)

def normalizacao_z_score(dados):
    media = np.mean(dados)
    desvio = np.std(dados)
    return (dados - media) / desvio

# Dados de exemplo 
salarios = np.array([2000, 5000, 8000, 15000, 3500])

print(f"Original: {salarios}")
print(f"Min-Max (0-1): {normalizacao_min_max(salarios).round(2)}")
print(f"Z-Score (Media 0): {normalizacao_z_score(salarios).round(2)}")

# Exemplo rápido de One-Hot Manual
categorias = ["Gato", "Cachorro", "Peixe"]
# Se a entrada é 'Cachorro' (índice 1)
one_hot = np.eye(len(categorias))[1]
print(f"One-hot para 'Cachorro': {one_hot}")