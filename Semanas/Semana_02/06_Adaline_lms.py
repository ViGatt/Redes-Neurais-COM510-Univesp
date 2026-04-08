import numpy as np

class Adaline:
    def __init__(self, n_entradas, taxa_aprendizado=0.01):
        self.w = np.zeros(n_entradas + 1) # Pesos + Bias
        self.eta = taxa_aprendizado

    def soma_linear(self, x):
        return np.dot(x, self.w[1:]) + self.w[0]

    def prever(self, x):
        # Para classificar no final, usamos uma função degrau
        return 1 if self.soma_linear(x) >= 0 else -1

    def treinar(self, X, d, epocas=50):
        custos = []
        for _ in range(epocas):
            # No Adaline, o erro é calculado na saída linear
            saida_linear = self.soma_linear(X)
            erros = (d - saida_linear)
            
            # Atualização dos pesos (Regra Delta)
            self.w[1:] += self.eta * X.T.dot(erros)
            self.w[0] += self.eta * erros.sum()
            
            custo = (erros**2).sum() / 2.0
            custos.append(custo)
        return custos

# Exemplo de uso
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
d = np.array([-1, -1, 1, 1]) # Classes -1 e 1

modelo = Adaline(n_entradas=2)
modelo.treinar(X, d)
print(f"Pesos finais: {modelo.w}")