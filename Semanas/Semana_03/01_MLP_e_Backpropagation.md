
# Semana 03: Perceptrons de Múltiplas Camadas (MLP)
> S3 - Texto-base 1 – Redes Neurais: princípios e prática (leia Capítulo 4 - Seções 4.1, 4.2, 4.5 e 4.7) | Simon Haykin 


As redes MLP representam uma generalização do Perceptron de camada única, utilizando camadas ocultas e funções de ativação não-lineares para aprender mapeamentos complexos.

## 1. Arquitetura da Rede MLP (Seções 4.1 e 4.2)

Uma rede MLP padrão possui três características distintivas que a diferenciam dos modelos lineares:

1. **Funções de Ativação Não-Lineares:** Diferente do Perceptron (que usa a função degrau), o MLP utiliza funções não-lineares e **diferenciáveis** (como a Sigmoide ou Tangente Hiperbólica). Isso é essencial para que o algoritmo de treino funcione.
2. **Camadas Ocultas:** Um ou mais conjuntos de neurônios que não estão em contato direto com a entrada ou a saída. Eles permitem que a rede extraia estatísticas de ordem elevada.
3. **Alta Conectividade:** Geralmente, as redes são totalmente conectadas (*fully connected*), onde cada neurônio de uma camada se conecta a todos os neurônios da camada seguinte.

---

## 2. O Algoritmo de Retropropagação (Seção 4.5)

O treinamento da rede MLP é feito de forma supervisionada através do **Backpropagation**. O processo ocorre em duas fases distintas:

### **A. Fase Direta (Forward Pass)**

* Os pesos da rede são fixos.
* O sinal de entrada se propaga camada por camada até a saída.
* É calculado o **sinal de erro** $e_j(n) = d_j(n) - y_j(n)$ na camada de saída.

### **B. Fase Indireta (Backward Pass)**

* O sinal de erro é propagado de volta, da saída para a entrada.
* Os pesos são ajustados para minimizar a energia do erro global.
* **Ajuste de Pesos:** Baseia-se na regra da cadeia para calcular o **gradiente local** ($\delta$).

#### **Equação do Gradiente Local ($\delta_j$):**

* **Para neurônios de saída:** O erro é direto.

$$\delta_j(n) = e_j(n) \cdot \phi'_j(v_j(n))$$


* **Para neurônios ocultos:** O erro é uma soma ponderada dos erros da camada seguinte.

$$\delta_j(n) = \phi'_j(v_j(n)) \cdot \sum_k \delta_k(n)w_{kj}(n)$$



---

## 3. Heurísticas para Melhor Desempenho (Seção 4.7)

O projeto de uma rede MLP é muitas vezes considerado uma "arte". O livro sugere alguns pontos para melhorar a convergência:

* **Taxas de Aprendizagem ($\eta$):** Neurônios nas últimas camadas tendem a ter gradientes locais maiores. Pode ser útil atribuir taxas menores para as últimas camadas e maiores para as iniciais.
* **Inversa da Raiz Quadrada:** Sugere-se que a taxa de aprendizagem de um neurônio seja inversamente proporcional à raiz quadrada do número de conexões sinápticas que ele recebe.
* **Conteúdo de Informação:** Deve-se priorizar exemplos de treino que resultem em maiores erros ou que sejam radicalmente diferentes dos já apresentados, para expandir a busca no espaço de pesos.


---

## Checkpoint 

* **Por que o Perceptron não resolve o XOR?** Porque o XOR não é linearmente separável. O MLP resolve através das camadas ocultas que criam novas representações dos dados.
* **Qual a importância da função de ativação ser diferenciável?** Sem a derivada, não conseguiríamos calcular o gradiente para atualizar os pesos das camadas ocultas.
* **Modo Sequencial vs. Lote:** O modo sequencial (padrão a padrão) costuma ser mais rápido para grandes conjuntos de dados redundantes.

