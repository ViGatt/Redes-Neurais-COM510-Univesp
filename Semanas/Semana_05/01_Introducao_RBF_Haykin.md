# 🎯 Semana 05: Introdução às Redes RBF (Haykin 5.1 - 5.3)
> S5 - Texto-base 1 – Redes Neurais: princípios e prática (Seções 5.1 até 5.3) | Simon Haykin

As Redes RBF (Radial Basis Function) tratam o aprendizado de máquina não como um ajuste de pesos em camadas sucessivas, mas como um **problema de interpolação em um espaço de alta dimensão**.

## 1. Introdução e Filosofia (Seção 5.1)

Diferente da MLP, que é inspirada no processamento de sinais biológicos, a rede RBF tem raízes profundas na análise numérica clássica. 
* **Abordagem:** A rede projeta os padrões de entrada em um espaço oculto de alta dimensão de forma **não-linear**.
* **O objetivo:** Transformar um problema que não é linearmente separável em um espaço de baixa dimensão em um problema que **é** linearmente separável em um espaço de dimensão superior.



---

## 2. Teorema de Cover sobre a Separabilidade (Seção 5.2)

Este é o fundamento teórico que justifica por que as RBFs funcionam. O **Teorema de Cover** afirma que:
> Um problema de classificação de padrões fundado em um espaço de alta dimensão é mais provável de ser linearmente separável do que em um espaço de baixa dimensão, desde que a transformação seja não-linear.

### Os Dois Passos da Rede RBF:
1. **Transformação Não-Linear (Camada Oculta):** Os dados são mapeados para um espaço de alta dimensão usando funções radiais (como a Gaussiana). Não há pesos treináveis aqui no sentido tradicional; o que importa é a distância do dado para o "centro" de cada função.
2. **Separação Linear (Camada de Saída):** Uma vez no espaço de alta dimensão, o problema torna-se simples o suficiente para ser resolvido com uma combinação linear (uma simples soma ponderada), similar ao que o Adaline faz.



---

## 3. O Problema da Interpolação (Seção 5.3)

Matematicamente, a rede RBF tenta encontrar uma função $F(x)$ que passe exatamente (ou muito perto) de todos os pontos de treinamento $(x_i, d_i)$.

A função de saída para uma entrada $x$ é dada por:
$$
F(x) = \sum_{i=1}^{N} w_i \phi(\|x - x_i\|)
$$

Onde:
* $\|x - x_i\|$: É a distância euclidiana entre a entrada e o centro do neurônio.
* $\phi$: É a função de base radial (geralmente uma curva em formato de sino).
* $w_i$: São os pesos da camada de saída.

### A Função Gaussiana (A mais comum)
$$
\phi(r) = \exp\left(-\frac{r^2}{2\sigma^2}\right)
$$
* Se a entrada está perto do centro do neurônio, a ativação é alta (próxima de 1).
* Se a entrada está longe, a ativação cai rapidamente para 0.

---

## Laboratório Conceitual: Visualizando a Função Radial

Para entender como a distância vira uma ativação no seu VS Code, visualize o arquivo 01_funcao_radial.py:

---

## Checkpoint
1. **Qual a principal diferença entre a camada oculta da MLP e da RBF?** Na MLP, a camada oculta usa funções sigmoides/ReLU e pesos treináveis. Na RBF, a camada oculta realiza uma transformação não-linear fixa baseada na distância para centros pré-definidos.
2. **O que diz o Teorema de Cover?** Que aumentar a dimensão do espaço (via transformação não-linear) aumenta as chances de tornar os dados linearmente separáveis.
3. **Por que a camada de saída da RBF é linear?** Porque a transformação complexa já foi feita na camada oculta; na saída, basta somar as contribuições de cada neurônio radial para obter a resposta final.

---