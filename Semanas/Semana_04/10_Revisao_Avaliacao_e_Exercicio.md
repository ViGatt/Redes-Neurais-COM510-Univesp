# ✅ Semana 04: Revisão de Conceitos (Quiz e Avaliação)

Este documento consolida os principais conceitos testados nas atividades avaliativas da Semana 04, servindo como um guia definitivo sobre diagnóstico, topologia e otimização de Redes MLP.

## 1. Diagnóstico de Modelos: Generalização, Overfitting e Underfitting

A análise da curva de erro é o que guia o trabalho do engenheiro ao ajustar hiperparâmetros.

* **Capacidade de Generalização:** É aferida utilizando o **conjunto de validação**. Um modelo generaliza bem quando o erro de validação atinge valores baixos e acompanha a queda do erro de treinamento. O conjunto de teste só entra no final para atestar a acurácia, nunca para guiar o treinamento.
* **Overfitting (Sobreajuste):** Ocorre quando o modelo apresenta um desempenho excelente no treino, mas falha miseravelmente no teste/validação (decorou os dados).
    * *Solução:* Reduzir a complexidade da rede, aplicar *Dropout* ou *Weight Decay* (L2).
* **Underfitting (Subajuste):** Ocorre quando a rede não consegue aprender adequadamente nem os dados de treino (erro permanece alto). 
    * *Solução:* **Aumentar a complexidade da topologia**, adicionando mais camadas e neurônios para ampliar a capacidade de representação matemática do modelo.

---

## 2. Heurísticas de Topologia e Arquitetura

A definição dos hiperparâmetros (número de camadas e neurônios) é um processo empírico que depende diretamente dos dados e do conhecimento prévio do desenvolvedor.

* **O Papel das Camadas:** O número de camadas dita a profundidade da rede e sua capacidade de resolver problemas complexos.
* **O Papel dos Neurônios:** Ajustar a quantidade de neurônios dentro de cada camada ajuda a moldar a estrutura fina para lidar com a dimensionalidade do problema.
* **Geometria da Classificação:** Para problemas bidimensionais não-linearmente separáveis (ex: uma classe dentro de um triângulo formado por outra classe), é necessário usar unidades ocultas para traçar múltiplas retas de fronteira. 
    * *Exemplo prático:* Uma topologia `[2; 3; 1]` (2 entradas, 3 neurônios ocultos traçando 3 retas, e 1 saída julgando a união delas) ou `[2; 5; 1]` são capazes de resolver o problema.

---

## 3. Estratégias de Otimização e Aceleração

Para acelerar a convergência do algoritmo de retropropagação sem perder a estabilidade, aplicamos as seguintes heurísticas:

1. **Taxas Dinâmicas Individuais:** Associar uma taxa de aprendizagem individual para cada peso (exatamente o que algoritmos como RMSProp e Adam fazem).
2. **Ajuste Temporal:** Alterar a taxa de aprendizagem base ao longo das épocas (Decaimento).
3. **Leitura do Gradiente:** * Ampliar a taxa se a derivada se mantém constante (sinal de que a rede está descendo um platô longo).
    * Reduzir a taxa se o sinal da derivada oscila/alterna (sinal de que a rede está zigue-zagueando e pulando o mínimo).
4. **SGD vs. Adam:** Ambos são algoritmos de primeira ordem, mas a principal diferença é que o **Adam utiliza médias móveis** para obter uma estimativa dinâmica tanto do momento (inércia) quanto do gradiente (escala), tornando a convergência drasticamente mais rápida.
* *Nota:* O número de neurônios **nunca** é alterado dinamicamente durante o loop de treinamento. A topologia é fixa após instanciada.

---

## 4. Técnicas de Regularização

Quando a rede é muito complexa, utilizamos técnicas para forçar a simplicidade e distribuir o conhecimento.

* **Dropout:** Inativa um subconjunto de neurônios nas camadas ocultas de forma aleatória durante o treino. Isso impede a co-adaptação (a rede aprende a não depender excessivamente de um único neurônio) e tem um efeito prático de redução de *overfitting* muito similar à Regularização L2.
* **Weight Decay (L2):** Penaliza os pesos grandes na função de custo, reduzindo a influência de parâmetros excessivos.
* **Poda da Rede (Pruning):** É uma técnica de redução estrutural. Consiste em começar com uma rede MLP grande que já atingiu um desempenho adequado, e então **eliminar pesos sinápticos de forma seletiva e ordenada** (cortando conexões inúteis para melhorar a eficiência e generalização final).

---