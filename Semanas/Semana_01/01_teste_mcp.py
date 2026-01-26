# Simulação simples de um neurônio artificial (Modelo MCP)
import numpy as np

def neuronio_mcp(entradas, pesos, limiar):
    # Cálculo do campo local induzido (soma ponderada)
    u = np.dot(entradas, pesos)
    
    # Função de ativação degrau (Step Function)
    return 1 if u >= limiar else 0

# Exemplo: Porta Lógica AND (E)
pesos = np.array([0.5, 0.5])
limiar = 1.0

print(f"Entrada (1,1): {neuronio_mcp([1,1], pesos, limiar)}") # Dispara (1)
print(f"Entrada (1,0): {neuronio_mcp([1,0], pesos, limiar)}") # Não dispara (0)