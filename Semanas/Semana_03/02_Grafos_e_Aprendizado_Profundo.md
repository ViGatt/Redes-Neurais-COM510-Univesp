

#  Semana 03: Redes Profundas e Grafos de Computação

Enquanto os modelos clássicos focam em camadas isoladas, a visão de Russell & Norvig foca na **expressividade** dos caminhos longos de computação e na automação do aprendizado.

## 1. Aprendizado Profundo como Circuitos (Seção 21.1)

A ideia central é representar hipóteses como **grafos de computação** com pesos ajustáveis.

* **Caminhos Longos de Computação:** Diferente das árvores de decisão (que podem ser curtas para a maioria das entradas), as redes profundas permitem que todas as variáveis de entrada interajam de formas complexas através de múltiplos níveis de abstração.
* **Expressividade:** Modelos de circuito são altamente expressivos e capturam a complexidade do mundo real (visão, fala, NLP) de forma que modelos "rasos" não conseguem.

---

## 2. A Vantagem da Profundidade (Seção 21.4)

Uma das descobertas empíricas mais importantes citadas é que, para um número similar de parâmetros, **redes mais profundas geralmente oferecem melhor generalização**.

* **Exemplo Prático:** No reconhecimento de números de casas, uma rede de 11 camadas apresenta um erro muito menor do que uma rede de 3 camadas com o mesmo número de pesos.
* **Redes Residuais (ResNets):** Para contornar o problema de treinar redes muito profundas, utilizam-se conexões residuais (atalhos) que permitem que o sinal passe diretamente por algumas camadas, evitando que o gradiente desapareça.

---

## 3. Diferenciação Automática e Aprendizado de Ponta a Ponta

Este é um conceito chave para quem desenvolve software:

* **Modo Reverso (Backpropagation):** É uma aplicação da regra da cadeia "de fora para dentro". É extremamente eficiente quando a rede tem muitas entradas e poucas saídas (como uma classificação).
* **Diferenciação Automática:** Os frameworks modernos automatizam o cálculo das derivadas. Isso dá liberdade para experimentar novas funções de ativação e estruturas sem precisar derivar o algoritmo manualmente toda vez.
* **Aprendizado de Ponta a Ponta (End-to-End):** Sistemas complexos (como tradutores) podem ser compostos por vários subsistemas treináveis. O sistema inteiro é treinado de uma vez a partir de pares de entrada e saída, sem necessidade de definir manualmente o que cada parte deve fazer.


---

## 📝 Checkpoint  (Visão Russell & Norvig)

1. **Árvores de Decisão vs. Redes:** Árvores são eficientes para poucas variáveis; Redes Profundas brilham na interação complexa de **alta dimensionalidade**.
2. **Por que usar redes profundas?** Elas generalizam melhor para o mesmo número de parâmetros em comparação com redes largas mas rasas.
3. **Diferenciação Automática:** É o que permite o **Aprendizado de Ponta a Ponta**, pois não exige que o projetista conheça a fundo o que cada subsistema faz individualmente.