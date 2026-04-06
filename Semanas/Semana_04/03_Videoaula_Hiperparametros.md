# ⚙️ Semana 04: Configuração de Hiperparâmetros e Aceleração

Esta videoaula foca em estratégias práticas para definir a arquitetura (topologia) ideal da rede MLP e as técnicas para acelerar o processo de convergência dos pesos.

## 1. O Desafio da Topologia
Como os problemas reais possuem múltiplas dimensões (muitos atributos), é impossível visualizar a distribuição dos dados em um gráfico 2D para "adivinhar" quantos neurônios usar. A definição da topologia exige métodos específicos:
* **Força Bruta / Busca em Grade (Grid Search):** Testar exaustivamente várias combinações de camadas e neurônios.
* **Métodos de Otimização:** Utilizar Algoritmos Genéticos ou *Simulated Annealing* para automatizar a busca pela melhor arquitetura.
* **Configuração Empírica / Heurística:** Iniciar com a topologia mínima (linear). Se o erro for alto, amplia-se o número de parâmetros; se for baixo, o modelo serve como uma boa base inicial.

---

## 2. O Dilema Viés-Variância (Bias vs. Variance)
O ajuste da rede é um cabo de guerra entre a capacidade de aprender e a capacidade de generalizar. 

* **Alto Viés (Underfitting):** A rede é muito simples para a complexidade do problema.
    * *Sintoma:* O erro é alto logo no **conjunto de treinamento**.
    * *Solução:* Aumentar a quantidade de parâmetros (mais neurônios/camadas) ou treinar por mais tempo.
* **Alta Variância (Overfitting):** A rede é complexa demais e decorou os dados.
    * *Sintoma:* O erro de treinamento é baixo, mas o erro no **conjunto de validação** é alto.
    * *Solução:* Obter mais dados reais, aplicar regularização (como Dropout ou decaimento $L_2$) ou reduzir o tamanho da topologia.

---

## 3. Acelerando o Treinamento
Para problemas do mundo real, treinar uma rede pode levar dias. A aula destaca técnicas para otimizar esse tempo:

### A. Modos de Treinamento
* **Padrão (Estocástico):** Os parâmetros são ajustados a cada exemplo individual (muito ruidoso).
* **Em Lote (Batch):** Os parâmetros são ajustados apenas uma vez no final da época, somando o erro de toda a base (lento e consome muita memória).
* **Mini-lote (Mini-batch):** O padrão ouro da engenharia de IA. Divide os dados em pequenos subconjuntos (ex: lotes de 32 ou 64 exemplos) e atualiza os pesos a cada mini-lote, equilibrando velocidade e estabilidade.

### B. Inicialização e Taxa de Aprendizagem ($\eta$)
* **Pesos:** Devem ser iniciados com valores pequenos e aleatórios. Uma boa prática é ponderar esse valor inicial pela quantidade de sinapses que o neurônio recebe (para evitar que a soma da ativação exploda).
* **Decaimento da Taxa ($\eta$):** Utilizar uma taxa de aprendizagem decrescente costuma ser mais eficiente que uma fixa. A rede dá passos largos no início e passos curtos/finos quando se aproxima do mínimo. A fórmula clássica de decaimento ao longo do tempo $t$ é:

$$
\eta(t) = \frac{\eta_0}{1 + \left(\frac{t}{\tau}\right)}
$$

### C. O Termo de Momentum ($\alpha$)
Gera uma "inércia" na descida do gradiente, reduzindo o perigo de instabilidade (oscilações fortes). 

$$
\Delta w^t = \eta \cdot \delta + \alpha \cdot \Delta w^{t-1}
$$

---

## Laboratório: Mini-batch, Momentum e Decaimento no PyTorch

Como trabalha frequentemente com Python e modelagem no seu ambiente, a conversão dessa teoria para o código moderno (PyTorch) envolve o uso da classe `DataLoader` e dos *Schedulers* no seu VS Code, como mostrado no arquivo 

---

## Checkpoint 
1. **Qual a vantagem do treinamento por Mini-lote?** Ele combina a eficiência computacional (usando vetorização) com a injeção de ruído útil do método estocástico para escapar de mínimos locais.
2. **Qual é o sintoma clássico de Overfitting (Alta variância)?** O erro de treinamento é muito baixo, mas o erro do conjunto de validação começa a subir.
3. **Por que utilizamos o decaimento da taxa de aprendizagem?** Para permitir avanços rápidos nas primeiras épocas (quando estamos longe do mínimo) e ajustes finos nas épocas finais, evitando oscilar ao redor da solução ótima.