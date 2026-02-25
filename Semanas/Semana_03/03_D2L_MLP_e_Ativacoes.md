

#  Semana 03: Por que Deep Learning? (Visão D2L)
> S3 - Texto-base 3 – Dive into Deep Learning – edição em português (leia a Seção 4.1) | Aston Zhang e outros

Enquanto o Perceptron simples mapeia entradas diretamente para saídas, o **Perceptron Multicamadas (MLP)** aprende uma representação intermediária dos dados.

## 1. As Limitações da Linearidade

Modelos lineares assumem a **monotonicidade**: a ideia de que um aumento em um recurso ($x$) deve sempre causar um aumento (ou diminuição) na saída. No entanto, o mundo real raramente é assim:

* **Exemplo de Saúde:** Se a temperatura corporal sobe de 35°C para 37°C, o risco de morte diminui. Mas se sobe de 37°C para 40°C, o risco aumenta. Um modelo linear não consegue capturar essa inversão sem pré-processamento manual complexo.
* **Exemplo de Imagens:** Mudar o brilho de um único pixel não diz se a imagem é um gato ou um cachorro. O significado de um pixel depende do **contexto** (pixels ao redor).

## 2. A Camada Oculta e o Ingrediente Secreto

Para superar a linearidade, empilhamos camadas. No entanto, matematicamente, **empilhar camadas lineares não adianta nada**:

Se tivermos:

1. Camada Oculta: $\mathbf{H} = \mathbf{X}\mathbf{W}_1 + \mathbf{b}_1$
2. Camada de Saída: $\mathbf{O} = \mathbf{H}\mathbf{W}_2 + \mathbf{b}_2$

Podemos substituir $\mathbf{H}$ na segunda equação:
$\mathbf{O} = (\mathbf{X}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2 = \mathbf{X}(\mathbf{W}_1\mathbf{W}_2) + (\mathbf{b}_1\mathbf{W}_2 + \mathbf{b}_2)$

Isso resulta em um novo modelo linear $\mathbf{O} = \mathbf{X}\mathbf{W}_{novo} + \mathbf{b}_{novo}$.

> **Conclusão:** Para que o MLP funcione, precisamos aplicar uma **Função de Ativação Não Linear** ($\sigma$) após cada camada oculta:
> 
> $$\mathbf{H} = \sigma(\mathbf{X}\mathbf{W}_1 + \mathbf{b}_1)$$
> 
> 

---

## 3. Galeria de Funções de Ativação

As funções de ativação são operadores diferenciáveis que decidem o "disparo" do neurônio e adicionam a não linearidade necessária.

| Função | Fórmula | Comportamento | Uso Principal |
| --- | --- | --- | --- |
| **ReLU** | $max(0, x)$ | Zera valores negativos e mantém positivos. | Padrão ouro para **camadas ocultas**. Evita o desaparecimento do gradiente. |
| **Sigmoid** | $\frac{1}{1 + e^{-x}}$ | Esmaga valores para o intervalo $(0, 1)$. | Camada de saída para **classificação binária**. |
| **Tanh** | $\tanh(x)$ | Esmaga valores para o intervalo $(-1, 1)$. | Similar à Sigmoid, mas centrada em zero. |

---

## 4. Teorema do Aproximador Universal

O D2L destaca que MLPs são **aproximadores universais**:

* Com uma única camada oculta e neurônios suficientes, um MLP pode modelar **qualquer função computável**.
* **Analogia:** É como a linguagem C; você pode escrever qualquer programa com ela, mas o desafio é descobrir como configurar os parâmetros para que o programa faça o que você quer.

---

## Checkpoint para o Quiz

1. **Por que precisamos de ativações não lineares?** Porque sem elas, múltiplas camadas colapsam em uma única transformação linear.
2. **Qual a vantagem da ReLU sobre a Sigmoid?** Suas derivadas são mais fáceis de calcular (0 ou 1) e ela não satura para valores altos, mitigando o problema do gradiente de desaparecimento.
3. **Monotonicidade:** É a suposição de que se uma entrada aumenta, a saída deve obrigatoriamente seguir a mesma tendência (aumentar ou diminuir sempre). MLPs quebram essa suposição para lidar com dados complexos.

---

