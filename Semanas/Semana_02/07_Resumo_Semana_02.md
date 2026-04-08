# 📈 Semana 02: Resumo Geral - Perceptron, Adaline e o XOR

Esta semana marcou a evolução dos neurônios estáticos para modelos capazes de aprender sozinhos com base em dados.

## 1. O Perceptron de Rosenblatt (1958)
O primeiro algoritmo de aprendizado supervisionado da história.
* **Mecanismo:** Utiliza a Regra de Correção de Erro. Se o neurônio erra a predição, os pesos são atualizados proporcionalmente ao erro e ao valor da entrada.
* **Teorema da Convergência:** Foi provado matematicamente que, se as classes do problema forem **Linearmente Separáveis** (podem ser divididas por uma única reta em 2D ou um hiperplano em nD), o Perceptron garantidamente encontrará a solução em um número finito de passos.

## 2. O Adaline e a Regra Delta (1960)
Desenvolvido por Widrow e Hoff, trouxe a rede neural para o domínio do Cálculo Contínuo.
* **A Grande Diferença:** Enquanto o Perceptron atualiza os pesos com base na saída binária (após a função de ativação degrau), o Adaline atualiza os pesos com base no erro do **somatório linear** (antes do degrau).
* **Regra Delta:** O aprendizado baseia-se na minimização do **Erro Quadrático Médio (MSE)** utilizando o método do **Gradiente Descendente**. É a base de toda a otimização moderna.

## 3. O Inverno da IA e o Problema do XOR (1969)
Marvin Minsky e Seymour Papert publicaram um livro provando as limitações matemáticas do Perceptron de camada única.
* **A Falha:** Um único neurônio linear não consegue resolver o problema do XOR (Ou Exclusivo), pois os dados dessa porta lógica não são linearmente separáveis (não dá para dividi-los com uma única reta).
* **Consequência:** Isso causou o primeiro "Inverno da IA", com corte massivo de financiamento em pesquisas de redes neurais, pois a comunidade acreditava que elas haviam chegado a um beco sem saída.