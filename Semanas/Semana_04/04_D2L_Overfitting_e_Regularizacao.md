# 📖 Semana 04: Seleção de Modelo e Regularização (Visão D2L)
> S4 - Texto-base 3 – Dive into Deep Learning - em português (Seções 4.4, 4.5, 4.6) | Aston Zhang et al.

O livro *Dive into Deep Learning* aborda a engenharia de modelos com foco na diferença matemática entre memorizar dados e descobrir padrões universais.

## 1. Erro de Treinamento vs. Erro de Generalização (Seção 4.4)

A Seção 4.4 formaliza os dois principais erros que monitoramos em Machine Learning:
* **Erro de Treinamento:** A métrica calculada sobre os dados que o modelo efetivamente "vê" e usa para atualizar os pesos.
* **Erro de Generalização:** A expectativa teórica do erro sobre uma população infinita de dados novos. Como não temos dados infinitos, estimamos esse erro usando o conjunto de teste.

### O Fenômeno do Subajuste e Sobreajuste
O D2L utiliza o exemplo clássico do ajuste de curvas polinomiais para ilustrar a capacidade do modelo:
* **Subajuste (Underfitting):** O modelo é simples demais (ex: uma linha reta de grau 1) para capturar um padrão complexo (ex: uma parábola). O erro é alto em todo lugar.
* **Sobreajuste (Overfitting):** O modelo é complexo demais (ex: polinômio de grau 9). Ele cria uma curva absurda que passa perfeitamente por todos os pontos de treino (erro zero), mas erra bizarramente em qualquer ponto novo.



---

## 2. Decaimento de Pesos / Regularização $L_2$ (Seção 4.5)

Para controlar a complexidade de um modelo sem necessariamente reduzir o número de neurônios, limitamos os valores que os pesos podem assumir. O **Decaimento de Pesos** penaliza pesos grandes adicionando o quadrado da magnitude deles (norma $L_2$) à função de perda clássica.

A nova função de perda minimizada pelo modelo passa a ser:

$$
L(\mathbf{w}, b) + \frac{\lambda}{2} \|\mathbf{w}\|^2
$$

* $L(\mathbf{w}, b)$: O erro original (ex: Erro Quadrático Médio).
* $\lambda$ (lambda): O hiperparâmetro de regularização. Se $\lambda = 0$, não há regularização. Quanto maior o $\lambda$, mais a rede é forçada a manter os pesos próximos de zero.
* O termo é dividido por 2 apenas para simplificar a matemática quando calculamos a derivada (o 2 "cai" e corta).

---

## 3. Dropout: Injeção de Ruído Interno (Seção 4.6)

Enquanto a penalidade $L_2$ atua diretamente na matemática da função de custo, o **Dropout** atua na arquitetura da rede injetando "ruído" nas ativações das camadas ocultas.

A sacada genial matemática do Dropout é que, ao zerar um neurônio aleatoriamente (com probabilidade $p$), ele precisa **redimensionar os neurônios sobreviventes** (dividindo por $1-p$) para garantir que a esperança matemática da camada (o valor médio esperado) continue exatamente a mesma.

Para um neurônio oculto $h$, a aplicação do dropout resulta em $h'$:

$$
h' = 
\begin{cases} 
0 & \text{com probabilidade } p \\ 
\frac{h}{1-p} & \text{com probabilidade } 1-p 
\end{cases}
$$



---

## Laboratório: A Matemática do Dropout no Código

Para entender exatamente como essa fórmula do Dropout se comporta nos tensores, verifique o script matematica_dropout.py 



---

## Checkpoint 
1. **O que é capacidade do modelo?** É a habilidade matemática do modelo de se ajustar a uma ampla variedade de funções. Modelos profundos têm alta capacidade, o que facilita o sobreajuste se não houver dados suficientes.
2. **Como o hiperparâmetro $\lambda$ afeta os pesos?** Um $\lambda$ elevado puxa agressivamente os pesos para próximo de zero, "amortecendo" a rede e reduzindo sua complexidade para evitar overfitting.
3. **Por que o Dropout redimensiona os neurônios (divide por $1-p$)?** Para manter o valor esperado das ativações constante entre a fase de treinamento (com neurônios faltando) e a fase de teste (onde todos os neurônios estão ativos).

---