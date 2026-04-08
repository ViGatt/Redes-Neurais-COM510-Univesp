# ✅ Semana 04: Resumo Geral e Revisão de Avaliações

Este documento consolida a visão geral da quarta semana de estudos, juntamente com as "regras de ouro" testadas nas atividades avaliativas e a dinâmica do Exercício de Apoio.

## 🌟 Visão Geral da Semana 04

A Semana 04 marcou a transição da teoria matemática pura para a **Engenharia de Machine Learning** aplicada. Saímos da fase de "fazer a rede funcionar" para a fase de "fazer a rede ser eficiente e confiável no mundo real". 

O aprendizado desta semana foi sustentado por três pilares fundamentais:

1. **Ajuste de Topologia (A Arquitetura):** Entendemos que configurar hiperparâmetros (como o número de camadas e neurônios) é um cabo de guerra entre o viés e a variância. Redes simples demais causam *Underfitting* (subajuste), enquanto redes complexas demais causam *Overfitting* (sobreajuste).
2. **Otimização Avançada (O Motor):** Vimos que o Gradiente Descendente Estocástico (SGD) tradicional é lento e instável. A engenharia moderna resolve isso com o treinamento em **Mini-lotes**, a adição de **Momentum** (inércia direcional) e o uso de taxas de aprendizagem adaptativas, culminando no estado da arte: o otimizador **Adam** (que funde Momentum e RMSProp).
3. **Regularização (O Freio):** Aprendemos as ferramentas para impedir que a rede simplesmente "decore" os dados de treino. Isso inclui monitorar a rede com o conjunto de Validação (*Early Stopping*), penalizar pesos excessivamente grandes (*L1/L2 Weight Decay*), inativar neurônios aleatoriamente para forçar robustez (*Dropout*), podar conexões inúteis (*Pruning*) e gerar dados sintéticos (*Data Augmentation*).

---

## 1. Diagnóstico de Modelos: Generalização, Overfitting e Underfitting

A leitura das curvas de erro é a bússola para os ajustes da rede:

* **Capacidade de Generalização:** É aferida exclusivamente utilizando o **conjunto de validação**. A generalização é garantida quando o erro de validação atinge valores baixos e aproxima-se do erro de treinamento. *Nota: O conjunto de teste (externo) não deve guiar o treinamento, ele atesta a acurácia final.*
* **Overfitting (Sobreajuste):** Ocorre quando o modelo apresenta uma precisão excelente no treino, mas um desempenho fraco/insatisfatório no teste. A rede "memorizou" os ruídos.
    * *Tratamento:* Aplicar técnicas de regularização (como *Weight Decay* / L2, que reduz a influência de parâmetros elevados) ou reduzir o número de camadas/neurônios.
* **Underfitting (Subajuste):** A rede não aprende adequadamente e a precisão fica baixa em todos os conjuntos.
    * *Tratamento:* **Aumentar a complexidade da topologia**, adicionando mais camadas ocultas e neurônios para permitir a representação de padrões mais complexos.

## 2. Configuração de Topologia e Arquitetura

O processo de definição dos hiperparâmetros não tem fórmula pronta; é um processo **empírico**, dependente dos dados e do especialista.

* **A Estrutura:** Primeiramente, define-se o número de **camadas** (influencia a profundidade) e, em seguida, o número de **neurônios** em cada camada. A topologia não é alterada ao longo do *loop* de treinamento.
* **Topologia para Classificação Geométrica:** Problemas bidimensionais não-linearmente separáveis (ex: cruzes vermelhas fechadas dentro de um triângulo) exigem unidades ocultas para criar fronteiras. Um modelo `[2 entradas; 3 neurônios ocultos; 1 saída]` é capaz de isolar o triângulo, pois seus 3 neurônios ocultos traçam as 3 retas necessárias.
* **Poda da Rede (Pruning):** Uma técnica para minimizar redes. Começa-se com um MLP grande que tenha um bom desempenho, da qual passam a ser eliminados (ou reduzidos) pesos sinápticos de forma seletiva e ordenada.

## 3. Otimizadores e Regularização

* **Heurísticas para Acelerar a Convergência:**
    1. Ajustar a taxa de aprendizagem ao longo do treinamento (decaimento).
    2. Associar uma taxa de aprendizagem individual a cada peso.
    3. Ampliar a taxa se o sinal da derivada se mantiver constante e reduzi-la se o sinal ficar oscilando (zigue-zague).
* **SGD vs. Adam:** Ambos são algoritmos de primeira ordem, mas o grande diferencial é que o **Adam utiliza médias móveis** para obter uma estimativa dinâmica do *momentum* e do gradiente.
* **O Efeito do Dropout:** Inativa um subconjunto aleatório de neurônios ocultos durante o treino. A camada posterior aprende a não depender excessivamente de nenhum neurônio específico. Possui um efeito prático de combate ao *overfitting* altamente eficaz (semelhante ao L2).

## 4. O Exercício de Apoio (MLP no Colab)

No *Jupyter Notebook* explorado (`Univesp_Semana04_MLP_V2.ipynb`), toda essa teoria é materializada num problema de regressão:

1. **Separação de Dados:** A base é dividida em Treino, Validação e Teste para permitir um fluxo metodológico correto.
2. **Instanciação (Topologia):** Utiliza a classe `nn.Sequential` do PyTorch para empilhar camadas `Linear` intercaladas com quebras não-lineares (`Tanh`).
3. **Métrica:** Avalia o Erro Quadrático Médio (`MSELoss`).
4. **Desafio Prático:** O material baseia-se em alterar o otimizador padronizado pelo professor (`SGD`) para utilizar os hiperparâmetros modernos de decaimento do `Adam`, monitorando nos gráficos as perdas de Validação vs. Treino para identificar o momento exato em que o *Overfitting* começa a ocorrer.
