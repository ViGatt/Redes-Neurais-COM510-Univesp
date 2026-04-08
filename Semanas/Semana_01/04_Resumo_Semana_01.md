# 🧠 Semana 01: Resumo Geral e Fundamentos

Este documento consolida os blocos construtivos fundamentais das Redes Neurais Artificiais (RNAs), fazendo a ponte entre a biologia e a matemática computacional.

## 1. Inspiração Biológica
O cérebro humano é um processador de informações altamente complexo, não-linear e paralelo. As RNAs buscam imitar sua estrutura básica:
* **Dendritos:** Receptores de sinais (Entradas / Inputs).
* **Soma (Corpo Celular):** Processador central que soma os sinais.
* **Axônio:** Transmissor do sinal resultante (Saída / Output).
* **Sinapses:** As conexões entre os neurônios. A "força" dessa conexão (plasticidade) é o que chamamos de **Pesos Sinápticos** nas RNAs. O aprendizado ocorre pelo ajuste desses pesos.

## 2. O Modelo de McCulloch-Pitts (1943)
O primeiro modelo matemático de um neurônio artificial.
* **Características:** Operava estritamente com sinais binários (0 ou 1). Não possuía um algoritmo de aprendizado automático; os pesos precisavam ser calculados e fixados manualmente pelo engenheiro.
* **Importância Histórica:** Provou que neurônios artificiais podiam simular operadores lógicos universais (portas AND, OR, NOT), demonstrando que o cérebro poderia ser modelado como uma máquina computacional.

## 3. A Regra de Hebb (1949)
O primeiro postulado de aprendizado biológico transposto para a IA.
* **O Princípio:** "Neurônios que disparam juntos, conectam-se juntos."
* **Matemática:** Se um neurônio pré-sináptico e um pós-sináptico são ativados simultaneamente, a força da conexão (peso) entre eles é aumentada. Se a ativação for assíncrona, a conexão é enfraquecida. É a base do aprendizado não-supervisionado associativo.