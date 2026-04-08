# 🚀 Semana 04: Otimizadores Modernos (RMSProp e Adam)

>S4 - Texto-base 6 – Dive into Deep Learning - em português (Leia as seções 11.8 e 11.10) | Aston Zhang et al.


O Gradiente Descendente Estocástico (SGD) com Momentum é excelente, mas possui um ponto cego: ele usa a mesma taxa de aprendizagem ($\eta$) para todos os pesos da rede. O livro D2L explica como algoritmos modernos adaptam essa taxa **individualmente para cada peso**.

## 1. O Problema das Escalas Diferentes
Em problemas multidimensionais, a superfície de erro frequentemente se parece com um "desfiladeiro" ou ravina: muito íngreme em uma direção e muito plana em outra.
* Se usarmos um $\eta$ grande, o peso da direção íngreme explode (diverge).
* Se usarmos um $\eta$ pequeno, o peso da direção plana demora uma eternidade para convergir.

A solução é usar uma **Taxa de Aprendizagem Adaptativa**: frear a atualização de pesos que estão oscilando muito e acelerar a atualização de pesos que estão estagnados.

---

## 2. RMSProp (Root Mean Square Propagation) - Seção 11.8

O RMSProp resolve o problema do desfiladeiro dividindo a taxa de aprendizagem por uma média móvel exponencial do quadrado dos gradientes recentes.

* **O Mecanismo:** O algoritmo mantém um histórico (uma variável de estado $\mathbf{s}$) que acumula o quadrado do gradiente $\mathbf{g}$.
* **A Matemática:**
  $$\mathbf{s} \leftarrow \gamma \mathbf{s} + (1 - \gamma) \mathbf{g}^2$$
  $$\mathbf{w} \leftarrow \mathbf{w} - \frac{\eta}{\sqrt{\mathbf{s} + \epsilon}} \odot \mathbf{g}$$
* **Intuição:** Se um peso tem tido gradientes muito grandes (oscilando muito), o seu valor $\mathbf{s}$ será grande. Como dividimos o passo por $\sqrt{\mathbf{s}}$, o passo real dado por esse peso é "encurtado" (amortecido). Se o gradiente é pequeno, $\mathbf{s}$ é pequeno, e a divisão atua como um multiplicador, acelerando o passo.

---

## 3. Adam (Adaptive Moment Estimation) - Seção 11.10

O Adam é, indiscutivelmente, o otimizador mais famoso e utilizado em Deep Learning hoje. Ele é essencialmente a união perfeita do **Momentum** com o **RMSProp**.

### Os Dois Momentos
O Adam calcula e guarda duas médias móveis:
1. **Primeiro Momento ($\mathbf{v}$):** A média dos gradientes passados (exatamente como o Momentum clássico). Funciona como a "inércia" da bola rolando.
2. **Segundo Momento ($\mathbf{s}$):** A média dos gradientes ao quadrado (exatamente como o RMSProp). Funciona como o "amortecedor" de escalas.

### Correção de Viés (Bias Correction)
O grande diferencial do Adam é que, nas primeiras épocas, essas médias ($\mathbf{v}$ e $\mathbf{s}$) são inicializadas com zero e demoram a "esquentar". O algoritmo aplica uma correção matemática pesada nas iterações iniciais para compensar isso, garantindo que a rede comece aprendendo rápido e de forma estável desde o passo 1.



---

## Laboratório: Otimizadores no PyTorch

A melhor parte da engenharia moderna é que toda essa matemática complexa está encapsulada em uma única linha de código. Visualize o script `comparativo_otimizadores.py` no seu VS Code para ver a sintaxe


---
## Checkpoint
1. **Qual é o diferencial das taxas adaptativas (RMSProp/Adam)?** Diferente do SGD, elas ajustam dinamicamente a taxa de aprendizagem para cada peso individualmente, dependendo do histórico de gradientes daquele peso.
2. **O que o Adam combina?** Ele combina a inércia direcional (Momentum) com o ajuste de escala por magnitude (RMSProp).
3. **Por que o Adam faz correção de viés?** Para compensar o fato de que as médias móveis são inicializadas em zero, evitando passos falsos e lentidão nas primeiras iterações do treinamento.