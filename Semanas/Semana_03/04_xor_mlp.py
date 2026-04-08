import numpy as np
from sklearn.neural_network import MLPClassifier

# Tabela Verdade do XOR
X = np.array([[0, 0], 
              [0, 1], 
              [1, 0], 
              [1, 1]])

# Saídas esperadas (Classes)
y = np.array([0, 1, 1, 0])

# Criando a rede MLP (1 camada oculta com 4 neurônios, ativação não-linear ReLU)
# max_iter=2000 garante que o algoritmo tenha tempo para convergir
mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=2000, random_state=42)

# Treinamento (Backpropagation acontecendo internamente)
mlp.fit(X, y)

# Testando as predições
print("--- Teste do Problema XOR com MLP ---")
for entrada in X:
    previsao = mlp.predict([entrada])
    print(f"Entrada: {entrada} -> Previsão do MLP: {previsao[0]}")