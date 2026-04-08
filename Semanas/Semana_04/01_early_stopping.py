import numpy as np

# Variáveis de controle para o Early Stopping
melhor_erro_validacao = float('inf')
epocas_sem_melhoria = 0
paciencia = 5  # Quantas épocas esperar antes de parar

epocas = 100
for epoca in range(epocas):
    # 1. Treinamento (Atualização de pesos)
    # erro_treino = modelo.treinar(X_train, y_train)
    
    # 2. Validação (Sem atualizar pesos, apenas calcula o erro)
    # erro_validacao = modelo.avaliar(X_val, y_val)
    
    # Simulando erros para o exemplo
    erro_treino = 1.0 / (epoca + 1)
    erro_validacao = 1.0 / (epoca + 1) if epoca < 20 else (epoca - 20) * 0.05 + 0.05
    
    # 3. Lógica do Early Stopping
    if erro_validacao < melhor_erro_validacao:
        melhor_erro_validacao = erro_validacao
        epocas_sem_melhoria = 0
        # Aqui você salvaria os pesos do modelo!
        # torch.save(modelo.state_dict(), 'melhor_modelo.pth')
    else:
        epocas_sem_melhoria += 1
        
    if epocas_sem_melhoria >= paciencia:
        print(f"🛑 EARLY STOPPING acionado na época {epoca}!")
        print(f"Melhor erro de validação salvo: {melhor_erro_validacao:.4f}")
        break # Interrompe o treinamento