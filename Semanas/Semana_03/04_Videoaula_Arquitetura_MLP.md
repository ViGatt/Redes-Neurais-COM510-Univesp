Para consolidar a videoaula que demonstra o funcionamento interno do MLP (especialmente a resolução do clássico problema XOR), crie o arquivo `Semanas/Semana_03/04_Videoaula_Arquitetura_MLP.md` no seu VS Code.

Aqui estão as anotações estruturadas e com os destaques matemáticos:

---

# 🏗️ Semana 03: A Arquitetura da Rede Multilayer Perceptron (MLP)

Esta aula foca em mostrar visualmente por que as redes de camada única falham em certos problemas e como o MLP contorna essa limitação criando novas representações matemáticas.

## 1. As Limitações dos Modelos Lineares (O Problema XOR)

Os modelos baseados em um único neurônio (como o Perceptron simples) criam apenas **uma fronteira de separação linear** (uma linha reta num gráfico 2D, ou um hiperplano).

* **O Problema XOR (Ou-Exclusivo):** É o exemplo clássico de um problema que não pode ser resolvido com uma única linha reta.
    * Entradas iguais `(0,0)` ou `(1,1)` $\rightarrow$ Saída `0`
    * Entradas diferentes `(0,1)` ou `(1,0)` $\rightarrow$ Saída `1`
* Como os pontos estão dispostos de forma cruzada, é impossível traçar uma única reta que separe as classes perfeitamente.

---

## 2. Redes com Múltiplas Camadas e a Não-Linearidade

Para superar a barreira da linearidade, empilhamos camadas de neurônios. No entanto, a aula destaca uma regra matemática fundamental: **adicionar camadas só funciona se utilizarmos funções de ativação não-lineares.**

### O Colapso Linear
Se você colocar dois neurônios lineares em sequência:
1.  Camada 1: $y_1 = x_1 \cdot w_1$
2.  Camada 2: $y_2 = y_1 \cdot w_2$

Substituindo, temos $y_2 = x_1 \cdot (w_1 \cdot w_2)$. Como a multiplicação de dois pesos resulta em apenas um terceiro peso (um $w_{equivalente}$), a rede inteira "colapsou" e voltou a ser matematicamente igual a um único neurônio linear. 

---

## 3. A Solução do XOR (A Mágica da Camada Oculta)

A aula demonstra a solução do XOR usando uma arquitetura com 2 neurônios na camada oculta (N1, N2) e 1 neurônio na camada de saída (N3).

* **N1 (Neurônio Oculto 1):** Pode ser configurado (através dos pesos) para agir como uma porta lógica **AND** (só dispara se ambas as entradas forem 1).
* **N2 (Neurônio Oculto 2):** Pode ser configurado para agir como uma porta lógica **OR** (dispara se qualquer entrada for 1).
* **N3 (Neurônio de Saída):** Recebe as saídas de N1 e N2 e toma a decisão final.

> **O que a rede MLP realmente faz?**
> A função das camadas ocultas é **transformar o problema original** (não-linearmente separável) em uma nova representação num espaço diferente, onde a camada de saída consiga resolvê-lo traçando uma simples linha reta. As camadas ocultas funcionam como extratoras de características.

---

## 4. Revisão das Funções de Ativação

A aula retoma o catálogo de funções que garantem a quebra da linearidade:
* **Degrau (Heaviside):** Retorna 0 ou 1.
* **Sigmoide Logística:** Transforma a saída do somador em um valor contínuo entre $0$ e $1$.
* **Tangente Hiperbólica:** Similar à sigmoide, mas o intervalo de saída é de $-1$ a $1$.
* **ReLU:** Zera os valores negativos e mantém os positivos intactos.
* **Softmax:** Converte um vetor de saídas em uma **distribuição de probabilidade** (a soma de todas as saídas será 1). Muito usada na última camada para problemas com múltiplas classes.

---

## 💻 Laboratório: O MLP resolvendo o XOR no Python


```python
import numpy as np
from sklearn.neural_network import MLPClassifier

# Tabela Verdade do XOR
X = np.array([[0, 0], 
              [0, 1], 
              [1, 0], 
              [1, 1]])

# Saídas esperadas (Classes)
y = np.array([0, 1, 1, 0])

# Criando a rede MLP (1 camada oculta com 4 neurônios, ativação não-linear ReLU)
# max_iter=2000 garante que o algoritmo tenha tempo para convergir
mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=2000, random_state=42)

# Treinamento (Backpropagation acontecendo internamente)
mlp.fit(X, y)

# Testando as predições
print("--- Teste do Problema XOR com MLP ---")
for entrada in X:
    previsao = mlp.predict([entrada])
    print(f"Entrada: {entrada} -> Previsão do MLP: {previsao[0]}")
```

---

## Checkpoint
1. **O que acontece se uma rede com várias camadas usar apenas ativação linear?** Ela se comporta exatamente como uma rede de camada única.
2. **Qual é o papel da camada oculta?** Mapear os dados de entrada para um novo espaço (uma nova dimensão) onde eles se tornem linearmente separáveis pela camada de saída.
3. **O que é Softmax?** Uma função de ativação focada em gerar distribuições de probabilidade para classificação multiclasse.