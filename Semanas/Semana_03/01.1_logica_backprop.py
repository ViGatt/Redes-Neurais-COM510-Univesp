import numpy as np

# Funções auxiliares (Sigmoide e sua derivada)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# --- FASE FORWARD ---
# Entrada -> [Peso1] -> Camada Oculta -> [Peso2] -> Saída
entrada = np.array([0.5, 0.1])
peso_oculto = np.random.rand(2, 3) 
saida_oculta = sigmoid(np.dot(entrada, peso_oculto))

# --- FASE BACKWARD (Conceitual) ---
alvo = 0.8
erro_saida = alvo - saida_final # Exemplo hipotético
# Gradiente local depende da derivada da ativação 
delta_saida = erro_saida * sigmoid_derivative(saida_final)