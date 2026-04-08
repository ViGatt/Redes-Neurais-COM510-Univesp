# 🔄 Semana 03: Resumo Geral - MLP e Backpropagation

Esta semana abordou a solução para o problema do XOR e o renascimento das Redes Neurais nas décadas de 1980 e 1990.

## 1. O Perceptron de Múltiplas Camadas (MLP)
A arquitetura que quebrou a barreira da separabilidade linear.
* **A Solução do XOR:** Ao adicionar camadas "Ocultas" (Hidden Layers) entre a entrada e a saída, a rede ganha a capacidade de curvar o espaço e traçar múltiplas retas de decisão.
* **Quebra de Linearidade:** Para que múltiplas camadas funcionem, é estritamente obrigatório o uso de **funções de ativação não-lineares diferenciáveis** (como Sigmoide, Tanh ou ReLU). Se usássemos apenas funções lineares, a matemática faria a rede profunda colapsar e se comportar como um único neurônio inútil.

## 2. O Algoritmo de Retropropagação (Backpropagation)
O "motor" matemático que permite treinar as camadas ocultas.
* **O Dilema:** Sabíamos o erro da saída, mas como calcular o erro dos neurônios do meio, já que não tínhamos um gabarito para eles?
* **A Solução (Regra da Cadeia):** O algoritmo funciona em duas fases:
    1. **Fase Forward (Para frente):** O sinal viaja da entrada para a saída. Os pesos estão travados. Calcula-se o erro final.
    2. **Fase Backward (Retropropagação):** Usa-se derivadas parciais para distribuir a "culpa" do erro de trás para frente. Cada neurônio oculto ajusta seus pesos proporcionalmente ao impacto que ele teve no erro da camada seguinte.

## 3. Otimização e a Superfície de Custo
Diferente do Adaline (que tem uma função de custo em forma de "tigela" - convexa), o MLP tem funções de custo **não-convexas**, cheias de montanhas e vales.
* **SGD (Stochastic Gradient Descent):** Atualizar os pesos exemplo a exemplo insere um "ruído" útil no aprendizado, ajudando o algoritmo a escapar de mínimos locais (vales rasos) em busca do mínimo global (o fundo real do oceano).
* **Momento:** Adição de uma inércia ao passo do gradiente para acelerar a passagem por áreas muito planas (plateaus) e evitar oscilações severas.