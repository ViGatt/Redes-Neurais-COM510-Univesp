# 💻 Semana 04: Prática de Otimização e Regularização no PyTorch

Nesta aula prática, o professor desenvolve um notebook passo a passo demonstrando como configurar e tratar o *overfitting* de uma rede MLP voltada a um problema de regressão (aprender a função de uma onda ruidosa).

## 1. O Problema e a Divisão de Dados (Holdout)

O primeiro grande passo de engenharia demonstrado na aula não está na rede, mas nos dados. Em problemas reais, não dividimos a base apenas em "Treino e Teste". O professor implementa a divisão tripla (Holdout):

* **Treinamento (ex: 70%):** Usado exclusivamente para calcular o gradiente e atualizar os pesos.
* **Validação (ex: 15%):** Usado ao final de cada época para verificar o desempenho do modelo em dados "novos". É essa base que guia o ajuste de hiperparâmetros e indica a hora do *Early Stopping*.
* **Teste (ex: 15%):** Mantida "fechada" até o final do projeto. Serve apenas para atestar a qualidade final da rede que foi escolhida.

> *No código, a biblioteca `scikit-learn` é utilizada com a função `train_test_split` chamada duas vezes consecutivas para criar essas três subdivisões.*

---

## 2. Implementação das Melhorias no PyTorch

O professor demonstra como é incrivelmente simples engatar as técnicas matemáticas complexas (vistas nas aulas teóricas) diretamente no PyTorch através dos otimizadores.

### A. Adição do Momentum
Se o modelo estiver utilizando o clássico Gradiente Descendente Estocástico (`SGD`), a adição da inércia para escapar de mínimos locais é feita por um único parâmetro:
```python
otimizador = torch.optim.SGD(modelo.parameters(), lr=0.01, momentum=0.9)
```

### B. Algoritmos Otimizados (Adam)
Para contornar o problema da escala de gradientes, substitui-se o SGD pelo padrão da indústria (`Adam`), que gerencia a taxa de aprendizagem de forma dinâmica e individual para cada peso:
```python
# O Adam não exige o parâmetro momentum, pois já o calcula internamente (os betas)
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.01)
```

### C. Regularização
Para combater o *overfitting* na prática, aplicou-se a Regularização L2 (Decaimento de Pesos). No PyTorch, isso não é feito alterando a função de custo manualmente, mas sim configurando o otimizador para "esmagar" os pesos a cada passo via o parâmetro `weight_decay`:
```python
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.01, weight_decay=1e-5)
```

---

## Laboratório: O Esqueleto Completo (Notebook da Aula)

Para verificar a síntese de como o código estrutural se parece no seu ambiente, integrando os dados da onda senoidal, o mini-batch, e o otimizador Adam com L2. visualize o arquivo `mlp_pratica_completa.py`:

---