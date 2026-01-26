# Simulação simplificada da Regra Delta (Correção de Erro)
import numpy as np

# Configurações iniciais
entrada = 2.0
valor_desejado = 10.0
peso = 0.5  # Começamos com um peso aleatório/baixo
taxa_aprendizado = 0.1

print(f"Alvo: {valor_desejado} | Início com Peso: {peso}")

for epoca in range(1, 11):
    saida_atual = entrada * peso
    erro = valor_desejado - saida_atual
    
    # Ajuste do peso: delta_w = n * erro * entrada
    peso = peso + (taxa_aprendizado * erro * entrada)
    
    print(f"Época {epoca}: Saída = {saida_atual:.2f} | Novo Peso = {peso:.2f}")

print(f"\nResultado Final: {entrada * peso:.2f} (Próximo de {valor_desejado})")