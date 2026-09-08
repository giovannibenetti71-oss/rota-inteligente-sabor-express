import heapq
import networkx as nx
import matplotlib.pyplot as plt
import os

# 1. Criação do Grafo (representando a cidade)
grafo = {
    'Centro': {'Mercado': 5, 'Hospital': 8},
    'Mercado': {'Centro': 5, 'Escola': 4, 'Padaria': 6},
    'Hospital': {'Centro': 8, 'Escola': 3},
    'Escola': {'Mercado': 4, 'Hospital': 3, 'Residencial': 7},
    'Padaria': {'Mercado': 6, 'Residencial': 5},
    'Residencial': {'Escola': 7, 'Padaria': 5, 'Shopping': 10},
    'Shopping': {'Residencial': 10}
}

# 2. Implementação do Algoritmo A* (Busca pelo menor caminho)
heuristica = {
    'Centro': 10, 'Mercado': 8, 'Hospital': 7, 
    'Escola': 6, 'Padaria': 5, 'Residencial': 3, 'Shopping': 0
}

def a_star(grafo, inicio, destino, heuristica):
    fila = []  # Fila de prioridade (custo estimado, nó atual, caminho)
    heapq.heappush(fila, (heuristica[inicio], inicio, [inicio]))
    visitados = set()
    
    while fila:
        custo_estimado, atual, caminho = heapq.heappop(fila)
        
        if atual in visitados:
            continue
        visitados.add(atual)
        
        if atual == destino:
            return caminho
        
        for vizinho, peso in grafo[atual].items():
            if vizinho not in visitados:
                g = custo_estimado - heuristica[atual] + peso
                h = heuristica[vizinho]
                f = g + h
                novo_caminho = caminho + [vizinho]
                heapq.heappush(fila, (f, vizinho, novo_caminho))
    
    return None

# 3. Executar o algoritmo
inicio = 'Centro'
destino = 'Shopping'
caminho = a_star(grafo, inicio, destino, heuristica)

print(f"Menor caminho de {inicio} até {destino}: {caminho}")
print(f"Total de paradas: {len(caminho) - 1}")

# 4. Visualizar o grafo (para colocar nos outputs/relatório)
G = nx.Graph()
for no, vizinhos in grafo.items():
    for vizinho, peso in vizinhos.items():
        G.add_edge(no, vizinho, weight=peso)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Mapa da Cidade - Sabor Express")
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/grafo_cidade.png")
plt.show()