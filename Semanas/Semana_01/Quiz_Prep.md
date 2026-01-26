#  Quiz de Preparação - Semana 01

Este arquivo contém questões de fixação baseadas nos Objetos Educacionais e videoaulas da semana.

---

##  Exercício 1: Estrutura do Neurônio MCP

**Pergunta:** Considerando a estrutura e o funcionamento do neurônio MCP, qual afirmação abaixo está correta?

* [ ] O neurônio MCP é intrinsicamente linear, uma vez que só é capaz de lidar com problemas linearmente separáveis.
* [ ] O bias (viés) tem como objetivo modular os pesos sinápticos.
* [ ] O neurônio MCP consiste num modelo de neurônio estocástico.
* [ ] O neurônio foi proposto originalmente para tratar dados contínuos.
* [x] **O neurônio MCP é composto por três partes principais: as sinapses, o corpo celular e a função de ativação.**

> ###  Justificativa Técnica
> 
> 
> O modelo de McCulloch e Pitts (1943) é uma abstração binária.
> 1. **Sinapses:** Entradas ponderadas.
> 2. **Corpo Celular (Soma):** Realiza a combinação linear .
> 3. **Função de Ativação:** Utiliza a função **Degrau**, o que o torna um modelo **não-linear**, apesar de sua simplicidade. Ele trata sinais **binários** (0 ou 1) e é determinístico (não estocástico).

---

##  Exercício 2: Aprendizado Competitivo

**Pergunta:** Sobre o aprendizado competitivo, avalie as afirmações abaixo:

* **i.** Apenas um neurônio pode ser ativado num determinado instante.
* **ii.** Os pesos dos neurônios são atualizados utilizando a técnica de correção de erros.
* **iii.** Neurônios se especializam em subconjunto de padrões, representando protótipos dos dados associados.

**Qual a alternativa correta?**

* [ ] Apenas a alternativa i está correta.
* [ ] Apenas a alternativa ii está correta.
* [ ] Apenas a alternativa iii está correta.
* [ ] Todas as alternativas estão corretas.
* [x] **Apenas as alternativas i e iii estão corretas.**

> ###  Justificativa Técnica
> 
> 
> No aprendizado competitivo (Paradigma Não Supervisionado):
> * **Winner-take-all:** Existe uma competição onde apenas o neurônio "vencedor" (ou ele e sua vizinhança imediata) é ativado para aquela entrada.
> * **Protótipos:** Com o tempo, os neurônios migram para o centro de grupos de dados, tornando-se "protótipos" ou representantes de classes de padrões.
> * **Erro:** A alternativa **ii está incorreta** porque a correção de erros é característica do aprendizado **supervisionado**, enquanto o competitivo foca na similaridade/auto-organização.
> 
> 

---

###  Revisão Rápida

* **MCP é Não-Linear?** Sim, por causa da função degrau.
* **MCP é para dados contínuos?** Não, é para sinais binários.
* **Aprendizado Competitivo precisa de rótulos?** Não, é não supervisionado.

---

#  Resolução: S1 - Atividade Avaliativa

##  Questão 1: Paradigmas de Aprendizagem

*1)Os três principais paradigmas de aprendizagem em redes neurais são: aprendizado supervisionado, aprendizado não supervisionado e aprendizado por reforço. Cada paradigma possui características específicas e é adequado para diferentes tipos de problemas e contextos. Considerando as características e aplicações mencionadas, assinale a alternativa que descreve corretamente os três paradigmas de aprendizagem em redes neurais*
**Resposta Correta: e**

> **Justificativa:** > * **Supervisionado:** Requer um "gabarito" (dados rotulados).
> * **Não Supervisionado:** Trabalha com a estrutura intrínseca dos dados (sem rótulos).
> * **Reforço:** Baseia-se na interação agente-ambiente com feedback de recompensa/penalidade.
> * *Erro das outras:* A alternativa 'a' e 'c' trocam a função dos dados rotulados no não supervisionado.


---

##  Questão 2: Modelagem Matemática do Neurônio

*2)O neurônio biológico possui componentes específicos que desempenham funções essenciais para a transmissão de sinais. Esses componentes incluem os dendritos, o soma e o axônio, cada um com uma função distinta. Compreender como esses componentes operam é crucial para a modelagem matemática usada no desenvolvimento das redes neurais artificiais. Essa modelagem permite que redes neurais artificiais executem tarefas complexas de maneira eficiente, inspirando-se no funcionamento dos neurônios biológicos. 
A estrutura do neurônio biológico é representada na modelagem matemática utilizada em redes neurais artificiais. Assinale a alternativa que descreve corretamente um possível representação.*
**Resposta Correta: c**

> **Justificativa:** > Na modelagem de redes neurais artificiais:
> * As **sinapses/dendritos** são representadas pelas entradas multiplicadas pelos pesos ().
> * O **soma (corpo celular)** é o centro de processamento que realiza a combinação linear (soma ponderada) e aplica a função de ativação.
> * *Nota:* O axônio seria a saída (), e não um receptor.

---

##  Questão 3: Aprendizagem Competitiva (Interpretação)

**Resposta Correta: e (I, III, IV e V, apenas)**

> **Análise das Afirmativas:**
> * **I (Verdadeira):** É o princípio básico do *Winner-Take-All*.
> * **II (Falsa):** Se os pesos fossem idênticos, não haveria competição nem especialização; todos responderiam igual.
> * **III (Verdadeira):** Ela agrupa dados por similaridade estatística.
> * **IV (Verdadeira):** A inibição lateral é o mecanismo que "desliga" os neurônios vizinhos para que apenas o vencedor brilhe.
> * **V (Verdadeira):** Com o tempo, cada neurônio se torna um "especialista" em um tipo de padrão (detector de características).


---

##  Questão 4: Asserções sobre Aprendizado Competitivo

**Resposta Correta: d (As asserções I e II são proposições verdadeiras, e a II é uma justificativa da I)**

> **Análise:**
> * **Asserção I:** É verdadeira, pois o objetivo do aprendizado competitivo é justamente organizar o espaço de entrada (ex: Mapas de Kohonen).
> * **Asserção II:** É verdadeira e descreve a **Regra de Aprendizagem de Kohonen**. Ao mover apenas os pesos do vencedor para mais perto do dado atual, criamos a especialização citada na asserção I.
> * **Relação:** A I só acontece *porque* o mecanismo descrito na II existe.
