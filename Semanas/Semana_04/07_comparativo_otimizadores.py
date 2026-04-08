import torch
import torch.nn as nn

# Instanciando um modelo genérico
modelo = nn.Linear(10, 2)

# 1. Otimizador SGD Tradicional (com Momentum)
otimizador_sgd = torch.optim.SGD(modelo.parameters(), lr=0.01, momentum=0.9)

# 2. Otimizador RMSProp
# alpha é o fator de suavização (o equivalente ao gamma da fórmula)
otimizador_rmsprop = torch.optim.RMSprop(modelo.parameters(), lr=0.01, alpha=0.99)

# 3. Otimizador Adam (O Padrão da Indústria)
# betas=(0.9, 0.999) controlam o decaimento do Primeiro e Segundo Momentos
otimizador_adam = torch.optim.Adam(modelo.parameters(), lr=0.001, betas=(0.9, 0.999))

print("Otimizadores configurados!")
print("Dica: Em 90% dos projetos modernos, comece usando o Adam com lr=1e-3.")