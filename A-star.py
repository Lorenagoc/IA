from collections import deque


class Grafo:

    # Cria o objeto grafo que possui vizinhos como atributos
    def __init__(self, vertices) -> None:
        self.vertices = vertices

    # Método para retornar os vizinhos do nó
    def obtem_vizinhos(self, node):
        return self.vertices[node]

    # Tabela de heurísticas das cidades
    def h(self, node):
        H = {
            'Arad': 366,
            'Bucareste': 0,
            'Craiova': 160,
            'Drobeta': 242,
            'Eforie': 161,
            'Fagaras': 176,
            'Giurgiu': 77,
            'Hirsova': 151,
            'Iasi': 226,
            'Lugoj': 244,
            'Mehadia': 241,
            'Neamt': 234,
            'Oradea': 380,
            'Pitesti': 100,
            'Rimnicu Vilcea': 193,
            'Sibiu': 253,
            'Timisoara': 329,
            'Urziceni': 80,
            'Vaslui': 199,
            'Zerind': 374
        }

        return H[node]

    # Implementação do algoritm A* sendo f(n) = g(n) + h(n)
    def a_star(self, origem, destino):

        # Nós que foram abertos começando da cidade de origem (vizinhos não visitados)
        lista_abertos = set([origem])
        # Nós que foram fechados (vizinhos já visitados)
        lista_fechados = set([])

        g = {}  # Custo do caminho do nó inicial até o nó n
        g[origem] = 0

        visitados = {}  # Mapa de vizinhos visitados
        visitados[origem] = origem

        # Enquanto ainda houver nós abertos com vizinhos não visitados...
        while len(lista_abertos) > 0:

            n = None  # Nó com menor f(n) até o momento

            # Calcula menor custo do caminho total estimado
            for vertice_atual in lista_abertos:
                if n == None or g[vertice_atual] + self.h(vertice_atual) < g[n] + self.h(n):
                    n = vertice_atual

            if n == None:
                print('O caminho não existe')
                return None

            # Se chegamos na cidade destino então percorre o caminho de volta
            if n == destino:
                caminho = []

                # Enquanto o nó houver vértices já visitados
                while visitados[n] != n:
                    # Adiciona no array todos os nós que foram abertos e verificados
                    caminho.append(n)
                    n = visitados[n]  # Passa para o próximo

                caminho.append(origem)  # Terminando, adiciona o nó de origem
                caminho.reverse()  # Inverte todo o array

                print('Melhor caminho: {}'.format(caminho))
                return caminho

            # Para todos os vizinhos do nó atual
            for(vizinho, h_vizinho) in self.obtem_vizinhos(n):
                # Se o vertice ainda não foi aberto nem teve seus vizinhos inspecionados
                if vizinho not in lista_abertos and vizinho not in lista_fechados:
                    lista_abertos.add(vizinho)  # Adiciona na lista de abertos
                    # Adiciona como um vértice visitado de n
                    visitados[vizinho] = n
                    # Calcula o custo do caminho até o vertice em questão
                    g[vizinho] = g[n] + h_vizinho
                # Se o vertice não foi aberto ou já foi aberto mas não inspecionado
                else:
                    # Verifica se compensa seguir em frente
                    if g[vizinho] > g[n] + h_vizinho:
                        # Atualiza o custo do vizinho (adiciona o valor acumulativo no lugar)
                        g[vizinho] = g[n] + h_vizinho
                        # Adiciona como um vértice visitado de n
                        visitados[vizinho] = n

                        if vizinho in lista_fechados:
                            lista_fechados.remove(vizinho)
                            lista_abertos.add(vizinho)

            lista_abertos.remove(n)
            lista_fechados.add(n)

        print('O caminho não existe')
        return None


if __name__ == "__main__":

    mapa = {
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Zerind': [('Arad', 75)],
        'Arad': [('Sibiu', 140), ('Timisoara', 118)],
        'Timisoara': [('Lugoj', 111)],
        'Lugoj': [('Mehadia', 70)],
        'Mehadia': [('Drobeta', 75)],
        'Drobeta': [('Craiova', 120)],
        'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138)],
        'Rimnicu Vilcea': [('Pitesti', 97), ('Sibiu', 80)],
        'Sibiu': [('Fagaras', 99)],
        'Fagaras': [('Bucareste', 211)],
        'Pitesti': [('Bucareste', 101)],
        'Bucareste': [('Giurgiu', 90), ('Urziceni', 85)],
        'Urziceni': [('Hirsova', 98), ('Vaslui', 142)],
        'Hirsova': [('Eforie', 86)],
        'Vaslui': [('Iasi', 92)],
        'Iasi': [('Neamt', 87)]
    }

    grafo = Grafo(mapa)
    grafo.a_star('Arad', 'Bucareste')
