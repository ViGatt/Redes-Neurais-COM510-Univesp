# 🚀 Semana 03: Acelerando a Convergência com o Termo de Momento
>S3 - Texto-base 6 – Redes Neurais: princípios e prática (leia Capítulo 4 - Seção 4.6) | Simon Haykin

O algoritmo de retropropagação clássico segue uma trajetória que pode ser muito lenta em regiões planas do espaço de erro (platôs) e muito oscilatória em regiões com vales íngremes. A Seção 4.6 do Haykin apresenta a solução para estabilizar esse comportamento.

## 1. O Problema da Taxa de Aprendizagem ($\eta$)

Como vimos, a taxa de aprendizagem dita o tamanho do passo:
* **Passo pequeno:** Aprendizado seguro, mas inaceitavelmente lento. Pode ficar preso no primeiro mínimo local que encontrar.
* **Passo grande:** Aprendizado rápido, mas com alto risco de oscilação (zigue-zague) que impede o algoritmo de chegar ao fundo do vale (mínimo global).



## 2. A Inclusão do Momento ($\alpha$)

A ideia do termo de momento é inspirada na física: uma bola rolando ladeira abaixo ganha "embalo". Se ela encontrar um pequeno buraco (mínimo local), seu momento (inércia) a ajuda a passar direto por ele.

Matematicamente, adicionamos uma fração do **ajuste de peso da iteração anterior** à iteração atual. A nova Regra Delta Generalizada fica assim:

$$
\Delta w_{ji}(n) = \alpha \cdot \Delta w_{ji}(n-1) + \eta \cdot \delta_j(n) \cdot y_i(n)
$$

Onde:
* $\Delta w_{ji}(n)$: Ajuste atual do peso.
* $\Delta w_{ji}(n-1)$: Ajuste feito na iteração anterior.
* $\alpha$ (alfa): **Constante de Momento** (geralmente um valor entre $0.1$ e $0.9$).
* $\eta \cdot \delta_j(n) \cdot y_i(n)$: O cálculo padrão do gradiente atual.

---

## 3. Os Efeitos Práticos do Momento

A adição de $\alpha$ atua matematicamente como um **filtro passa-baixas** para as atualizações de peso, trazendo três grandes benefícios:

1. **Aceleração em Platôs:** Se os gradientes estão apontando consecutivamente para a mesma direção (região plana), o termo de momento se acumula, aumentando o tamanho efetivo do passo e acelerando a descida.
2. **Amortecimento de Oscilações:** Se o gradiente fica alternando de sinal (zigue-zagueando pelos lados de um vale estreito), o momento da iteração anterior cancela parte do gradiente atual, suavizando a trajetória.
3. **Fuga de Mínimos Locais:** A inércia acumulada pode ser suficiente para "empurrar" a atualização de pesos para fora de um mínimo local raso.

---

## 💻 Laboratório: Implementando o Momento

```python
import numpy as np

# Hiperparâmetros
eta = 0.1      # Taxa de aprendizagem
alfa = 0.9     # Termo de momento (0.0 significa sem momento)

# Variáveis do neurônio
peso_atual = 0.5
delta_w_anterior = 0.0  # Na primeira iteração, não há momento

# Simulando 5 épocas de treinamento com gradientes hipotéticos
gradientes = [0.2, 0.2, -0.1, 0.15, 0.1] 

print("Época | Gradiente | Delta W | Novo Peso")
print("-" * 40)

for epoca, gradiente_local in enumerate(gradientes):
    # Calculo do termo principal (simplificado aqui como gradiente_local)
    # Na real seria: eta * delta * entrada
    termo_gradiente = eta * gradiente_local 
    
    # A MÁGICA DO MOMENTO AQUI:
    delta_w_atual = (alfa * delta_w_anterior) + termo_gradiente
    
    # Atualiza o peso
    peso_atual += delta_w_atual
    
    print(f"  {epoca+1}   |   {gradiente_local:>5.2f}   |  {delta_w_atual:>5.4f} |  {peso_atual:>5.4f}")
    
    # Prepara para a próxima iteração
    delta_w_anterior = delta_w_atual
```

---

## 📝 Checkpoint para o Quiz
1. **O que é $\alpha$?** A constante de momento, que determina a influência da atualização passada na atualização presente.
2. **O que acontece se $\alpha = 0$?** A equação volta a ser a Regra Delta Generalizada padrão, sem inércia.
3. **O momento aumenta o custo computacional?** O aumento é insignificante (apenas guardar o último valor na memória), mas o ganho em velocidade de convergência é massivo.