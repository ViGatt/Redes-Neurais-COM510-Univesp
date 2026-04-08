import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

# 1. Dados de exemplo (X -> Entrada, y -> Alvo)
X = np.random.rand(100, 2)
y = np.sin(X[:, 0] * 5) + np.cos(X[:, 1] * 3)

# 2. FASE NÃO SUPERVISIONADA: Encontrar 10 centros (neurônios ocultos)
kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
centros = kmeans.cluster_centers_

# 3. TRANSFORMAÇÃO RBF: Calcular a ativação para cada dado em relação aos centros
def transformar_rbf(X, centros, sigma=1.0):
    ativacoes = []
    for x in X:
        # Distância Euclidiana para cada centro
        distancias = np.linalg.norm(x - centros, axis=1)
        # Ativação Gaussiana
        phi = np.exp(-(distancias**2) / (2 * sigma**2))
        ativacoes.append(phi)
    return np.array(ativacoes)

X_rbf = transformar_rbf(X, centros)

# 4. FASE SUPERVISIONADA: Ajustar pesos de saída com Regressão Linear
modelo_saida = LinearRegression().fit(X_rbf, y)

print(f"Pesos da camada de saída calculados: {modelo_saida.coef_.shape}")