# Simulação simples da lógica de classificação (Árvore vs. Móvel)
def classificador_simples(tem_madeira, tem_folhas, esta_plantado):
    # O "conhecimento" embutido na função
    if tem_madeira and tem_folhas and esta_plantado:
        return "Árvore (Alta Probabilidade)"
    elif tem_madeira and not tem_folhas:
        return "Móvel ou Madeira Morta"
    else:
        return "Desconhecido"

print(f"Objeto 1: {classificador_simples(True, True, True)}")
print(f"Objeto 2: {classificador_simples(True, False, False)}")