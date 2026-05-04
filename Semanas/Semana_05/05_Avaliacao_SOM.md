# 📊 Semana 05: Avaliação da Qualidade da Rede SOM

> S5 - Texto-base 4 – Avaliação da rede SOM | Marcos G. Quiles

Após o treinamento de um Mapa Auto-organizável, precisamos de métricas objetivas para saber se a rede realmente aprendeu a estrutura dos dados ou se o mapa "se embolou" durante a competição. As duas métricas principais focam na **Precisão** e na **Topologia**.

## 1. Erro de Quantização ($q_e$)

O Erro de Quantização mede a **resolução do mapa**. Ele indica o quão bem os pesos dos neurônios (protótipos) representam os dados de entrada.

*   **Cálculo:** É a média das distâncias euclidianas entre cada vetor de entrada $\mathbf{x}$ e sua respectiva BMU (vencedor).
*   **Interpretação:** 
    *   **$q_e$ baixo:** Significa que os neurônios estão "em cima" dos dados. O mapa representa bem os valores reais.
    *   **$q_e$ alto:** Sugere que a grade não é densa o suficiente ou que o treinamento não convergiu.

---

## 2. Erro Topológico ($t_e$)

O Erro Topológico mede a **preservação da forma**. Ele verifica se a rede conseguiu manter a vizinhança correta entre os dados.

*   **Cálculo:** Para cada dado, encontramos a 1ª BMU (vencedor) e a 2ª BMU (segundo lugar). Se esses dois neurônios **não forem vizinhos adjacentes** na grade, temos um erro topológico.
*   **Interpretação:**
    *   O erro é a proporção de dados onde as duas melhores BMUs não são vizinhas.
    *   Um $t_e$ alto indica que o mapa está "torcido" ou "rasgado", falhando em sua missão principal de preservar a topologia.



---

## 3. Visualização: A Matriz-U (Unified Distance Matrix)

A Matriz-U é a ferramenta visual padrão para interpretar o SOM. Ela calcula a distância entre os pesos de neurônios vizinhos na grade.

*   **Cumes (Cores escuras/altas):** Indicam grandes distâncias entre neurônios. Funcionam como "muros" que separam diferentes agrupamentos (clusters).
*   **Vales (Cores claras/baixas):** Indicam neurônios muito parecidos. Representam o "corpo" de um cluster, onde os dados são homogêneos.



---

## 💻 Laboratório: Calculando o Erro de Quantização

Para entender a matemática por trás da métrica , verifique o arquivo `Semanas/Semana_05/05_metricas_som.py`:

---

## Resumo para Revisão
*   **Precisão:** Avaliada pelo Erro de Quantização (distância dado-peso).
*   **Topologia:** Avaliada pelo Erro Topológico (vizinhança das BMUs).
*   **Análise Visual:** Feita pela Matriz-U para identificar fronteiras entre grupos.

---