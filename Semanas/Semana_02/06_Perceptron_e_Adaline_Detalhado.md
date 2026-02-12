# Semana 02: Evolução dos Modelos - Perceptron e Adaline

Nesta aula, exploramos como saímos de uma configuração manual de pesos para um sistema que aprende através da minimização do erro.

## 1. Do MCP ao Perceptron

O neurônio de McCulloch-Pitts (MCP) era capaz de implementar funções lógicas (AND, OR), mas os pesos precisavam ser definidos manualmente pelo projetista. O **Perceptron** automatiza isso.

* **O Problema da Separação:** O Perceptron funciona como um classificador linear. Ele busca encontrar um **hiperplano** que separe duas classes no espaço de atributos.
* **Limitação:** Só converge se as classes forem **linearmente separáveis**. Se os dados estiverem misturados de forma que nenhuma linha reta possa separá-los (como no problema do XOR), o Perceptron falhará.

---

## 2. O Modelo Adaline (Adaptive Linear Element)

O Adaline introduz uma mudança sutil, mas revolucionária, na forma como o erro é calculado, servindo de base para as redes neurais modernas.

### Diferença na Saída ($y$):

* **Perceptron:** O erro é calculado após a função de ativação degrau ($e = d - \text{degrau}(u)$).
* **Adaline:** O erro é calculado com a saída **linear** antes da ativação ($e = d - u$). Isso permite usar o **Gradiente Descendente**.

### A Regra Delta (Regra de Widrow-Hoff / LMS)

O objetivo é minimizar o Erro Quadrático Médio (MSE). O ajuste do peso  é proporcional ao negativo do gradiente do erro:

Onde:

$$\Delta w_{ki} = \eta (d_k - y_k) x_i$$

*  $\eta$(eta): Taxa de aprendizagem.
* ($(d_k - y_k)$): Sinal de erro.
* $x_i$: Valor da entrada.

---

## 3. Gradiente Descendente Estocástico vs. Batch

A aula também toca na forma como atualizamos os pesos:

* **Batch:** Calcula o erro para todo o conjunto de dados antes de atualizar os pesos.
* **Estocástico (SGD):** Atualiza os pesos para cada exemplo individualmente. É mais rápido e ajuda a evitar mínimos locais em problemas complexos.

---

## Checkpoint 

* **Qual modelo usa o erro linear?** Adaline.
* **O que acontece se a taxa de aprendizado ($\eta$) for muito alta no Adaline?** O algoritmo pode oscilar e divergir, nunca encontrando o mínimo da função de erro.
* **Diferença de Saída:** Perceptron tem saída discreta (binária) durante o treino; Adaline tem saída contínua (linear) durante o treino.

---