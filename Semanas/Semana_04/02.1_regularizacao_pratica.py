import torch
import torch.nn as nn

class RedeRegularizada(nn.Module):
    def __init__(self):
        super(RedeRegularizada, self).__init__()
        self.camada1 = nn.Linear(10, 50)
        # 1. Implementando Dropout (30% de chance de desligar neurônios)
        self.dropout = nn.Dropout(p=0.3)
        self.camada2 = nn.Linear(50, 2)

    def forward(self, x):
        x = torch.relu(self.camada1(x))
        x = self.dropout(x) # Aplica dropout após a ativação
        x = self.camada2(x)
        return x

modelo = RedeRegularizada()

# 2. Implementando Weight Decay (L2) diretamente no Otimizador
# O parâmetro weight_decay aplica a penalidade L2 automaticamente
otimizador = torch.optim.Adam(
    modelo.parameters(), 
    lr=0.01, 
    weight_decay=1e-5 # Este é o lambda da regularização L2
)

print("Configuração de Regularização Concluída!")