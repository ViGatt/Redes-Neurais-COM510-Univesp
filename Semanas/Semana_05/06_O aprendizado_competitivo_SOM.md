# 🗺️ Semana 05: O Aprendizado Competitivo e a Rede SOM (Videoaula 14)

Nesta videoaula, consolidamos os conceitos práticos e as engrenagens por trás dos Mapas Auto-organizáveis (SOM), detalhando as fases do aprendizado competitivo e a arquitetura desse modelo não supervisionado.

## 1. Aprendizado Não Supervisionado e Competitivo

No aprendizado não supervisionado, o modelo deve extrair características ou padrões significativos dos dados sem a ajuda de um "especialista" (rótulos).
* **Redundância é essencial:** O modelo só consegue aprender se houver redundância (padrões repetitivos) nos dados. Sem isso, os dados são interpretados apenas como ruídos aleatórios.
* **O Aprendizado Competitivo:** Segue a regra do *The winner takes all* (O vencedor leva tudo). Os neurônios competem entre si para ver quem é ativado pelo padrão de entrada apresentado.

## 2. A Arquitetura do SOM (Mapas de Kohonen)

A rede SOM possui uma forte inspiração neurofisiológica, baseada no córtex cerebral (auditivo, visual, motor), onde neurônios topologicamente próximos tendem a responder a estímulos semelhantes.
* **O Grid:** Normalmente, a rede é formada por um *grid* bidimensional (2D).
* **Células de Voronoi:** Cada neurônio possui um vetor de pesos que representa um protótipo de sua região geométrica (uma célula de Voronoi), mapeando um espaço de alta dimensão ($R^m$) para o grid 2D.

## 3. Os 3 Processos de Formação do Mapa

Quando uma amostra de entrada é apresentada, três processos ocorrem sequencialmente:

1. **Competição:** A rede computa a função discriminante (geralmente a distância euclidiana) entre a entrada e os pesos dos neurônios. O neurônio com o menor valor é o **BMU** (*Best Matching Unit* - Unidade de Melhor Correspondência).
2. **Cooperação:** O neurônio vencedor determina uma vizinhança topológica (baseada na proximidade física no grid, não nos pesos). Os vizinhos próximos se beneficiam da ativação, utilizando uma função que sofre decaimento ao longo do tempo.
3. **Adaptação Sináptica (Ajuste):** Os pesos do BMU e de seus vizinhos são ajustados na direção do padrão de entrada, utilizando a taxa de aprendizagem e o fator de vizinhança.

## 4. Avaliação e Inspeção do Mapa

Para garantir que o mapa foi bem formado (sem supervisão), utilizamos:
* **Métricas Matemáticas:** Erro de Quantização (distância da entrada ao peso) e Erro Topográfico (preservação da vizinhança).
* **Inspeção Visual:** 
  * *Heat Maps:* Mostram a distribuição dos pesos no grid.
  * *Hit Maps:* Mostram quantos padrões caíram em cada neurônio.
  * *U-Matrix:* Mostra as fronteiras entre os agrupamentos calculando a similaridade com os vizinhos.

---

## 💻 Laboratório: A Matemática da Adaptação Sináptica

Para entender a etapa 3 (Adaptação) no seu VS Code, vamos simular como o peso "caminha" em direção ao dado de entrada. Crie o arquivo `Semanas/Semana_05/06_adaptacao_som.py`:


---

## Resumo para Revisão
* **Aprendizado:** Não supervisionado e baseado em competição (*Winner takes all*).
* **3 Etapas da Formação:** Competição (encontrar o BMU), Cooperação (definir vizinhança geométrica) e Adaptação (ajustar os pesos).
* **Inspeção Visual:** U-Matrix, Heat Maps e Hit Maps ajudam a visualizar a topologia 2D gerada.
