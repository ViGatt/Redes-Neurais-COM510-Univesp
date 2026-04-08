# 🧠 Semana 05: Estratégias de Aprendizado e Comparação RBF (Haykin 5.8, 5.11, 5.13)
>S5 - Texto-base 2 – Redes Neurais: princípios e prática (Seções 5.8, 5.11 e 5.13) | Simon Haykin

Diferente das MLPs, as redes de Função de Base Radial possuem uma natureza dual: uma camada oculta que interpreta a geometria local e uma camada de saída que realiza uma combinação linear.

## 1. Estratégias de Aprendizado (Seção 5.8)

Existem três formas principais de configurar e treinar uma rede RBF, variando em complexidade e eficiência:

### **A. Centros Fixos Selecionados Aleatoriamente**
* **O que é:** Os centros ($\mu$) são escolhidos aleatoriamente a partir dos dados de treinamento.
* **Ajuste:** Apenas os pesos da camada de saída são treinados (via Mínimos Quadrados).
* **Vantagem:** Extremamente rápido. É a forma mais simples de implementar.

### **B. Seleção Auto-organizada de Centros (Aprendizado Híbrido)**
* **O que é:** Os centros são determinados por um algoritmo de **agrupamento (Clustering)**, como o K-means. 
* **Funcionamento:** 1.  **Fase Não Supervisionada:** Agrupa-se os dados de entrada para encontrar os centros naturais (protótipos).
    2.  **Fase Supervisionada:** Com os centros fixos, ajusta-se os pesos de saída usando regressão linear.
* **Vantagem:** Os neurônios ocultos se posicionam onde os dados realmente estão, otimizando a cobertura do espaço.

### **C. Seleção Supervisionada de Centros**
* **O que é:** Todos os parâmetros (centros, larguras das gaussianas e pesos de saída) são ajustados simultaneamente.
* **Mecanismo:** Utiliza-se o Gradiente Descendente (similar ao Backpropagation).
* **Vantagem:** É a abordagem mais precisa, porém a mais lenta e computacionalmente cara.

---

## 2. Redes de Regularização (Seção 5.11)

Esta seção fornece a justificativa matemática rigorosa: a rede RBF pode ser vista como a solução para um **problema de regularização**.
* Para evitar que a rede apenas "decore" os pontos (overfitting), a teoria de regularização impõe uma restrição de **suavidade** à função aprendida. 
* A função Gaussiana é o kernel natural que emerge dessa matemática para garantir que a transição entre pontos conhecidos seja suave e contínua.

---

## 3. RBF vs. MLP: O Grande Comparativo (Seção 5.13)

Embora ambas sejam aproximadores universais, suas filosofias são opostas:

| Característica | Redes MLP (Multilayer Perceptron) | Redes RBF (Radial Basis Function) |
| :--- | :--- | :--- |
| **Ativação** | Global (Sigmoide/ReLU cobrem áreas vastas). | Local (Gaussiana só ativa perto do centro). |
| **Camadas** | Pode ter muitas camadas ocultas (Deep). | Geralmente possui apenas **uma** camada oculta. |
| **Conexões** | Pesos em todas as camadas são treinados. | Pesos de entrada são fixos (centros); apenas saída é treinada. |
| **Aprendizado** | Uniforme (Backpropagation em tudo). | Frequentemente híbrido (Clustering + Linear). |



---

## Laboratório: Abordagem Híbrida (K-Means + Linear)

Para simular a estratégia "B" no seu VS Code, utilize este esqueleto usando Scikit-Learn no arquivo `02_rbf_hibrida.py`:



---

## Checkpoint 
1.  **Por que a RBF é chamada de "Aproximador Local"?** Porque cada neurônio só responde a uma vizinhança pequena ao redor do seu centro. Fora disso, a Gaussiana tende a zero.
2.  **Qual a vantagem de usar K-means para definir os centros?** Garante que os neurônios ocultos representem a real distribuição estatística dos dados, sem "desperdiçar" neurônios em áreas vazias.
3.  **O que acontece se o $\sigma$ (largura) for muito pequeno?** A rede perde a capacidade de interpolação e vira um "vizinho mais próximo", ativando apenas um neurônio por vez e perdendo a suavidade.

---