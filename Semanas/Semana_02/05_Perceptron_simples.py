import numpy as np

class Perceptron:
    def __init__(self, entradas, taxa_aprendizado=0.1):
        self.pesos = np.zeros(entradas + 1) # +1 para o bias
        self.eta = taxa_aprendizado

    def predict(self, x):
        # Soma ponderada + bias
        u = np.dot(x, self.pesos[1:]) + self.pesos[0]
        # Função de ativação degrau
        return 1 if u > 0 else 0

    def treinar(self, X, d, epocas=10):
        for _ in range(epocas):
            for xi, alvo in zip(X, d):
                previsao = self.predict(xi)
                erro = alvo - previsao
                # Ajuste dos pesos e bias (Regra do Perceptron)
                self.pesos[1:] += self.eta * erro * xi
                self.pesos[0] += self.eta * erro

# Teste com a porta lógica OR (Linearmente Separável)
X = np.array([[0,0], [0,1], [1,0], [1,1]])
d = np.array([0, 1, 1, 1])

modelo = Perceptron(entradas=2)
modelo.treinar(X, d)

print("Teste Porta OR:")
for teste in X:
    print(f"Entrada {teste} -> Saída: {modelo.predict(teste)}")