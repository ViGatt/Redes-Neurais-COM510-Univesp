
# 👨‍💻 Semana 03: Códigos de Apoio (Explicação Detalhada)

Neste documento, dissecamos os exemplos práticos disponibilizados no Google Colab para entender exatamente o que cada linha do PyTorch faz nos bastidores.

## Parte 1: MLP para Classificação (Base Iris)

Neste exemplo, a rede recebe 4 medidas de uma flor (pétala e sépala) e tenta classificar qual das 3 espécies ela é.

### Código Completo 
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# 1. CARREGAMENTO E PREPARAÇÃO DOS DADOS
dados_iris = load_iris()
X = dados_iris.data   # As 4 características (entradas)
y = dados_iris.target # As 3 classes (0, 1 ou 2)

# Normalização (MinMaxScaler): Coloca todos os valores entre 0 e 1.
# Isso ajuda a rede a aprender mais rápido e não dar peso excessivo a valores grandes.
scaler = MinMaxScaler()
X_normalizado = scaler.fit_transform(X)

# Divisão: 80% para treino, 20% para teste
X_train, X_test, y_train, y_test = train_test_split(X_normalizado, y, test_size=0.2, random_state=42)

# CONVERSÃO PARA TENSORES DO PYTORCH
# PyTorch não entende arrays do numpy, precisamos converter para Tensors.
# FloatTensor para entradas (números quebrados) e LongTensor para as classes (números inteiros).
X_train_t = torch.FloatTensor(X_train)
X_test_t = torch.FloatTensor(X_test)
y_train_t = torch.LongTensor(y_train)
y_test_t = torch.LongTensor(y_test)

# 2. DEFINIÇÃO DA ARQUITETURA DA REDE
class RedeClassificacao(nn.Module):
    def __init__(self):
        super(RedeClassificacao, self).__init__()
        # Camada Oculta: 4 entradas -> 10 neurônios ocultos
        self.camada_oculta = nn.Linear(4, 10) 
        # Camada de Saída: 10 neurônios ocultos -> 3 saídas (as 3 classes)
        self.camada_saida = nn.Linear(10, 3)

    def forward(self, x):
        # Passa os dados pela camada oculta e aplica a função ReLU (quebra de linearidade)
        x = F.relu(self.camada_oculta(x))
        # Passa pela camada de saída (sem ativação extra aqui, o PyTorch faz isso na função de perda)
        x = self.camada_saida(x)
        return x

modelo = RedeClassificacao()

# 3. CONFIGURAÇÃO DO TREINAMENTO
# CrossEntropyLoss: É a função de custo padrão para classificação. 
# Internamente ela já aplica a função Softmax nas saídas!
criterio = nn.CrossEntropyLoss()

# Otimizador Adam: Uma versão mais moderna e inteligente do Gradiente Descendente Estocástico (SGD).
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.01)

# 4. LOOP DE TREINAMENTO (O BACKPROPAGATION NA PRÁTICA)
epocas = 100
for epoca in range(epocas):
    # a) Fase Forward (Para frente): Calcula a predição da rede
    y_predito = modelo(X_train_t)
    
    # b) Cálculo do Erro (Loss)
    erro = criterio(y_predito, y_train_t)
    
    # c) Fase Backward (Retropropagação)
    otimizador.zero_grad() # Limpa os gradientes da rodada anterior (obrigatório no PyTorch)
    erro.backward()        # Calcula a derivada do erro para cada peso (Regra da Cadeia)
    otimizador.step()      # Atualiza os pesos (Dá o "passo" do gradiente descendente)

print("Treinamento de Classificação Concluído!")
```



### Pontos Chaves do Código 1:
* `torch.LongTensor`: A função `CrossEntropyLoss` exige que os "gabaritos" (labels) sejam tensores do tipo Long (inteiros puros), pois ela usa isso como índice das classes.
* `otimizador.zero_grad()`: O PyTorch acumula gradientes por padrão. Se você não zerar a cada época, ele vai somar o erro da época atual com o da época anterior, o que fará os pesos divergirem loucamente.

---

## Parte 2: MLP para Regressão (Função Senoidal)

Neste exemplo, a rede não quer descobrir "o que é" um dado, mas sim "quanto vale". Ela tenta aprender a desenhar uma onda baseada na matemática do seno com um pouco de ruído inserido.

### Código Completo 
```python
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 1. GERAÇÃO DOS DADOS (CRIANDO O PROBLEMA)
# Criando um eixo X de 0 a 7 pulando de 0.05 em 0.05
X = np.arange(0, 7, 0.05).reshape(-1, 1) 
# Criando o eixo Y baseado numa função Seno + Ruído aleatório + Inclinação (0.5*X)
y = np.sin(X) + 0.3 * np.random.randn(X.shape[0], 1) + 0.5 * X

# Divisão de Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# CONVERSÃO PARA TENSORES
# Como é regressão, TANTO as entradas quanto as saídas são números contínuos (FloatTensor)
X_train_t = torch.FloatTensor(X_train)
y_train_t = torch.FloatTensor(y_train)

# 2. DEFINIÇÃO DA ARQUITETURA DA REDE
class RedeRegressao(nn.Module):
    def __init__(self):
        super(RedeRegressao, self).__init__()
        # 1 entrada (valor do eixo X) -> 50 neurônios na camada oculta
        self.densa1 = nn.Linear(1, 50)
        # 50 neurônios ocultos -> 1 saída (valor previsto para o eixo Y)
        self.densa2 = nn.Linear(50, 1)

    def forward(self, x):
        # A ativação Tanh ou ReLU curva a reta para que a rede consiga desenhar o formato do Seno
        x = torch.tanh(self.densa1(x))
        # Saída PURAMENTE LINEAR: Na regressão não podemos amassar a saída entre 0 e 1.
        x = self.densa2(x)
        return x

modelo_reg = RedeRegressao()

# 3. CONFIGURAÇÃO DO TREINAMENTO
# MSELoss (Mean Squared Error): Erro Quadrático Médio. Padrão ouro para regressão!
criterio_reg = nn.MSELoss()

# Otimizador SGD (Gradiente Descendente Estocástico)
otimizador_reg = torch.optim.SGD(modelo_reg.parameters(), lr=0.01)

# 4. LOOP DE TREINAMENTO
epocas = 1000 # Regressões complexas costumam precisar de mais épocas
for epoca in range(epocas):
    # Forward Pass
    y_predito = modelo_reg(X_train_t)
    
    # Cálculo do Erro (Diferença quadrática entre o previsto e a linha real do seno)
    erro = criterio_reg(y_predito, y_train_t)
    
    # Backward Pass (Retropropagação)
    otimizador_reg.zero_grad()
    erro.backward()
    otimizador_reg.step()

print("Treinamento de Regressão Concluído!")
```

### Pontos Chaves do Código 2:
* **A Saída Linear:** Veja que no `forward` da regressão, o `self.densa2(x)` retorna o valor puro. Se colocássemos uma Sigmoide ali, a rede nunca conseguiria prever valores maiores que 1 ou menores que 0, e nosso eixo Y do seno ultrapassa esses limites.
* **A Função de Custo `MSELoss`:** Em vez de verificar se o modelo "acertou a classe", o `MSE` mede literalmente a distância geométrica entre o ponto que a rede previu e onde o ponto real deveria estar.

---

## 💡 Resumo Definitivo: Classificação vs. Regressão no PyTorch

Para o seu dia a dia de desenvolvedor e para a prova, guarde esta regra de ouro:

| Característica | Problema de Classificação | Problema de Regressão |
| :--- | :--- | :--- |
| **Camada de Saída** | Quantidade de neurônios = Número de classes | Apenas 1 neurônio |
| **Ativação Final** | Softmax (embutida no `CrossEntropyLoss`) | Nenhuma (Linear) |
| **Função de Erro (Loss)** | `nn.CrossEntropyLoss()` | `nn.MSELoss()` |
| **Tipo do Tensor (Alvo)** | Inteiro (`torch.LongTensor`) | Ponto Flutuante (`torch.FloatTensor`) |

---