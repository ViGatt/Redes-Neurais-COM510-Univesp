# 🌐 Semana 04: Teoria da Generalização e Regularização (Russell & Norvig)

Nesta seção, exploramos por que modelos com milhões de parâmetros não necessariamente "decoram" tudo e como podemos forçar a rede a preferir soluções mais simples e robustas.

## 1. Generalização e Desempenho (Seção 21.5.1)

A questão fundamental é: por que uma rede neural com capacidade para decorar todo o conjunto de treinamento ainda consegue classificar corretamente dados novos?

* **O Erro de Teste:** O objetivo final não é o erro zero no treino, mas a minimização do erro no **conjunto de teste**.
* **Complexidade vs. Erro:** Modelos muito simples sofrem de **subajuste (underfitting)**. Modelos complexos demais sofrem de **sobreajuste (overfitting)**. 
* **Navalha de Occam:** Entre duas explicações que explicam igualmente bem os dados, a mais simples costuma ser a correta. Na IA, a regularização é a ferramenta matemática que aplica essa "navalha".

---

## 2. Técnicas de Regularização (Seção 21.5.2)

Regularizar significa adicionar informações ou restrições ao aprendizado para evitar que os pesos se tornem excessivamente complexos ou específicos para o ruído do treino.

### **A. Decaimento de Pesos (Weight Decay / Regularização $L_2$)**
Em vez de apenas minimizar o erro, a função de perda passa a penalizar pesos grandes. A lógica é que pesos menores tornam a rede mais "suave" e menos sensível a pequenas variações na entrada.
* **Nova Função de Perda:** $Loss = Erro + \lambda \sum w^2$
* O parâmetro $\lambda$ (lambda) controla a força da regularização.



### **B. Dropout (Abandono)**
Uma das técnicas mais eficazes e populares no aprendizado profundo moderno.
* **Como funciona:** Durante cada iteração do treinamento, cada neurônio tem uma probabilidade $p$ (ex: 50%) de ser temporariamente "desligado".
* **Efeito:** Isso impede a **co-adaptação**, onde um neurônio depende excessivamente de outro para corrigir um erro. A rede é forçada a aprender representações redundantes e robustas, já que não pode contar com a presença de todos os neurônios o tempo todo.
* **Nota:** O Dropout é usado **apenas no treinamento**. No teste/inferência, todos os neurônios são usados, mas suas saídas são multiplicadas por $(1-p)$.



---

## Laboratório: Implementando Dropout e $L_2$ no PyTorch

No PyTorch, o Dropout é uma camada e o Weight Decay ($L_2$) é um parâmetro do otimizador. Veja como ajustar seu modelo no VS Code conforme arquivo 02.01 - regularizacao_pratica.py

---

## Checkpoint 
1. **O que o Dropout evita?** Evita a co-adaptação de neurônios, forçando a rede a ser mais robusta.
2. **Qual a relação entre Weight Decay e a complexidade do modelo?** O decaimento de pesos ($L_2$) força os pesos a ficarem menores, o que simplifica a função aprendida pela rede, combatendo o overfitting.
3. **Dropout é usado na fase de teste?** Não. No teste, a rede usa todos os seus neurônios para garantir a máxima precisão, apenas ajustando a escala dos valores.
