import numpy as np

# Hiperparâmetros
eta = 0.1      # Taxa de aprendizagem
alfa = 0.9     # Termo de momento (0.0 significa sem momento)

# Variáveis do neurônio
peso_atual = 0.5
delta_w_anterior = 0.0  # Na primeira iteração, não há momento

# Simulando 5 épocas de treinamento com gradientes hipotéticos
gradientes = [0.2, 0.2, -0.1, 0.15, 0.1] 

print("Época | Gradiente | Delta W | Novo Peso")
print("-" * 40)

for epoca, gradiente_local in enumerate(gradientes):
    # Calculo do termo principal (simplificado aqui como gradiente_local)
    # Na real seria: eta * delta * entrada
    termo_gradiente = eta * gradiente_local 
    
    # A MÁGICA DO MOMENTO AQUI:
    delta_w_atual = (alfa * delta_w_anterior) + termo_gradiente
    
    # Atualiza o peso
    peso_atual += delta_w_atual
    
    print(f"  {epoca+1}   |   {gradiente_local:>5.2f}   |  {delta_w_atual:>5.4f} |  {peso_atual:>5.4f}")
    
    # Prepara para a próxima iteração
    delta_w_anterior = delta_w_atual