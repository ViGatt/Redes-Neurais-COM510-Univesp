### 🧠 Notas de Aula: Introdução às Redes Neurais Artificiais (RNA)

#### **1. O Contexto: IA vs. Machine Learning vs. Deep Learning**

* **IA (Inteligência Artificial):** Campo amplo que busca simular inteligência humana.
* **Machine Learning (ML):** Subcampo da IA que foca em algoritmos que aprendem padrões a partir de dados, sem programação explícita para cada tarefa.
* **Redes Neurais (Sistemas Conexionistas):** Modelos de ML inspirados na microestrutura do cérebro.
* **Deep Learning:** Redes neurais com muitas camadas ("profundas"), capazes de extrair características complexas automaticamente.

#### **2. Inspiração Biológica: O Neurônio**

As RNAs tentam emular qualitativamente o funcionamento do sistema nervoso:

* **Dendritos:** Receptores de sinais (Entradas).
* **Corpo Celular (Soma):** Processador central (Soma Ponderada).
* **Axônio:** Transmissor do sinal (Caminho para a Saída).
* **Sinapses:** Pontos de conexão onde ocorre o ajuste de intensidade (Pesos).

#### **3. Modelagem Matemática (O Modelo MCP)**

Proposto por McCulloch e Pitts (1943), o neurônio artificial é uma abstração simplificada:

1. **Entradas ():** Sinais provenientes do ambiente ou de outros neurônios.
2. **Pesos ():** Parâmetros que determinam a influência de cada entrada. É onde o **conhecimento** fica armazenado.
3. **Junção Somadora:** Calcula o potencial de ativação (campo local induzido).
4. **Função de Ativação ():** Decide se o neurônio deve "disparar" (enviar sinal) ou não.

*(Onde  representa o limiar de ativação ou "threshold").*

#### **4. Paradigmas de Aprendizagem**

| Paradigma | Descrição | Exemplo |
| --- | --- | --- |
| **Supervisionado** | O modelo aprende com dados rotulados (Entrada + Resposta Correta). | Classificação de e-mails (Spam/Não Spam). |
| **Não Supervisionado** | O modelo busca padrões e estruturas ocultas nos dados sem rótulos. | Agrupamento de clientes (Clustering). |
| **Por Reforço** | O modelo aprende por tentativa e erro, recebendo prêmios ou punições. | IA jogando videogame ou robótica. |

---

**Dica para o Quiz:** Fique atento à diferença entre o neurônio biológico (contínuo/químico) e o artificial (discreto/matemático) e lembre-se que o "conhecimento" da rede está nos **pesos sinápticos**.

[Introdução às Redes Neurais - Aula 01](https://www.youtube.com/watch?v=kzFqGhK8Q2s)
Este vídeo fornece uma visão detalhada sobre a história e os fundamentos das redes neurais, essencial para compreender a transição do modelo biológico para o matemático abordada na sua disciplina.