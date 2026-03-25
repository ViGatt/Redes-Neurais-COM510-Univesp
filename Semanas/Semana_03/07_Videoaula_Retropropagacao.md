# 🔄 Semana 03: Fundamentos e Derivação da Retropropagação

A Videoaula 08 explica o mecanismo que permite treinar os Perceptrons de Múltiplas Camadas (MLP). Sem a retropropagação, não saberíamos como ajustar os pesos das camadas ocultas, pois não temos uma "resposta desejada" explícita para elas.

## 1. O Problema Central

* **A Dúvida:** Como atualizar os neurônios das camadas escondidas se o erro só é visível na camada de saída?
* **A Solução:** O algoritmo de retropropagação (*Backpropagation*) resolve isso utilizando a regra da cadeia para derivar o erro de trás para frente.
* **Impacto Histórico:** Seu desenvolvimento permitiu que redes com múltiplas camadas pudessem ser treinadas para resolver problemas não-lineares, sendo o grande responsável pelo ressurgimento do interesse em IA na década de 1980.

---

## 2. Minimização do Erro e o Gradiente Descendente

O processo de aprendizagem baseia-se na minimização da energia do erro ($E$) pelo método do gradiente descendente. O erro é calculado usando o Erro Quadrático Médio:

$$
E(n) = \frac{1}{2} \sum_{k} (d_k(n) - y_k(n))^2
$$

A regra de atualização de um peso $w_{ki}$ caminha na direção oposta ao gradiente:

$$
\Delta w_{ki} = -\eta \frac{\partial E}{\partial w_{ki}}
$$

*(Lembrando que $\eta$ é a taxa de aprendizagem).*

---

## 3. A Derivação e o Gradiente Local ($\delta$)

A aula destrincha como aplicar a Regra da Cadeia para resolver essa derivada parcial. O resultado final nos dá a regra de atualização universal:

$$
\Delta w_{kj} = \eta \cdot \delta_k \cdot x_j
$$

A diferença crucial está em como o **Gradiente Local ($\delta$)** é calculado dependendo da posição do neurônio:

### **Para um neurônio na Camada de Saída ($k$):**
O cálculo é direto, pois conhecemos o erro ($e_k = d_k - y_k$):

$$
\Delta w_{kj} = \eta \cdot f'(v_k) \cdot e_k \cdot x_j
$$

### **Para um neurônio na Camada Oculta ($j$):**
O erro não é conhecido, então o neurônio $j$ assume uma parcela de "culpa" proporcional aos pesos que o conectam aos neurônios de saída $k$ que ele ajudou a ativar:

$$
\Delta w_{ji} = \eta \cdot f'(v_j) \left( \sum_{k} w_{kj}\delta_k \right) x_i
$$

*(Onde $f'$ é a derivada da função de ativação do neurônio).*

---

## 4. O Algoritmo em Duas Fases

O algoritmo de retropropagação é executado iterativamente em duas grandes fases (após a inicialização aleatória dos pesos):

1. **Feedforward (Fase Adiante / Propagação):**
   * As entradas se propagam pela rede, camada a camada, da entrada até a saída.
   * Os pesos permanecem fixos.
   * Ao final, calcula-se o erro da rede.
2. **Feedback (Fase de Retorno / Retropropagação):**
   * Os erros (através dos gradientes $\delta$) se propagam camada a camada, da saída **de volta** para a entrada.
   * Os pesos são atualizados durante este processo inverso.

> **Ciclo de Vida:** Esse processo (aplicar o padrão, propagar, calcular erro, retropropagar e ajustar) se repete para todos os padrões de treinamento até que o erro seja aceitável ou o número máximo de épocas seja atingido.

---

## Checkpoint
* **Por que usamos a derivada da função de ativação ($f'$)?** Porque é o resultado da aplicação da Regra da Cadeia para encontrar como a mudança no peso afeta a mudança no erro final. É por isso que funções como a Sigmoide e a ReLU precisam ser diferenciáveis.
* **Qual é o "motor" das atualizações ocultas?** O somatório $\left(\sum w_{kj}\delta_k\right)$, que distribui o erro dos neurônios da frente para os neurônios de trás.
