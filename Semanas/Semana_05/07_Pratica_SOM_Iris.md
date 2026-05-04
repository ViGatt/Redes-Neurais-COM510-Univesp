# 🛠️ Semana 05: Aplicação Prática da Rede SOM (Videoaula 15)

Nesta aula, o conteúdo foca na implementação prática de Mapas Auto-organizáveis (SOM) utilizando a linguagem Python e a biblioteca **MiniSom**. O objetivo é demonstrar como a rede agrupa dados reais e como a visualização auxilia na interpretação de padrões.

## 1. O Pacote MiniSom
O **MiniSom** é uma implementação minimalista baseada em NumPy para Mapas Auto-organizáveis. Ele é amplamente utilizado por sua simplicidade e eficiência na construção de grades neuronais.

### Configuração Básica:
Para criar uma rede, definimos os seguintes parâmetros principais:
* **x, y:** Dimensões da grade (ex: 10x10 = 100 neurônios).
* **input_len:** Número de atributos (dimensões) do dado de entrada.
* **sigma:** Raio da função de vizinhança (abertura da curva gaussiana).
* **learning_rate:** Taxa de aprendizado inicial ($\eta$).

---

## 2. Estudo de Caso: Dataset Iris
A aplicação utiliza o conjunto de dados *Iris*, que consiste em 150 amostras de flores divididas em 3 classes (Setosa, Versicolor e Virginica). Cada flor possui 4 atributos: comprimento e largura da sépala e da pétala.

### Preparação dos Dados:
* **Conversão:** Rótulos categóricos (nomes das flores) são convertidos em valores numéricos (0, 1, 2) para facilitar a plotagem de mapas de distribuição.
* **Análise de Correlação:** Antes do treino, é comum gerar um mapa de calor de correlação para entender como os atributos se relacionam (ex: comprimento e largura da pétala costumam ter alta correlação).

---

## 3. Visualizações e Métricas de Qualidade
Após o treinamento, o SOM gera mapas que permitem "ver" as separações entre as classes de flores:

* **U-Matrix (Unified Distance Matrix):** Calcula a similaridade entre um neurônio e seus vizinhos. É utilizada para encontrar as "fronteiras" entre agrupamentos.
* **Hit Map:** Indica quantos padrões de entrada foram associados a cada neurônio. Neurônios com zero "hits" indicam regiões vazias do espaço de atributos.
* **Heat Maps (Mapas de Pesos):** Mostram a distribuição dos pesos de cada atributo no grid. Ajudam a identificar quais variáveis influenciam cada cluster.

---

## 💻 Laboratório: Implementação com MiniSom

No seu VS Code, visualize o arquivo **`Semanas\Semana_05\Univesp_Semana05_SOM_videoaula_15.ipynb`** para simular os passos do Notebook fornecido


---

## Resumo para Revisão
* **MiniSom:** Biblioteca minimalista em Python focada em performance via NumPy.
* **Dataset Iris:** O SOM consegue isolar a classe *Setosa* (linearmente separável), mas as classes *Versicolor* e *Virginica* apresentam sobreposição no mapa devido à similaridade estatística.
* **Métricas:** O Erro de Quantização mede a precisão da representação, enquanto o Erro Topográfico mede a preservação das relações espaciais dos dados.