import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

# 1. Configurando o Mini-Batch (ex: lotes de 32 dados por vez)
X_treino = torch.randn(1000, 10) # 1000 exemplos, 10 atributos
y_treino = torch.randint(0, 2, (1000,)) # Classes 0 ou 1

dataset = TensorDataset(X_treino, y_treino)
# O DataLoader cuida de dividir a base e embaralhar (shuffle) a cada época
loader_mini_batch = DataLoader(dataset, batch_size=32, shuffle=True)

modelo = nn.Linear(10, 2)

# 2. Configurando o Momentum no Otimizador
# O SGD do PyTorch já aceita o parâmetro de inércia (momentum) nativamente!
otimizador = torch.optim.SGD(modelo.parameters(), lr=0.1, momentum=0.9)

# 3. Configurando o Decaimento da Taxa de Aprendizagem (Scheduler)
# StepLR vai reduzir o LR pela metade (gamma=0.5) a cada 10 épocas (step_size=10)
agendador_lr = torch.optim.lr_scheduler.StepLR(otimizador, step_size=10, gamma=0.5)

epocas = 30
for epoca in range(epocas):
    for lote_x, lote_y in loader_mini_batch:
        # Treinamento por Mini-lote ocorre aqui...
        otimizador.zero_grad()
        saida = modelo(lote_x)
        erro = nn.CrossEntropyLoss()(saida, lote_y)
        erro.backward()
        otimizador.step()
        
    # Atualiza a taxa de aprendizagem no final de cada época
    agendador_lr.step()
    
    # Visualizando a queda do LR
    if (epoca + 1) % 10 == 0:
        lr_atual = otimizador.param_groups[0]['lr']
        print(f"Época {epoca+1}: Taxa de Aprendizagem reduzida para {lr_atual:.4f}")