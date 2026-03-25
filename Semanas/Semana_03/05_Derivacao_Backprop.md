# 🧮 Semana 03: O Algoritmo de Retropropagação e as Duas Fases (Haykin)

Nesta etapa, destrinchamos a matemática por trás de como a rede MLP aprende, baseando-nos nas Seções 4.3 e 4.4 do livro-texto.

## 1. O Algoritmo de Retropropagação de Erro (Seção 4.3)

O objetivo do treinamento supervisionado é minimizar a energia do erro instantâneo da rede. O erro no neurônio $j$ da camada de saída na iteração $n$ é:

$$
e_j(n) = d_j(n) - y_j(n)
$$

A energia do erro total ($E$) é a soma dos erros quadráticos de todos os neurônios da camada de saída. Para minimizar $E$, aplicamos o método do gradiente descendente, ajustando os pesos na direção oposta ao gradiente. Isso resulta na **Regra Delta Generalizada**:

$$
\Delta w_{ji}(n) = \eta \cdot \delta_j(n) \cdot y_i(n)
$$

Onde:
* $\Delta w_{ji}(n)$: Ajuste a ser feito no peso que conecta o neurônio $i$ ao $j$.
* $\eta$: Taxa de aprendizagem.
* $y_i(n)$: Sinal de entrada vindo do neurônio $i$.
* $\delta_j(n)$: O **Gradiente Local**. É aqui que a "mágica" acontece.

### O Cálculo do Gradiente Local ($\delta$)
A genialidade do *Backpropagation* é descobrir o erro de neurônios que estão escondidos (camadas ocultas), pois não temos um "gabarito" direto para eles.

* **Se $j$ é um neurônio de saída:** O gradiente é direto (erro vezes a derivada da ativação).
* **Se $j$ é um neurônio oculto:** O gradiente é calculado somando os gradientes locais dos neurônios da próxima camada multiplicados pelos pesos que os conectam. É por isso que o erro se "retropropaga".



---

## 2. As Duas Fases da Computação (Seção 4.4)

O Haykin organiza o funcionamento do algoritmo em duas passagens distintas de informações pela rede:

### **A. Fase para Frente (Forward Pass)**
* **Objetivo:** Calcular as saídas da rede para uma dada entrada.
* **O que acontece com os pesos:** Eles permanecem **fixos** (inalterados).
* **Fluxo:** O sinal entra na primeira camada, sofre as transformações lineares (soma ponderada) e não-lineares (função de ativação), avançando camada por camada até gerar a saída $y_j$.

### **B. Fase para Trás (Backward Pass)**
* **Objetivo:** Ajustar os pesos para diminuir o erro.
* **O que acontece com os pesos:** Eles são **atualizados** com base na Regra Delta Generalizada.
* **Fluxo:** Começa na camada de saída (onde o erro $e_j$ é conhecido). O sinal de erro propaga-se no sentido inverso (da saída para a entrada), camada por camada, calculando os gradientes locais $\delta$ e aplicando as correções $\Delta w$.

---

## 💻 Laboratório: A Lógica das Duas Fases no Código


```python
import numpy as np

# Taxa de aprendizagem
eta = 0.1

# --- 1. FASE PARA FRENTE (FORWARD) ---
# Entradas e Pesos Iniciais
y_i = 0.5  # Saída de um neurônio da camada anterior
peso_w_ji = 0.8
# Cálculo do somador e ativação (ex: Sigmoide)
v_j = y_i * peso_w_ji
y_j = 1 / (1 + np.exp(-v_j))

# --- CÁLCULO DO ERRO ---
d_j = 1.0  # Valor desejado (gabarito)
erro_j = d_j - y_j

# --- 2. FASE PARA TRÁS (BACKWARD) ---
# Derivada da Sigmoide: y_j * (1 - y_j)
derivada_j = y_j * (1 - y_j)

# Gradiente Local (considerando j como camada de saída)
delta_j = erro_j * derivada_j

# Ajuste do Peso (Regra Delta Generalizada)
delta_w = eta * delta_j * y_i
novo_peso = peso_w_ji + delta_w

print(f"Erro na Saída: {erro_j:.4f}")
print(f"Ajuste a ser feito no peso: {delta_w:.4f}")
print(f"Peso Atualizado: {novo_peso:.4f}")
```

---

## Checkpoint 
1.  **O que é retropropagado na rede?** O **sinal de erro** (mais especificamente, o gradiente local), e não o sinal de entrada.
2.  **O que acontece com os pesos durante a Fase para Frente?** Eles ficam **congelados/inalterados**.
3.  **Qual o papel da Regra da Cadeia?** Como as funções são aninhadas (uma camada dentro da outra), a Regra da Cadeia do cálculo diferencial é o que permite derivar o erro global em relação a um peso específico numa camada oculta profunda.

---
