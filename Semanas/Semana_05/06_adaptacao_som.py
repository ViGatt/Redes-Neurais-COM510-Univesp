import numpy as np

# 1. Parâmetros simulados
x = np.array([0.8, 0.2])       # Vetor do padrão de entrada
w = np.array([0.5, 0.5])       # Vetor de pesos atual do neurônio (vencedor ou vizinho)
taxa_aprendizado = 0.1         # O quão rápido a rede aprende (eta)
funcao_vizinhanca = 1.0        # Fator de vizinhança (1.0 se for o próprio BMU)

# 2. ADAPTAÇÃO SINÁPTICA: Regra de Kohonen
# Fórmula: W(t+1) = W(t) + eta * h(t) * (x - W(t))
w_novo = w + taxa_aprendizado * funcao_vizinhanca * (x - w)

print(f"Vetor de Pesos Antigo: {w}")
print(f"Padrão de Entrada:     {x}")
print(f"Vetor de Pesos Novo:   {w_novo}")
# Note como o novo peso se aproximou dos valores [0.8, 0.2]