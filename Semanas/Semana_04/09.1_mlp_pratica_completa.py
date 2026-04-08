import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader

# 1. Geração dos Dados (Problema: Aprender a onda senoidal com ruído)
np.random.seed(0)
X = np.arange(0, 20, 0.1).reshape(-1, 1)
Y = (np.sin(X) + 0.3 * np.random.randn(X.shape[0], 1) + 0.3 * X)

# Normalização simples
X = X / np.max(X)

# 2. Separação: Treino, Validação e Teste
# Primeiro separa 70% para teste/validação (sobram 30% pro treino neste ex. hipotético)
X_dev, X_test, Y_dev, Y_test = train_test_split(X, Y, test_size=0.7, random_state=3)
# Divide o "dev" no meio (50/50) para ter Treino e Validação
X_train, X_val, Y_train, Y_val = train_test_split(X_dev, Y_dev, test_size=0.5, random_state=3)

# Conversão para Tensores
X_train_t = torch.FloatTensor(X_train)
Y_train_t = torch.FloatTensor(Y_train)

# 3. Definição da Arquitetura (Topologia)
class ModeloMLP(nn.Module):
    def __init__(self):
        super(ModeloMLP, self).__init__()
        self.camada_oculta = nn.Linear(1, 50)
        self.saida = nn.Linear(50, 1) # Regressão: saída puramente linear

    def forward(self, x):
        # A ativação curva a reta para seguir o seno
        x = torch.relu(self.camada_oculta(x)) 
        x = self.saida(x)
        return x

modelo = ModeloMLP()

# 4. Aplicação das Melhorias de Engenharia
criterio = nn.MSELoss() # Erro Quadrático Médio
# Aqui a mágica acontece: Otimizador Adam + Regularização L2 (weight_decay)
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.05, weight_decay=1e-4)

# Treinamento (Exemplo Simplificado sem o loop do DataLoader por brevidade)
print("Configuração de Hiperparâmetros pronta para o treinamento!")