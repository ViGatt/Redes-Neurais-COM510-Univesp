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

## 🚀 Como utilizar este repositório

1. Clone o projeto: `git clone https://github.com/ViGatt/Redes-Neurais-COM510-Univesp`
2. Navegue até a semana desejada em `/Semanas`.
3. Abra os arquivos `.md` para teoria ou execute os scripts `.py` para testes práticos.

> **Nota:** Este repositório é um registro pessoal de evolução acadêmica. 

### Dica para o VS Code:

Para que as equações matemáticas acima (em LaTeX) apareçam corretamente no seu VS Code, lembre-se de instalar a extensão **Markdown Preview Enhanced**.