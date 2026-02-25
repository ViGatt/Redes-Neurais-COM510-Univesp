import numpy as np

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

# Teste com uma lista de valores
valores = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])

print("Entradas:", valores)
print("ReLU:    ", relu(valores))
print("Sigmoid: ", sigmoid(valores).round(3))
print("Tanh:    ", tanh(valores).round(3))