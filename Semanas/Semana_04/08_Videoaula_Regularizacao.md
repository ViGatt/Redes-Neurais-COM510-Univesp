# Semana 04: Métodos Otimizados e Regularização (Videoaula 11)

Nesta aula, consolidamos as soluções práticas para dois dos maiores problemas no treinamento de Redes Neurais: as dificuldades de encontrar o ponto mínimo do erro na função de custo (otimização) e a necessidade de evitar o *overfitting* (regularização).

## 1. Algoritmos Otimizados (Além do SGD)

O método do Gradiente Descendente possui limitações críticas em cenários reais:
* Não temos a informação completa sobre a "paisagem" da função de erro (superfície de custo).
* A rede frequentemente encontra **Mínimos Locais** (vales rasos), **Plateaus** (regiões muito planas onde o aprendizado estagna) e **Oscilações** (zigue-zagues descontrolados).

A literatura propôs algoritmos mais inteligentes para adaptar a taxa de aprendizagem dinamicamente durante o treinamento:

### A. RMSProp (Root Mean Squared Propagation)
* **Origem:** Proposto informalmente por Geoffrey Hinton (o "pai" do Deep Learning).
* **Mecanismo:** Em vez de usar uma taxa fixa, ele calcula a **média móvel do quadrado dos gradientes** para cada peso individualmente.
* **Efeito:** Se um peso está sofrendo **grandes variações** (oscilando muito), o algoritmo divide o passo por um valor alto, atuando como um "amortecedor". Se o peso apresenta **pequenas variações** constantes, ele amplifica o passo, acelerando o aprendizado nos *plateaus*.

### B. Adam (Adaptive Moment Estimation)
* **Origem:** Proposto por Kingma & Ba (2014), tornou-se rapidamente o padrão ouro na indústria.
* **Mecanismo:** É essencialmente a fusão perfeita. Consiste numa extensão do RMSProp (que adapta a escala de cada peso) **adicionando o termo de Momentum** (que preserva a inércia da direção).

---

## 2. Técnicas de Regularização

A regularização é o conjunto de técnicas utilizadas para lidar com o problema da Alta Variância (quando a rede sofre *overfitting* e perde a capacidade de generalizar).

### A. Regularização L2 e L1
Adicionam penalidades diretas à função de custo (Loss) caso a rede tente criar pesos sinápticos muito grandes:
* **Regularização L2 (Decaimento de Pesos):** Soma o **quadrado** dos pesos à função de custo. Pune severamente os pesos altos, forçando a rede a distribuir a "responsabilidade" da decisão por todo o modelo.
* **Regularização L1:** Soma o valor **absoluto** dos pesos à função de custo. A grande diferença do L1 é que ele tende a zerar completamente os pesos menos importantes, atuando não apenas como regularizador, mas como um mecanismo de **seleção de atributos** (*Feature Selection*).

### B. Dropout
Uma intervenção direta na arquitetura da rede durante o treinamento:
* **Mecanismo:** Desativa (ignora) uma porcentagem de neurônios aleatoriamente a cada nova época de treino.
* **Efeito:** Evita que um "único" neurônio ou grupo de neurônios decore um padrão específico. Ao desligar unidades, a carga de aprendizado é forçadamente distribuída pelos outros pesos da rede, forçando o modelo a criar redundância e ser mais robusto a ruídos.
* *Nota:* O parâmetro principal é a "probabilidade de ativação" das unidades (normalmente chamada de probabilidade $p$ ou taxa de *dropout*).

---

## 3. Outras Melhorias para Generalização

A aula encerra listando outras estratégias clássicas que o engenheiro deve ter em mente:
* **Mais Dados Representativos:** A cura definitiva para o overfitting.
* **Data Augmentation (Aumento Artificial de Dados):** Aplicar transformações geométricas/ruído aos dados existentes para multiplicar a base.
* **Parada Prematura (Early Stopping):** Monitorar o erro de validação. Quando o erro de treino continua a cair, mas o erro de validação começa a subir, o treinamento deve ser interrompido imediatamente.
* **Adequação da Função de Custo:** Escolher a função (Loss) correta. (Ex: MSE para regressão, Cross-Entropy para classificação).

---

## Checkpoint 
1. **O que difere o Adam do RMSProp tradicional?** O Adam incorpora o termo de Momentum aos cálculos adaptativos de escala do RMSProp.
2. **Como a Regularização L1 atua na seleção de atributos?** Ao penalizar o valor absoluto, ela tende a empurrar os pesos das características menos úteis exatamente para zero, "desligando-os" do modelo final.
3. **Qual é a consequência de aplicar o Dropout na rede?** A rede é forçada a não depender de neurônios específicos (co-adaptação), desenvolvendo caminhos mais robustos para a resolução do problema.

---