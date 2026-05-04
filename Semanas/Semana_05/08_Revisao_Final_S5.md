# 🎓 Semana 05: Guia de Revisão e Consolidação Final

Este guia unifica os fundamentos teóricos do livro de Simon Haykin, a aplicação prática com o dataset Iris e os pontos críticos abordados nas avaliações da semana.

## 1. Fundamentos do Aprendizado Competitivo e SOM
O aprendizado competitivo é um processo não supervisionado onde os neurônios disputam a ativação por padrões de entrada.
*   **Regra de Saída:** Segue o princípio *Winner-Takes-All* (o vencedor leva tudo).
*   **Best Matching Unit (BMU):** É o neurônio cujo vetor de pesos é o mais próximo (menor distância euclidiana) do vetor de entrada.
*   **Fases de Treinamento do SOM**:
    1.  **Ordenação:** Utiliza vizinhança ampla para organizar o mapa topológico, aproximando a vizinhança do grid à do espaço original.
    2.  **Convergência:** Reduz o raio de vizinhança (até zero) para especializar neurônios em exemplos específicos.

## 2. Métricas e Visualização de Qualidade
*   **Erro de Quantização ($q_e$):** Mede a precisão da representação calculando a distância média entre os dados e seus respectivos pesos (BMUs).
*   **Erro Topográfico ($t_e$):** Avalia se a topologia foi preservada, verificando se a 1ª e a 2ª BMUs de um dado são vizinhas no grid.
*   **U-Matrix:** Visualiza as distâncias entre neurônios vizinhos; áreas de alta intensidade indicam fronteiras entre clusters.

## 3. Aplicação Prática: Dataset Iris e MiniSom
O agrupamento de dados reais exige ferramentas eficientes como a biblioteca **MiniSom**.
*   **Dataset Iris:** O SOM isola facilmente a classe *Setosa*, mas apresenta sobreposição entre *Versicolor* e *Virginica* devido às suas correlações.
*   **Parâmetros Críticos:** O sucesso do agrupamento depende do ajuste fino da taxa de aprendizado ($\eta$) e do desvio padrão da vizinhança ($\sigma$).

## 4. Tópicos Específicos de Avaliação (Quizzes/Provas)
Pontos de alta recorrência que complementam o estudo da semana:
*   **Redes RBF:** A estratégia mais simples para definir centros é fixá-los sobre os exemplos de treinamento (centros fixos selecionados ao acaso).
*   **Otimização:** O algoritmo **Adam** supera o SGD padrão por utilizar médias móveis para obter estimativas mais precisas do momentum e do gradiente.
*   **Redes Recorrentes (RNN):** Projetadas para dados sequenciais (fala, texto, vídeo) utilizando o algoritmo **BPTT** para propagar erros através de cópias temporais da rede.
*   **Máquina de Boltzmann:** Utiliza neurônios **visíveis** para interface com o ambiente e neurônios **ocultos** para extrair características e correlações.
*   **Poda de Rede (Pruning):** Visa melhorar a generalização e reduzir a complexidade eliminando pesos sinápticos de forma seletiva.

## 5. Identificação Visual de Arquiteturas
Relacione o grafo ao fluxo de sinais:
1.  **Rede Recorrente sem autoalimentação:** Ciclos entre neurônios, sem auto-laços.
2.  **Rede Alimentada Adiante Única:** Uma camada, sinal unidirecional.
3.  **Rede Recorrente com Ocultos:** Ciclos em camadas internas.
4.  **Rede Alimentada Adiante Múltipla:** Arquitetura MLP (várias camadas).

---