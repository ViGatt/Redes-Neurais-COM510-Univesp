# Semana 02: Perceptron, Adaline e Otimização Linear

Nesta seção, exploramos os modelos fundamentais que deram origem ao campo da aprendizagem supervisionada e os métodos matemáticos para ajuste de pesos.

## 1. O Perceptron de Rosenblatt (Seção 3.1 e 3.2)
>S2 - Texto-base 4 – Redes Neurais: princípios e prática (Leia Capítulo 3 - Seções 3.1, 3.2, 3.3 - páginas 147-149, e Seções 3.5, 3.6, 3.7 e 3.8) | Simon Haykin 

Proposto por Frank Rosenblatt em 1958, é o modelo mais simples de rede neural para classificação de padrões **linearmente separáveis**.

* **Estrutura:** Composto por um único neurônio com pesos ajustáveis e um bias.
* **Finalidade:** Decidir se um padrão de entrada pertence a uma de duas classes ( $C_1$ ou $C_2$ ).
* **Teorema de Convergência:** Se as classes forem linearmente separáveis (puderem ser divididas por um hiperplano), o algoritmo do Perceptron convergirá para uma solução em um número finito de passos.

---

## 2. Método da Descida mais Íngreme (Steepest Descent - Seção 3.3)

É o motor matemático por trás de quase todos os algoritmos de treinamento.

* **Conceito:** Ajustar os pesos na direção oposta ao vetor gradiente $\nabla E(w)$ (a direção de maior subida da função de erro).
* **Equação de Ajuste:**

$$w(n+1) = w(n) - \eta g(n)$$

Onde $\eta$ (eta) é a **taxa de aprendizado**.
* **Comportamento da Taxa ($\eta$):**
* *$\eta$* pequeno: Convergência lenta e suave (sobreamortecida).
* *$\eta$* grande: Convergência rápida, mas corre o risco de instabilidade ou oscilação (subamortecida).

## 3. O Modelo Adaline e a Regra Delta (Seções 3.5 a 3.8)

O **Adaline** (*Adaptive Linear Element*) diferencia-se do Perceptron pelo seu critério de erro.

* **Diferença Fundamental:** No Perceptron, o erro é calculado após a função de ativação (degrau). No Adaline, o erro é calculado com base na saída **linear** (antes da função de ativação).
* **Função de Custo:** Utiliza o Erro Quadrático Médio (MSE).
* **Algoritmo LMS (Widrow-Hoff):** Também conhecido como Regra Delta. Ele busca minimizar o erro médio através de ajustes contínuos.

| Característica | Perceptron | Adaline |
| --- | --- | --- |
| **Saída para Treino** | Discreta (0 ou 1) | Contínua (Linear) |
| **Aprendizagem** | Regra do Perceptron | Regra Delta (LMS) |
| **Objetivo** | Classificação | Minimização do Erro Quadrático |


---

## Resumo 

1. **Linearmente Separável:** Significa que você pode desenhar uma linha (ou plano) que separa perfeitamente as classes.
2. **Taxa de Aprendizado ($\eta$):** Controla a "velocidade" e a "estabilidade" do treino.
3. **Hiperplano de Decisão:** É a fronteira onde a soma ponderada é exatamente zero.
4. **Adaline:** Foca na minimização do erro quadrático, sendo o precursor das redes neurais modernas que usam gradiente descendente.