import numpy as np

def neuronio_estocastico(v, T):
    if T == 0: # Caso determinístico
        return 1 if v >= 0 else -1
    
    # Probabilidade de disparo P(v)
    prob_disparo = 1 / (1 + np.exp(-v / T))
    
    # Decisão baseada na probabilidade
    return 1 if np.random.random() < prob_disparo else -1

# Teste com diferentes temperaturas
v_campo = 0.2
for temp in [0.01, 1.0, 5.0]:
    resultados = [neuronio_estocastico(v_campo, temp) for _ in range(10)]
    print(f"Temp {temp}: {resultados}")