# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 📖 Descrição do Problema
A empresa de delivery "Sabor Express" enfrenta atrasos e custos elevados devido à falta de otimização nas rotas de entrega. Atualmente, os percursos são definidos manualmente, resultando em ineficiência operacional, especialmente em horários de pico. Este projeto utiliza Inteligência Artificial para sugerir as melhores rotas e agrupar entregas próximas, visando reduzir tempo, custo de combustível e aumentar a satisfação dos clientes.

## 🎯 Objetivos
- Modelar a cidade como um grafo, onde os bairros são nós e as ruas são arestas com pesos (distância ou tempo).
- Implementar o algoritmo A* (A-estrela) para encontrar o menor caminho entre os pontos de entrega.
- Implementar o algoritmo K-Means para agrupar entregas em zonas eficientes, otimizando o trabalho dos entregadores.
- Gerar visualizações gráficas (diagramas e gráficos) para análise dos resultados.

## 🧠 Abordagem e Algoritmos Utilizados
### Grafo da Cidade
A cidade foi representada como um grafo ponderado. Os nós representam os bairros ou locais, e as arestas possuem pesos baseados no tempo estimado de deslocamento.

### Algoritmo A* (Busca Heurística)
Utilizado para encontrar o caminho de menor custo entre um ponto de partida e um destino. O A* combina o custo real do caminho percorrido (g) com uma heurística (h) que estima o custo restante, guiando a busca de forma eficiente.

### Algoritmo K-Means (Aprendizado Não Supervisionado)
Utilizado para agrupar os pontos de entrega em *clusters* (zonas). Cada zona possui um centroide, que representa um ponto estratégico onde um entregador pode se posicionar para atender várias entregas próximas com eficiência.

## 📂 Estrutura do Projeto
- `src/` - Código-fonte principal (algoritmos A* e K-Means).
- `data/` - Arquivos de dados utilizados (ex: entregas.csv).
- `outputs/` - Imagens e gráficos gerados pela execução dos algoritmos.
- `docs/` - Documentação adicional do projeto.

## 🛠️ Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/giovannibenetti71-oss/rota-inteligente-sabor-express.git