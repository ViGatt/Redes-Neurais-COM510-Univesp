# 🧠 Redes Neurais (COM510) - Engenharia da Computação

Repositório dedicado ao armazenamento de notas de aula, trechos de código e experimentos práticos da disciplina **COM510 - Redes Neurais (Turma 001)**. O objetivo é explorar desde os fundamentos dos sistemas conexionistas até a base dos modelos de *Deep Learning*.

## 📌 Sobre a Disciplina

A disciplina aborda o desenvolvimento de modelos de inteligência artificial inspirados no sistema nervoso humano. O foco principal é entender a evolução histórica, os métodos de treinamento e as aplicações práticas de Redes Neurais em áreas como:

* **Visão Computacional**
* **Processamento de Linguagem Natural (NLP)**
* **Reconhecimento de Fala**

## 🛠️ Tecnologias e Ferramentas

* **IDE:** Visual Studio Code
* **Linguagem:** Python 3.x
* **Bibliotecas Principais:** NumPy, Matplotlib (planejado), Scikit-learn (planejado)
* **Documentação:** Markdown & LaTeX (para modelagem matemática)

## 📂 Organização do Repositório

| Pasta | Descrição |
| --- | --- |
| `00_Recursos/` | Materiais de apoio, ementa e PDFs da disciplina. |
| `Semanas/` | Notas de estudo e códigos divididos por semana letiva. |
| `Laboratorios/` | Pequenos experimentos e testes de conceitos. |

## 📅 Cronograma de Estudos (Semana 1)

### **Introdução e Modelagem Matemática**

Nesta etapa inicial, o foco é a transição do biológico para o artificial.

* **Fundamentos:** História e evolução dos sistemas conexionistas.
* **Modelo Biológico:** Como o neurônio humano processa sinais.
* **Modelo Matemático:** Representação computacional do neurônio.

A saída de um neurônio artificial (Perceptron) pode ser resumida pela equação:

$$y = \phi \left( \sum_{i=1}^{n} w_i x_i + b \right)$$

Onde:

* : $w$: Pesos (sinapses)
* : $x$: Entradas (estímulos)
* : $b$: Bias (viés/ajuste)
* : $\phi$: Função de ativação

---

## 📅 Cronograma de Estudos (Semana 2)

### **Arquiteturas, Preparação de Dados e Modelos Lineares**

Nesta etapa, avançamos para a organização estrutural das redes e as técnicas fundamentais de engenharia de dados.

* **Arquiteturas de Rede:** Classificação em camadas (única, múltiplas camadas e redes recorrentes).
* **Engenharia de Dados:** Metodologias de divisão (Treino, Validação e Teste), Validação Cruzada e técnicas de Normalização.
* **Perceptron e Adaline:** Estudo dos primeiros modelos neurais e suas aplicações em problemas linearmente separáveis.

O ajuste de pesos (aprendizado) do **Adaline**, baseado na Regra Delta (Mínimos Quadrados Médios), busca minimizar o erro quadrático:

$$E = \frac{1}{2} \sum_{i} (d_i - u_i)^2$$

Onde:

* $d$: Resposta desejada (target).
* $u$: Campo local induzido (saída linear antes da ativação).
* $E$: Função de custo a ser minimizada.

---

Para mantermos a consistência e a qualidade do seu repositório no GitHub, aqui está a estrutura formatada para a **Semana 3**. Esta semana marca um dos pontos mais importantes do curso: a transição para redes profundas e o algoritmo que permite treiná-las.

Copie e cole este bloco logo abaixo do cronograma da Semana 2 no seu `README.md`:

---

## 📅 Cronograma de Estudos (Semana 3)

### **Multilayer Perceptron (MLP) e Backpropagation**

Nesta semana, superamos as limitações dos modelos lineares (como o Perceptron simples e o Adaline) introduzindo camadas ocultas e o principal algoritmo de treinamento de redes neurais artificiais.

* **Arquitetura MLP:** Estrutura em múltiplas camadas (Entrada, Ocultas e Saída), tipos de neurônios e funções de ativação essenciais.
* **O Problema Clássico do XOR:** Demonstração prática de como a rede MLP consegue resolver problemas não-linearmente separáveis, compreendendo o que cada neurônio aprende na camada oculta.
* **Algoritmo de Retropropagação (Backpropagation):** O coração do aprendizado profundo. Derivação matemática e regra de atualização dos pesos distribuindo o erro da saída de volta para as camadas ocultas.

A essência da atualização de pesos no Backpropagation baseia-se na regra da cadeia para o cálculo do gradiente local ($\delta$):

$$\Delta w_{ji}(n) = \eta \cdot \delta_j(n) \cdot y_i(n)$$

Onde:

* $\eta$: : Taxa de aprendizagem.
* $\delta_j$: Gradiente local do neurônio  (calculado de forma diferente para a camada de saída e para as camadas ocultas).
* $y_i$ : Sinal de saída do neurônio  da camada anterior.
* **Laboratório Prático:** Desenvolvimento de redes MLP padrão para problemas de **Classificação** e **Regressão**, utilizando Python e o ambiente Google Colab / Jupyter Notebooks.

---


## Como utilizar este repositório

1. Clone o projeto: `git clone https://github.com/ViGatt/Redes-Neurais-COM510-Univesp`
2. Navegue até a semana desejada em `/Semanas`.
3. Abra os arquivos `.md` para teoria ou execute os scripts `.py` para testes práticos.

> **Nota:** Este repositório é um registro pessoal de evolução acadêmica. 

### Dica para o VS Code:

Para que as equações matemáticas acima (em LaTeX) apareçam corretamente no seu VS Code, lembre-se de instalar a extensão **Markdown Preview Enhanced**.