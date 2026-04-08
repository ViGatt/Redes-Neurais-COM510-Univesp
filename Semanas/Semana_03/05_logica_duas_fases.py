import numpy as np

# Taxa de aprendizagem
eta = 0.1

# --- 1. FASE PARA FRENTE (FORWARD) ---
# Entradas e Pesos Iniciais
y_i = 0.5  # Saída de um neurônio da camada anterior
peso_w_ji = 0.8
# Cálculo do somador e ativação (ex: Sigmoide)
v_j = y_i * peso_w_ji
y_j = 1 / (1 + np.exp(-v_j))

# --- CÁLCULO DO ERRO ---
d_j = 1.0  # Valor desejado (gabarito)
erro_j = d_j - y_j

# --- 2. FASE PARA TRÁS (BACKWARD) ---
# Derivada da Sigmoide: y_j * (1 - y_j)
derivada_j = y_j * (1 - y_j)

# Gradiente Local (considerando j como camada de saída)
delta_j = erro_j * derivada_j

# Ajuste do Peso (Regra Delta Generalizada)
delta_w = eta * delta_j * y_i
novo_peso = peso_w_ji + delta_w

print(f"Erro na Saída: {erro_j:.4f}")
print(f"Ajuste a ser feito no peso: {delta_w:.4f}")
print(f"Peso Atualizado: {novo_peso:.4f}")