# Semana 02: Representação por Grafos e Arquiteturas Modernas

Esta aula foca na formalização visual das redes e na introdução de modelos avançados como CNNs e Autoencoders.

## 1. Representação via Grafos Orientados

A representação por grafos facilita a derivação matemática e a visualização do fluxo de sinais. O fluxo é regido por três regras fundamentais:

* **Regra 1:** O sinal flui ao longo de um elo apenas no sentido da seta.
* **Regra 2:** O sinal de um nó é a **soma** de todos os sinais que entram nele.
* **Regra 3:** O sinal de um nó é transmitido para **todos** os elos de saída, independentemente das funções de transferência seguintes.

---

## 2. Taxonomia das Arquiteturas

A aula reforça as arquiteturas do Haykin e adiciona modelos de redes profundas:

### **Arquiteturas Clássicas**

1. **Camada Única (Single-Layer):** Apenas uma camada computacional (a de saída).
2. **Múltiplas Camadas (Multi-Layer):** Possui camadas ocultas que extraem estatísticas de ordem elevada.
3. **Redes Recorrentes (RNN):** Apresentam loops de realimentação, permitindo processar dados temporais.

### **Arquiteturas Modernas e Profundas**

* **Redes Convolucionais (CNN):** Especializadas em dados com grade (imagens). Utilizam conectividade local e compartilhamento de pesos.
* **Autoencoders:** Modelos **auto-supervisionados** que aprendem a comprimir a entrada em um "espaço latente" (Encoder) e depois reconstruí-la (Decoder).
* **GANs (Redes Adversárias Generativas):** Duas redes competindo — um Gerador (cria dados falsos) e um Discriminador (tenta detectar o que é real).
* **Arquiteturas Profundas:** Definidas pelo grande número de camadas e parâmetros ajustáveis.

---

## 3. Combinação de Arquiteturas

Uma tendência importante citada é a hibridização de modelos, como:

* **CNN + RNN:** Camadas convolucionais extraem características de imagens/vídeos e camadas recorrentes processam a sequência temporal dessas características.

---

## Destaque 

* **O que define uma arquitetura profunda?** O grande número de camadas e, consequentemente, de parâmetros ajustáveis.
* **Autoencoders são supervisionados?** Não, são considerados **auto-supervisionados**, pois usam a própria entrada como alvo.
* **Função dos neurônios ocultos:** Intervir entre a entrada e a saída para extrair características complexas.
