import numpy as np

def sigmoid(v):
    return 1 / (1 + np.exp(-v))

def tanh(v):
    return np.tanh(v)

def relu(v):
    return max(0, v)

# Testando um valor de campo local induzido (v)
v_teste = 0.5

print(f"Campo Local (v): {v_teste}")
print(f"Saída Sigmoide: {sigmoid(v_teste):.4f}")
print(f"Saída Tanh: {tanh(v_teste):.4f}")
print(f"Saída ReLU: {relu(v_teste):.4f}")