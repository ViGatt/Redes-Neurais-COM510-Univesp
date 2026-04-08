import numpy as np
import matplotlib.pyplot as plt

def rbf_gaussiana(distancia, sigma):
    return np.exp(-(distancia**2) / (2 * sigma**2))

# Simulando uma entrada se movendo em relação a um neurônio posicionado no zero
distancias = np.linspace(-5, 5, 100)
ativacao = rbf_gaussiana(distancias, sigma=1.0)

plt.plot(distancias, ativacao)
plt.title("Ativação de um Neurônio RBF (Gaussiana)")
plt.xlabel("Distância do Centro")
plt.ylabel("Intensidade da Resposta")
plt.grid(True)
plt.show()