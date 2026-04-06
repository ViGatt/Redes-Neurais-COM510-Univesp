# ✂️ Semana 04: Poda de Redes e Limitações do Backpropagation

Nestas seções, o Haykin discute o ciclo de vida do projeto de uma rede neural, mostrando que um bom modelo não é apenas aquele que aprende, mas aquele que é enxuto, computacionalmente eficiente e ciente de suas próprias limitações.

## 1. Técnicas de Poda de Rede (Network Pruning) - Seção 4.15

Encontrar a topologia ideal (número exato de neurônios e camadas) é um problema de otimização complexo. Existem duas abordagens principais na engenharia de IA:
1. **Crescimento da Rede:** Começa com um único neurônio e adiciona novos até o erro cair.
2. **Poda da Rede (Pruning):** Começa com uma rede gigantesca (para garantir que ela aprenda rápido) e, depois de treinada, **remove as sinapses e neurônios inúteis**.

### Por que podar?
A poda é uma forma poderosa de **Regularização**. Ao remover parâmetros, simplificamos o modelo (aplicando a Navalha de Occam) e reduzimos drasticamente a chance de *Overfitting*, além de deixar o modelo mais leve para rodar em dispositivos com pouca memória (como microcontroladores).



### Como podar (Optimal Brain Damage)
Não podemos simplesmente remover qualquer peso. O método citado (Dano Cerebral Ótimo) avalia a **sensibilidade** da rede a cada peso. 
* Em vez de olhar apenas para o valor do peso, calcula-se a segunda derivada (Matriz Hessiana) da função de erro. 
* O algoritmo identifica quais pesos, se removidos, causam o **menor aumento possível no erro** e os corta.

---

## 2. Virtudes e Limitações da Retropropagação - Seção 4.16

O *Backpropagation* mudou a história da IA, mas não é perfeito. O Haykin faz um balanço honesto do algoritmo:

### Virtudes
* **Simplicidade Matemática:** Baseado em cálculo diferencial básico (Regra da Cadeia), é fácil de programar e otimizar em hardware.
* **Aproximação Universal:** Associado a funções não-lineares, consegue mapear qualquer função contínua se tiver neurônios suficientes.

### Limitações Fatais
* **Lentidão Crônica:** Como o método usa gradiente descendente local, ele precisa de milhares ou milhões de iterações para cruzar platôs na superfície de erro.
* **Mínimos Locais:** Não há garantia matemática de que o algoritmo encontrará a solução perfeita (mínimo global).
* **Esquecimento Catastrófico:** Se você treinar a rede para a Tarefa A, e depois usar a mesma rede para aprender a Tarefa B, os novos ajustes de pesos irão "apagar" o conhecimento da Tarefa A. A rede não consegue aprender de forma contínua sem reter os dados antigos.

---

## 3. Considerações de Projeto e Conhecimento Prévio - Seção 4.20

O Haykin encerra as discussões do MLP com uma regra de ouro: **não deixe a rede aprender tudo do zero se você já sabe algo sobre o problema.**

Se você tem conhecimento prévio sobre as leis da física que regem seus dados, ou sobre invariâncias (ex: um gato na foto continua sendo um gato se a foto for movida alguns pixels para o lado), você deve **embutir isso na arquitetura**.
* **Compartilhamento de Pesos:** Forçar que certos neurônios tenham exatamente os mesmos pesos reduz drasticamente a quantidade de parâmetros livres que precisam ser treinados. Isso é a base teórica para o sucesso das Redes Neurais Convolucionais (CNNs) em visão computacional.

---

## Laboratório: Pruning no PyTorch

O PyTorch possui um módulo nativo fantástico para realizar a poda em redes treinadas, sem precisar recalcular derivadas complexas manualmente. Teste este código no arquivo pruning_pratico.py:



---

## Checkpoint

1. **Qual a relação entre Pruning (Poda) e Generalização?** Redes superdimensionadas tendem a decorar os dados. Podar conexões inúteis obriga a rede a reter apenas as características estruturais do problema, melhorando a generalização (combate ao overfitting).
2. **O que é o "Esquecimento Catastrófico"?** É a incapacidade do MLP tradicional de aprender novas tarefas sequencialmente sem destruir os pesos que foram otimizados para tarefas anteriores.
3. **Por que compartilhar pesos é uma boa ideia em arquiteturas profundas?** Porque embute conhecimento prévio no modelo e reduz a dimensionalidade do problema de otimização, exigindo menos dados e menos tempo de processamento.