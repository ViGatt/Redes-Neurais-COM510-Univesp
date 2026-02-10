#  Semana 02: Modelos Estocásticos e Arquiteturas de Rede

Nesta etapa, avançamos da unidade básica para a organização sistêmica das redes neurais, explorando como a estrutura influencia o aprendizado.

## 1. Modelo Estocástico de um Neurônio (Seção 1.4/1.5)
> Texto-base 1 – Redes Neurais: princípios e prática (Leia Capítulo 1 - Seções 1.4, 1.5 e 1.6 | Simon Haykin


Diferente do modelo determinístico (onde a saída é sempre a mesma para uma entrada fixa), o modelo estocástico introduz a **probabilidade** no disparo do neurônio.

* **Estado do Neurônio ():** Assume valores binários (ex: +1 ou -1).
* **Probabilidade de Disparo :** A decisão de mudar o estado para "ligado" é baseada em uma interpretação probabilística da função de ativação.
* **Influência da Temperatura ():** Utiliza-se uma "pseudotemperatura" para controlar o nível de ruído/incerteza.

### Equação Probabilística (Sigmoide):

> **Insight de Engenharia:** Quando , o neurônio se torna determinístico (comportando-se como uma função degrau). À medida que  aumenta, o comportamento torna-se mais aleatório.

---

## 2. Arquiteturas de Rede (Seção 1.6)

A arquitetura define como os neurônios são conectados e como o sinal flui. Existem três classes fundamentais:

### **A. Redes Alimentadas Adiante com Camada Única (Single-Layer Feedforward)**

É a forma mais simples. Temos uma camada de entrada (nós de fonte) que se projeta diretamente sobre uma camada de saída.

* **Observação Técnica:** A camada de entrada **não conta** como camada de processamento, pois não realiza cálculos. Por isso, chamamos de "camada única" referindo-se apenas à saída.

### **B. Redes Alimentadas Adiante com Múltiplas Camadas (Multi-Layer Feedforward)**

Distinguem-se pela presença de uma ou mais **camadas ocultas** (*hidden layers*).

* **Função dos Neurônios Ocultos:** Intervir entre a entrada e a saída para extrair estatísticas de ordem superior.
* **Perspectiva Global:** A rede deixa de ver apenas correlações simples e passa a entender padrões complexos devido às interações extras.

### **C. Redes Recorrentes (Recurrent Networks)**

Diferente das anteriores, estas possuem pelo menos um **laço de realimentação** (*feedback loop*).

* **Memória:** A realimentação permite que a rede mantenha uma forma de "memória" de estados anteriores, sendo essencial para processar sequências temporais ou dados que dependem do contexto.

---

##  Representação do Conhecimento

O conhecimento em uma rede neural não é um dado estático, mas um **modelo do mundo** armazenado nos pesos. Uma boa solução em Engenharia da Computação depende de:

1. Quais informações são tornadas explícitas.
2. Como essa informação é codificada fisicamente para uso subsequente.

## Dicas do Haykin

* **Redes Acíclicas:** São as *feedforward*. Não possuem loops.
* **Camadas Ocultas:** São o que permitem resolver problemas que não são linearmente separáveis (como o problema do XOR).
* **Nós de Fonte:** Apenas fornecem os dados; não possuem pesos ou funções de ativação.
---