Crie o arquivo `Semanas/Semana_04/06_Generalizacao_Avancada_Russell.md` no seu VS Code para acomodar a leitura complementar de Russell e Norvig. Abaixo estão as anotações organizadas:

---

# 🔄 Semana 04: Estratégias Avançadas de Generalização (Russell & Norvig)

As Seções 21.5.3 e 21.5.4 expandem a caixa de ferramentas do aprendizado profundo para além da alteração matemática da função de perda (como no L2) ou da arquitetura (como no Dropout), focando na manipulação dos dados de entrada e no reaproveitamento de conhecimento.

## 1. Aumento de Dados (Data Augmentation) - Seção 21.5.3

A melhor forma de evitar o *overfitting* é, indiscutivelmente, ter mais dados de treinamento. Quando a coleta de novos dados reais é cara ou demorada, a solução é gerar dados sintéticos a partir dos originais.

* **O que é:** Aplicar transformações geométricas ou colorimétricas aleatórias aos dados de entrada antes de passá-los para a rede.
* **Como funciona:** Se você possui um conjunto limitado de imagens (como recortes de imagens de satélite com dados de NDVI para monitoramento de pragas), você pode multiplicar artificialmente o tamanho dessa base. Ao rotacionar, espelhar horizontalmente ou aplicar *zoom* aleatório na imagem de uma cultura afetada, a rede é forçada a aprender características essenciais em vez de decorar a posição exata dos pixels.
* **Benefício:** Ensina à rede a **invariância** (a habilidade de reconhecer um padrão independentemente do seu ângulo, iluminação ou escala) sem adicionar novos parâmetros ao modelo.

---

## 2. Transferência de Aprendizado (Transfer Learning) - Seção 21.5.4

Para problemas complexos em que a base de dados não tem a escala de dezenas de milhares de amostras, treinar uma rede profunda do absoluto zero (com pesos aleatórios) quase inevitavelmente resulta em *overfitting*. A solução de engenharia para isso é a Transferência de Aprendizado.

* **A Premissa:** Redes profundas tendem a aprender características genéricas nas suas primeiras camadas (como detectores de bordas, linhas e gradientes de cor) e características específicas nas últimas camadas.
* **A Execução:**
  1. Utiliza-se uma arquitetura já treinada por semanas em um dataset colossal (como o *ImageNet*, que possui milhões de imagens genéricas).
  2. "Congelam-se" os pesos das primeiras camadas dessa rede (elas já sabem extrair texturas muito bem).
  3. Remove-se a última camada de saída da rede original e substitui-se por uma nova camada não treinada, configurada para as classes do seu problema específico.
  4. Treina-se a rede com uma taxa de aprendizagem baixa. Como a base já é sólida, a rede converge rapidamente para o novo problema utilizando os dados que você possui.

---

## Laboratório: Aumento de Dados Simples no PyTorch

O ecossistema PyTorch possui o pacote `torchvision`, que lida com o Aumento de Dados dinamicamente. Ele aplica as transformações na memória RAM ("on the fly") durante o treinamento, poupando espaço no seu disco rígido. Visualize na prática através do arquivo aumento_dados.py para salvar este *snippet*:


---

## Checkpoint 
1. **O Aumento de Dados altera o conjunto de teste?** Não. Todas as transformações aleatórias (rotação, ruído, espelhamento) são aplicadas **estritamente no conjunto de treinamento**. O teste sempre recebe dados intocados.
2. **Qual é o pré-requisito lógico para usar Aumento de Dados?** A transformação não pode alterar a classe semântica do dado. (Exemplo: rotacionar um '6' em 180 graus vira um '9', o que destruiria a coerência do rótulo se fosse uma tarefa de reconhecimento de dígitos).
3. **Por que congelar as primeiras camadas no Transfer Learning?** Porque as camadas iniciais funcionam como extratores universais de características (linhas, texturas). Congelá-las economiza grande poder computacional e evita que a nova base de dados, menor, destrua os pesos genéricos perfeitamente calibrados pela rede original.