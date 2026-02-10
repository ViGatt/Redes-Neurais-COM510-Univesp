# Semana 02: Preparação de Dados para Treinamento

A preparação correta evita problemas como o **overfitting** (quando a rede decora o treino mas falha no mundo real) e garante que todos os atributos tenham a mesma importância matemática.

## 1. Divisão do Conjunto de Dados

A base de dados original deve ser separada em três partes distintas para garantir a integridade do modelo:

1. **Conjunto de Treino:** Usado para o ajuste dos **parâmetros** (pesos e biases).
2. **Conjunto de Validação:** Usado para ajustar os **hiperparâmetros** (ex: número de camadas, neurônios, taxa de aprendizado).
3. **Conjunto de Teste:** Usado apenas uma vez, ao final, para avaliar o desempenho real. **Nunca** deve ser usado durante o desenvolvimento.

> **Proporções Sugeridas:**
> * Bases pequenas/médias: 70% Treino / 15% Validação / 15% Teste.
> * Bases gigantes (Big Data): 98% Treino / 1% Validação / 1% Teste.

---

## 2. Validação Cruzada (k-fold Cross-Validation)

Indicada quando o volume de dados é pequeno.

* Divide-se os dados em  blocos (folds).
* O modelo é treinado  vezes. Em cada vez, um bloco diferente é usado para validação e os outros $k-1$ para treino.
* O resultado final é a média das  execuções.

---

## 3. Pré-processamento de Dados

As redes neurais trabalham apenas com números e escalas equilibradas.

### **A. Transformação de Dados Categóricos (One-Hot Encoding)**

Se um atributo não é numérico (ex: "Cor": Verde, Azul, Vermelho), não podemos atribuir pesos 1, 2 e 3, pois a rede acharia que Vermelho é "maior" que Verde.

* **Solução:** Criamos colunas binárias para cada categoria.
* Verde $\to$ [1, 0, 0]
* Azul $\to$ [0, 1, 0]
* Vermelho $\to$ [0, 0, 1]


### **B. Normalização**

Serve para equilibrar a escala de atributos diferentes (ex: Idade [0-100] vs. Salário [0-10.000]).

| Método | Fórmula | Características |
| --- | --- | --- |
| **Por Amplitude (Min-Max)** | $v_{novo} = \frac{v_{atual} - min}{max - min}$ | Restringe dados a um intervalo fixo (ex: 0 a 1). Sensível a *outliers*. |
| **Por Distribuição (Z-score)** | $v_{novo} = \frac{v_{atual} - \mu}{\sigma}$ | Transforma os dados para média 0 e desvio padrão 1. Mais tolerante a *outliers*. |

---

## Checkpoint

* **Qual a diferença entre parâmetros e hiperparâmetros?** Parâmetros (pesos) são ajustados no treino; Hiperparâmetros (arquitetura) são validados no conjunto de validação.
* **Quando usar Normalização por Distribuição?** Quando seus dados possuem muitos valores discrepantes (*outliers*).
* **Pode-se usar o conjunto de teste para escolher o número de neurônios?** **Não.** Isso viciaria o modelo e invalidaria a avaliação final.
