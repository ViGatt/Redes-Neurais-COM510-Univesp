import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

# 1. Definindo uma camada com 5 entradas e 3 saídas (15 pesos no total)
camada = nn.Linear(5, 3)

print("Pesos ANTES da poda:")
print(camada.weight)

# 2. Aplicando a Poda (Unstructured L1)
# Vamos podar 40% (0.4) das conexões dessa camada específicas.
# O método L1Unstructured remove os pesos com os menores valores absolutos (mais próximos de zero).
prune.l1_unstructured(camada, name='weight', amount=0.4)

print("\nPesos DEPOIS da poda (note os zeros forçados):")
print(camada.weight)

# 3. Tornando a poda permanente
# O PyTorch cria uma "máscara" temporária. O comando abaixo aplica a máscara 
# de forma definitiva aos parâmetros reais da rede, deixando-a mais leve.
prune.remove(camada, 'weight')