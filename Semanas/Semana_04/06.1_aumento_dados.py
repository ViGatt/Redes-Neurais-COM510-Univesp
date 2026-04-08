import torch
from torchvision import transforms
from PIL import Image

# 1. Definindo o "Pipeline" de Aumento de Dados
# Quando uma imagem passar por aqui, ela sofrerá estas transformações de forma aleatória.
transformacoes_treino = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),      # 50% de chance de espelhar horizontalmente
    transforms.RandomRotation(degrees=15),       # Rotaciona até 15 graus para a esq/dir
    transforms.ColorJitter(brightness=0.2),      # Altera o brilho em até 20%
    transforms.ToTensor()                        # Converte a imagem para Tensor PyTorch
])

# 2. Pipeline de Teste (ATENÇÃO AQUI)
# No teste (ou validação), NÃO aplicamos aumento de dados. Queremos avaliar a imagem real.
transformacoes_teste = transforms.Compose([
    transforms.ToTensor()
])

# Simulação de uso:
# imagem_bruta = Image.open('foto_satelite.jpg')
# tensor_treino = transformacoes_treino(imagem_bruta)

print("Pipeline de Aumento de Dados configurado com sucesso!")