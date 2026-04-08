import numpy as np

# Uma função de custo fictícia (parábola simples: f(x) = x^2)
def derivada_custo(x):
    return 2 * x

def gradiente_descendente(x_inicial, eta, epocas):
    x = x_inicial
    print(f"--- Taxa de Aprendizagem: {eta} ---")
    for i in range(epocas):
        grad = derivada_custo(x)
        x = x - (eta * grad)
        print(f"Época {i+1}: Posição = {x:.4f}")
    return x

# Teste 1: Taxa ideal
gradiente_descendente(x_inicial=10, eta=0.1, epocas=5)

# Teste 2: Taxa muito alta (Divergência)
print("\nCUIDADO: O valor vai explodir!")
gradiente_descendente(x_inicial=10, eta=1.1, epocas=5)