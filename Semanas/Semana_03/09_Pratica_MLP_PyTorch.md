# 💻 Semana 03: Implementação Prática de Redes MLP (PyTorch)

Esta videoaula demonstra como desenvolver, treinar e avaliar um Perceptron de Múltiplas Camadas para os dois principais tipos de problemas em Aprendizado de Máquina: **Classificação** e **Regressão**[cite: 1, 2, 3].

## 1. O Ambiente e a Stack de Tecnologias
O código é desenvolvido na nuvem utilizando o **Google Colab**[cite: 3]. A "stack" de bibliotecas em Python envolve:
* **PyTorch (`torch` e `torch.nn`):** O framework central de Deep Learning para criação da rede, otimização e cálculo dinâmico de gradientes[cite: 1].
* **Scikit-Learn (`sklearn`):** Usada para manipulação de dados, como a divisão de conjuntos (`train_test_split`) e normalização (`MinMaxScaler`)[cite: 1].
* **Pandas & Numpy:** Para estruturação tabular e operações matriciais[cite: 1].
* **Matplotlib & Seaborn:** Para a visualização dos dados e das curvas de erro durante o treinamento[cite: 1].

---

## 2. Caso Prático 1: Problema de Classificação
Na classificação, a rede neural tenta prever uma **categoria discreta** (uma classe).

* **A Base de Dados (Iris Dataset):** O exemplo clássico da área. Contém 150 exemplos de flores separadas em 3 classes (Setosa, Versicolor e Virginica) baseadas em 4 atributos físicos (largura e comprimento de pétalas e sépalas)[cite: 1].
* **Estrutura da Rede:**
    * **Entrada:** 4 neurônios (um para cada atributo da flor).
    * **Ocultas:** Neurônios com funções de ativação não lineares (como ReLU).
    * **Saída:** 3 neurônios (um para cada classe). A saída passa por uma ativação tipo **Softmax**, que converte os valores brutos em probabilidades (a classe com a maior probabilidade é a escolhida).
* **Função de Custo:** A mais comum para classificação multiclasse é a Entropia Cruzada (`CrossEntropyLoss`).

---

## 3. Caso Prático 2: Problema de Regressão
Na regressão, o objetivo da rede é prever um **valor numérico contínuo**. O código do professor simula a tentativa de a rede aprender o padrão de uma onda senoidal ruidosa ($y = \sin(x) + \text{ruído} + 0.5x$)[cite: 2].

* **Estrutura da Rede:**
    * **Entrada:** 1 neurônio (representando a variável $x$).
    * **Ocultas:** Responsáveis por curvar o espaço e se adaptar às subidas e descidas do seno.
    * **Saída:** 1 neurônio **sem função de ativação restritiva** (ou com ativação puramente linear), pois o valor previsto pode ser qualquer número real ($3.14$, $-5.2$, etc.).
* **Função de Custo:** Diferente da classificação, aqui a rede é avaliada utilizando o Erro Quadrático Médio (`MSELoss` - *Mean Squared Error*)[cite: 2]. O otimizador de Gradiente Descendente Estocástico (`SGD`) busca minimizar esse valor[cite: 2].

---

## 💻 Laboratório: O Esqueleto PyTorch no VS Code


```python
import torch
import torch.nn as nn

# 1. Definindo a arquitetura herdando de nn.Module
class MinhaRedeMLP(nn.Module):
    def __init__(self, entradas, ocultos, saidas):
        super(MinhaRedeMLP, self).__init__()
        # Definindo as conexões (Camadas Densas/Lineares)
        self.camada_oculta = nn.Linear(entradas, ocultos)
        self.ativacao = nn.ReLU() # Quebra da linearidade
        self.camada_saida = nn.Linear(ocultos, saidas)

    # 2. O Método Forward define a Fase para Frente (Fluxo de Sinal)
    def forward(self, x):
        x = self.camada_oculta(x)
        x = self.ativacao(x)
        x = self.camada_saida(x)
        return x

# 3. Instanciando o modelo (Exemplo: 4 entradas, 10 na camada oculta, 3 saídas)
modelo = MinhaRedeMLP(entradas=4, ocultos=10, saidas=3)

# 4. Configurações para Fase de Retorno (Backpropagation)
# Função de erro para regressão (MSE) e Otimizador (SGD)
criterio_erro = nn.MSELoss()
otimizador = torch.optim.SGD(modelo.parameters(), lr=0.01)

print(modelo)
```

---

## Checkpoint (Revisão da Semana 03)
* **Classes (`nn.Module`):** Toda rede construída no PyTorch é uma classe que obrigatoriamente implementa o método `forward()`. O *Backpropagation* (fase para trás) é calculado de forma automática pela ferramenta (`Autograd`).
* **Tensores (`torch.FloatTensor`):** O PyTorch não trabalha diretamente com listas do Python ou matrizes do Pandas na hora de processar os pesos. Os dados devem ser convertidos para **Tensores**, que são estruturas matematicamente otimizadas (e que podem rodar em placas de vídeo - GPUs)[cite: 2].
* **Classificação vs. Regressão:** Se o problema quer saber *o que é* (flor Setosa ou Virginica), é classificação. Se quer saber *quanto é* (uma temperatura ou valor financeiro), é regressão.

