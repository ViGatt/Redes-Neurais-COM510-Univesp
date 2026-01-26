Aqui está uma versão consolidada e aprofundada das suas anotações para a **Semana 01**. Reorganizei os tópicos integrando as definições formais do Simon Haykin com a estrutura didática da videoaula, focando no que é essencial para um estudante de Engenharia da Computação.

Esta estrutura está pronta para ser copiada para o seu arquivo `Semanas/Semana_01/01_Introducao.md`.

---

# 🧠 Semana 01: Fundamentos e o Neurônio Artificial

Nesta semana, exploramos a transição do modelo biológico para o matemático e os mecanismos fundamentais que permitem às máquinas "aprenderem" através de sistemas conexionistas.

## 1. Definições e Contexto Técnico

### O que é uma Rede Neural? (Definição de Haykin)

Segundo Simon Haykin, uma **Rede Neural** é um processador massivamente paralelo distribuído, composto por unidades de processamento simples, que possui duas propriedades fundamentais:

1. **Aprendizagem:** O conhecimento é adquirido pela rede a partir de seu ambiente.
2. **Armazenamento:** O conhecimento é guardado através de forças de conexão entre os neurônios, conhecidas como **Pesos Sinápticos**.

### Hierarquia da Inteligência

* **IA:** Campo que busca simular a inteligência humana.
* **Machine Learning (ML):** Algoritmos que aprendem padrões sem programação explícita.
* **Redes Neurais:** Modelos de ML que emulam a microestrutura do cérebro.
* **Deep Learning:** Redes com múltiplas camadas capazes de extrair características complexas automaticamente.

---

## 2. Analogia Biológica vs. Modelagem Matemática

As Redes Neurais Artificiais (RNAs) são simplificações do sistema nervoso.

| Componente Biológico | Componente Artificial | Função no Modelo |
| --- | --- | --- |
| **Dendritos** | Entradas () | Receptores de sinais/estímulos. |
| **Sinapses** | Pesos Sinápticos () | Intensidade da conexão (armazenamento de conhecimento). |
| **Corpo Celular (Soma)** | Junção Somadora () | Agregador dos sinais de entrada ponderados. |
| **Limiar de Disparo** | Bias () ou Limiar () | Ajuste para o neurônio "decidir" se dispara. |
| **Axônio** | Saída () | Transmissão do resultado para o próximo neurônio. |

### O Modelo de McCulloch-Pitts (MCP)

Matematicamente, o neurônio  pode ser descrito pela equação:

Onde:

* : **Campo local induzido** (potencial de ativação).
* : **Função de Ativação** (ex: Degrau, Sigmóide, ReLU).

---

## 3. Processos e Regras de Aprendizagem (Haykin)

A aprendizagem é o processo de ajuste dos pesos sinápticos. Existem três regras principais citadas no texto-base:

1. **Correção de Erro:** Ajusta os pesos com base na diferença entre a saída real e a desejada (erro).
2. **Aprendizagem de Hebb:** Postula que se dois neurônios em ambos os lados de uma sinapse são ativados simultaneamente, a força daquela sinapse aumenta ("Neurônios que disparam juntos, conectam-se juntos").
3. **Aprendizagem Competitiva:** Os neurônios de saída competem entre si; apenas o neurônio "vencedor" tem seus pesos ajustados.

---

## 4. Paradigmas e Tarefas de Aprendizagem

### Paradigmas (Como a rede aprende)

* **Supervisionado:** Utiliza um "professor" (dados rotulados). A rede tenta minimizar o erro em relação ao gabarito.
* **Não Supervisionado:** Não há rótulos. A rede busca padrões intrínsecos nos dados (auto-organização).
* **Por Reforço:** Aprendizado baseado em crítica (recompensas ou punições) após uma sequência de ações.

### Tarefas (O que a rede resolve)

De acordo com a Seção 1.9 do Haykin, as principais aplicações são:

* **Associação de Padrões:** Recuperação de dados a partir de entradas incompletas ou ruidosas.
* **Reconhecimento de Padrões (Classificação):** Atribuição de classes (ex: identificar objetos em imagens).
* **Aproximação de Funções:** Estimar valores contínuos (regressão).
* **Controle:** Manter sistemas dinâmicos dentro de parâmetros desejados.

---

## 💡 Notas para o Quiz

* **Conhecimento:** Não está no código, está nos **pesos**.
* **Diferença Fundamental:** O neurônio biológico é químico/contínuo; o MCP é uma abstração matemática discreta.
* **Sinal de Erro:** É a bússola para o ajuste de pesos na aprendizagem supervisionada.

---

### 💻 Laboratório: Validando a Lógica de Pesos

Use este pequeno script no VS Code para visualizar como o peso altera a importância de uma entrada:

```python
def teste_neuronio(entrada, peso, bias):
    soma_ponderada = (entrada * peso) + bias
    # Função de Ativação Degrau
    saida = 1 if soma_ponderada > 0 else 0
    return saida

# Cenário: Decidir se vou à praia (Entrada 1 = Sol, Peso = Importância)
print(f"Com Sol e alta importância: {teste_neuronio(1, 10, -5)}") # Retorna 1
print(f"Com Sol mas baixa importância: {teste_neuronio(1, 2, -5)}")  # Retorna 0

```

---

**Links de Referência:**

* [Vídeo Aula 01 - Introdução](https://www.youtube.com/watch?v=kzFqGhK8Q2s)
* *Haykin, S. Redes Neurais: Princípios e Prática. Capítulo 1.*