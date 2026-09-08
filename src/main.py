import heapq
import networkx as nx
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
import numpy as np

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

# ==========================================
# 5. Implementação do K-Means (Agrupamento de Entregas)
# Simulando coordenadas (x, y) de 10 pontos de entrega na cidade
pontos_entrega = np.array([
    [2, 3], [2, 4], [3, 3],   # Zona 1 (Centro)
    [8, 7], [9, 8], [8, 8],   # Zona 2 (Mercado)
    [1, 9], [2, 10], [1, 10], # Zona 3 (Escola)
    [10, 2]                   # Ponto isolado
])

# Criando o modelo K-Means com 3 zonas 
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(pontos_entrega)

# Pegando os rótulos (qual zona pertence cada entrega) e os centros
rotulos = kmeans.labels_
centros = kmeans.cluster_centers_

print("\n--- K-MEANS: AGRUPAMENTO DE ENTREGAS ---")
print(f"Pontos de entrega:\n{pontos_entrega}")
print(f"\nZonas (clusters) atribuídas:\n{rotulos}")
print(f"\nCentros das zonas (locais ideais para os entregadores):\n{centros}")

plt.figure(figsize=(8, 6))
plt.scatter(pontos_entrega[:, 0], pontos_entrega[:, 1], c=rotulos, cmap='viridis', marker='o', s=100)
plt.scatter(centros[:, 0], centros[:, 1], c='red', marker='X', s=200, label='Centros dos Clusters')
plt.title("Agrupamento de Entregas com K-Means")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.legend()
plt.savefig("outputs/kmeans_entregas.png")
plt.show()