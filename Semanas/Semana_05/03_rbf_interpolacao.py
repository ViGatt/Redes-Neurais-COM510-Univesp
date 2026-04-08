import numpy as np
from scipy.interpolate import RBFInterpolator
import matplotlib.pyplot as plt

# 1. Dados ruidosos de uma função seno
x_treino = np.linspace(0, 10, 10).reshape(-1, 1)
y_treino = np.sin(x_treino).ravel()

# 2. Criando o Interpolador RBF (Simulando a rede)
# O kernel 'gaussian' é o padrão teórico visto em aula
rbf = RBFInterpolator(x_treino, y_treino, kernel='gaussian', epsilon=1.0)

# 3. Predição em novos pontos
x_novo = np.linspace(0, 10, 100).reshape(-1, 1)
y_predito = rbf(x_novo)

plt.scatter(x_treino, y_treino, color='red', label='Dados Reais')
plt.plot(x_novo, y_predito, label='Aproximação RBF')
plt.legend()
plt.title("Interpolação com Rede RBF")
plt.show()