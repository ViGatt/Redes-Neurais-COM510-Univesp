# 🧬 Semana 01: O Neurônio Biológico e sua Modelagem Matemática

Esta seção detalha como traduzimos impulsos eletroquímicos em operações de álgebra linear.

## 1. O Modelo do Neurônio (Haykin 1.2)

Um neurônio artificial é composto por três elementos básicos e um ajuste externo (Bias).

### Os Três Elementos Básicos

1. **Conjunto de Sinapses (Pesos):** Cada sinal de entrada  é multiplicado por um peso .
* *Nota:* Um peso positivo é **excitatório**, um negativo é **inibitório**.


2. **Junção Somadora:** Um somador linear que agrega os sinais de entrada ponderados.
3. **Função de Ativação ($\phi$):** Limita a amplitude da saída do neurônio. Também chamada de função de esmagamento (*squashing function*).

### O Papel do Bias ($b_k$)

O bias tem o efeito de aumentar ou diminuir a entrada líquida da função de ativação, dependendo se é positivo ou negativo.

* **Matematicamente:** Ele "desloca" a função de ativação para a esquerda ou para a direita no eixo .
* **Equação do Potencial de Ativação ($v_k$):**

$$v_k = \sum_{j=1}^{m} w_{kj} x_j + b_k$$

---

## 2. Funções de Ativação Comuns

A escolha da função determina como o neurônio "responde" aos estímulos. As principais citadas por Haykin são:

| Função | Equação | Comportamento |
| --- | --- | --- |
| **Degrau (Threshold)** | $\phi(v) = 1 \text{ se } v \geq 0; \text{ senão } 0$ | Saída binária (0 ou 1). Modelo original de McCulloch-Pitts. |
| **Sigmoide (Logística)** | $\phi(v) = \frac{1}{1 + \exp(-v)}$ | Saída entre 0 e 1. Útil para probabilidades. |
| **Tangente Hiperbólica** | $\phi(v) = \tanh(v)$ | Saída entre -1 e 1. Frequentemente preferida à sigmoide em redes profundas. |

---

## 3. Redes Neurais como Grafos Direcionados (Haykin 1.3)

Haykin introduz a visão da rede como um **Grafo de Fluxo de Sinais**. Isso é fundamental para entender como os dados se propagam:

* **Nós:** Representam os neurônios ou pontos de entrada.
* **Arcos (Arestas):** Representam as conexões sinápticas.
* **Fluxo:** O sinal sempre flui em uma direção (da entrada para a saída) em redes *feedforward*.

> **Conceito de Engenharia:** Um neurônio pode ser visto como um operador matemático que transforma um vetor de entrada  em um escalar de saída .

---

## 📝 Checkpoint para o Quiz

* **Diferença entre $u_k$ e $v_k$:** No livro de Haykin,  é a soma linear ($\sum w x$), enquanto $v_k$ é o potencial de ativação já somado ao bias ($u_k + b_k$).
* **Linearidade:** O somador é uma operação **linear**. O que traz a capacidade de aprender padrões complexos para a rede é a **não-linearidade** da função de ativação.
* **Sinapses Inibitórias:** Identificadas por pesos negativos ($w < 0$).