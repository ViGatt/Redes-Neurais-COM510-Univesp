# 🗺️ Semana 05: Mapas Auto-organizáveis (Haykin 9.1 - 9.4)

> S5 - Texto-base 3 – Redes Neurais: princípios e prática (Leia as seções 9.1 até 9.4) | Simon Haykin

Os Mapas Auto-organizáveis (Self-Organizing Maps - SOM) são inspirados na organização do córtex cerebral, onde neurônios vizinhos se especializam em tarefas ou estímulos sensoriais semelhantes.

## 1. Introdução e Filosofia (Seção 9.1)

Diferente de tudo o que vimos até agora, o SOM utiliza **Aprendizado Não Supervisionado**.
*   **O Objetivo:** Converter padrões de entrada complexos de alta dimensão em um mapa discreto de baixa dimensão (geralmente 1D ou 2D).
*   **Preservação Topológica:** A rede garante que pontos que estão próximos no espaço original (alta dimensão) fiquem próximos no mapa (grade de neurônios).
*   **Aplicações:** Agrupamento de dados (clustering), visualização e redução de dimensionalidade.



---

## 2. Arquitetura e os "Dois Reticulados" (Seção 9.2)

A rede SOM possui apenas duas camadas:
1.  **Camada de Entrada:** Representa o vetor de dados $\mathbf{x}$.
2.  **Camada de Saída (Grade/Lattice):** Uma grade de neurônios organizada em uma topologia fixa (ex: hexagonal ou retangular). Cada neurônio na grade possui um **vetor de pesos** com a mesma dimensão que a entrada.

---

## 3. O Processo de Auto-organização (Seção 9.3)

O aprendizado no SOM ocorre através de um processo competitivo em três estágios fundamentais:

### **A. Competição**
Para cada padrão de entrada, todos os neurônios da grade "competem" entre si. O vencedor é o neurônio cujo vetor de pesos é mais similar (menor distância euclidiana) ao vetor de entrada.
*   **BMU (Best Matching Unit):** É o neurônio vencedor.

### **B. Cooperação**
O vencedor (BMU) ativa seus vizinhos imediatos na grade.
*   **Função de Vizinhança:** Neurônios próximos ao vencedor aprendem mais; neurônios distantes aprendem menos ou nada. Geralmente usa-se uma função Gaussiana que diminui com o tempo de treino.

### **C. Adaptação**
A rede ajusta os pesos do vencedor e de seus vizinhos para que eles se tornem mais parecidos com o padrão de entrada atual. A regra de atualização é:
$$\Delta w_{ji} = \eta(t) \cdot h_{j,i(x)}(t) \cdot (x_i - w_{ji})$$
*   $\eta(t)$: Taxa de aprendizado que decai com o tempo.
*   $h(t)$: Função de vizinhança que encolhe com o tempo.

---

## 4. Propriedades do Mapa (Seção 9.4)

*   **Aproximação de Densidade:** Áreas do espaço com muitos dados atrairão mais neurônios no mapa.
*   **Seleção de Atributos:** O mapa aprende a representar as variações mais importantes dos dados de forma autônoma.

---

---

## 💻 Laboratório Conceitual: A Competição

Para visualizar como o SOM escolhe um vencedor, verifique o exemplo no arquivo `Semanas/Semana_05/04_som_competicao.py`:


---

## Checkpoint
1.  **O SOM é supervisionado ou não supervisionado?** Não supervisionado; ele não recebe rótulos ou valores desejados de saída.
2.  **O que define a "vizinhança" no SOM?** A posição física do neurônio na grade de saída, não o valor do seu peso.
3.  **Qual a finalidade da função de vizinhança encolher com o tempo?** No início, permite grandes mudanças globais para organizar o mapa. No fim, permite ajustes finos e locais.