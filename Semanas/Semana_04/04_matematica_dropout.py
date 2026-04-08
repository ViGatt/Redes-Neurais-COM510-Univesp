import torch

def dropout_manual(X, probabilidade_drop):
    # Se a chance de dropar for 100%, zera tudo
    if probabilidade_drop == 1:
        return torch.zeros_like(X)
    # Se for 0%, mantém intacto
    if probabilidade_drop == 0:
        return X
    
    # Cria uma máscara de zeros e uns (1 = mantém, 0 = dropa)
    # torch.rand gera números entre 0 e 1. Se for maior que p, mantém.
    mascara = (torch.rand(X.shape) > probabilidade_drop).float()
    
    # Aplica a máscara e FAZ O REDIMENSIONAMENTO matemático ( / 1-p )
    return mascara * X / (1.0 - probabilidade_drop)

# Testando a teoria na prática
tensor_entrada = torch.ones(2, 5) # Tensor cheio de 1s
print("Tensor Original:")
print(tensor_entrada)

print("\nTensor com 50% de Dropout (p=0.5):")
# Os sobreviventes devem ter seu valor dobrado (1 / 0.5 = 2) para compensar os zeros!
print(dropout_manual(tensor_entrada, 0.5))