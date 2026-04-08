# 🎯 Semana 05: Arquitetura e Treinamento de Redes RBF (Videoaula 13)

Nesta aula, o professor Marcos G. Quiles detalha o funcionamento das redes de **Função de Base Radial (RBF)**, destacando como elas utilizam a geometria local para resolver problemas de aproximação e classificação.

## 1\. Conceito e Histórico

A ideia central das RBFs é construir funções complexas a partir da combinação de funções simples (radiais).

  * **Inspiração:** Campos receptivos locais encontrados no sistema biológico.
  * **Funcionamento:** O neurônio não olha para o dado como um todo, mas sim para o quão **próximo** ele está de um ponto de referência (centro).
  * **Versatilidade:** Assim como as MLPs, as redes RBF são **aproximadores universais**, capazes de mapear qualquer função contínua.

-----

## 2\. O Neurônio de Base Radial

Diferente do neurônio do Perceptron (que calcula um produto escalar), o neurônio RBF calcula a **distância euclidiana** entre a entrada $\mathbf{x}$ e o seu centro $\mathbf{\mu}$.

### Função Gaussiana (A mais utilizada)

A resposta do neurônio é máxima quando a distância é zero e decai suavemente conforme o dado se afasta:

$$
\phi(r) = \exp\left(-\frac{\|\mathbf{x} - \mu\|^2}{2\sigma^2}\right)
$$

  * **$\mu$ (mu):** O centro do neurônio (protótipo).
  * **$\sigma$ (sigma):** A largura do campo receptivo. Define o "raio de influência" do neurônio.

-----

## 3\. Arquitetura da Rede

A rede RBF possui uma estrutura rígida de três camadas:

1.  **Camada de Entrada:** Apenas repassa os dados.
2.  **Camada Oculta:** Realiza uma transformação **não-linear** do espaço de entrada para um espaço de alta dimensão (Teorema de Cover). Cada neurônio aqui representa um "cluster" ou região do espaço.
3.  **Camada de Saída:** Realiza uma combinação **linear** das ativações da camada oculta.
      * A saída final é: $y = \sum w_i \phi_i(x)$.

-----

## 4\. Estratégias de Treinamento

O treinamento de uma RBF é geralmente mais rápido que o da MLP devido à sua natureza híbrida:

| Estratégia | Descrição | Complexidade |
| :--- | :--- | :--- |
| **Centros Fixos Aleatórios** | Os centros são escolhidos aleatoriamente dos dados de treino. Apenas a saída é treinada. | Muito Baixa |
| **Híbrida (K-Means)** | 1. Os centros são encontrados via **K-Means** (Não Supervisionado).<br>2. Os pesos de saída são ajustados via Mínimos Quadrados (Supervisionado). | Média |
| **Supervisionada Total** | Centros, larguras e pesos são ajustados via **Gradiente Descendente** simultaneamente. | Alta |

> **Nota sobre o K-Means:** O algoritmo busca minimizar a distância dos exemplos aos centros (centroides), garantindo que os neurônios ocultos cubram as áreas onde os dados realmente existem.

-----

## 5\. Comparativo: RBF vs. MLP

  * **Arquitetura:** RBF geralmente tem apenas **uma** camada oculta; MLP pode ser profunda.
  * **Ativação:** Neurônios RBF são **locais** (ativam apenas em áreas específicas); MLP são **globais** (neurônios podem responder a grandes porções do espaço).
  * **Velocidade:** RBF treina muito mais rápido em abordagens híbridas, pois o ajuste final é uma simples regressão linear.

-----

## Laboratório: Implementação com Scipy e Sklearn

Para testar o conceito de aproximação radial no seu VS Code, você pode usar este exemplo no arquivo `03_rbf_interpolacao.py`:

-----

## Checkpoint

1.  **O que define a saída de um neurônio RBF?** A distância entre a entrada e o centro do neurônio, processada por uma função radial (ex: Gaussiana).
2.  **Qual a função do K-Means no treinamento RBF?** Encontrar a posição ideal dos centros ($\mu$) na camada oculta de forma não supervisionada.
3.  **Por que a camada de saída da RBF é linear?** Porque a transformação complexa e não-linear para um espaço de alta dimensão já foi realizada pela camada oculta; o problema na saída torna-se linearmente separável.

-----


