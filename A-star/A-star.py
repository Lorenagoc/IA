'''
Primeira lista de exercício do laboratório de Inteligência Artificial 2022.1

Tema: Busca A*, problema do caminho de Arad até Bucareste

Referências bibliográficas: 
-> https://www.pythonpool.com/a-star-algorithm-python/
-> https://stackabuse.com/basic-ai-concepts-a-search-algorithm/
-> https://www.youtube.com/watch?v=UwtjG1BUHJA
-> https://www.youtube.com/watch?v=__DGIVPIE9U
'''

from collections import deque


class Grafo:

    # Cria o objeto grafo que possui vizinhos como atributos
    def __init__(self, grafo) -> None:
        self.grafo = grafo

    def obtem_vizinhos(self, vertice):
        return self.grafo[vertice]

    # Tabela de heurísticas das cidades
    def h(self, vertice):
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
            'Rimnicu': 193,
            'Sibiu': 253,
            'Timisoara': 329,
            'Urziceni': 80,
            'Vaslui': 199,
            'Zerind': 374
        }

        return H[vertice]

    def a_star(self, origem, destino):

        # Nós que foram abertos começando da cidade de origem (vizinhos não visitados)
        lista_abertos = set([origem])
        # Nós que foram fechados (vizinhos já visitados)
        lista_fechados = set([])

        g = {}  # Custo do caminho do nó inicial até o nó n
        g[origem] = 0

        adjacentes = {}  # Mapa de vizinhos visitados
        adjacentes[origem] = origem

        # Enquanto ainda houver nós abertos com vizinhos não visitados...
        while len(lista_abertos) > 0:

            n = None  # Nó com menor f(n) até o momento

            # Calcula menor f(n)
            for proximo_vertice in lista_abertos:
                if n == None or g[proximo_vertice] + self.h(proximo_vertice) < g[n] + self.h(n):
                    n = proximo_vertice  # Atualiza cidade atual

            if n == None:
                print('O caminho não existe')
                return None

            print(
                "***** Estamos em {}, f(n) = {} *****".format(n, g[n] + self.h(n)))
            print("")

            # Verifica se chegou na cidade destino e percorre o caminho de volta
            if n == destino:
                caminho = []

                # Enquanto o nó houver vértices já visitados
                while adjacentes[n] != n:
                    # Adiciona no array todos os nós que foram abertos e verificados
                    caminho.append(n)
                    n = adjacentes[n]  # Passa para o próximo

                caminho.append(origem)  # Terminando, adiciona o nó de origem
                caminho.reverse()  # Inverte todo o array para imprimir o caminho na ordem

                print('Melhor caminho: {}'.format(caminho))
                return caminho

            # Para todos os vizinhos do nó atual
            for(v_adjacente, custo_aresta) in self.obtem_vizinhos(n):
                # Se o vertice ainda não foi visitado
                if v_adjacente not in lista_abertos and v_adjacente not in lista_fechados:
                    # Adiciona na lista de abertos
                    lista_abertos.add(v_adjacente)
                    # Adiciona como um vértice de n
                    adjacentes[v_adjacente] = n
                    # Calcula custo da origem até o vertice em questão
                    g[v_adjacente] = g[n] + custo_aresta + self.h(v_adjacente)

                # Se o vertice já foi visitado
                else:
                    # Compara a possivel rota com o os caminhos já feitos anteriormente
                    # Se não compensa, atualiza os dados
                    if g[v_adjacente] > g[n] + custo_aresta:
                        # Atualiza o custo do vizinho (adiciona o valor acumulativo no lugar)
                        g[v_adjacente] = g[n] + custo_aresta
                        # Adiciona como um vértice visitado de n
                        adjacentes[v_adjacente] = n

                        # Abre o vertice novamente para ser inspecionado por outras rotas
                        if v_adjacente in lista_fechados:
                            lista_fechados.remove(v_adjacente)
                            lista_abertos.add(v_adjacente)

            # Imprime as possíveis próximas cidades da rota
            for v_aberto in lista_abertos:
                print("Considerando ir para {}, f(n) = {}".format(
                    v_aberto, g[v_aberto]+self.h(v_aberto)))
            print()

            # Todos os vizinhos foram visitados então fecha o nó
            lista_abertos.remove(n)
            lista_fechados.add(n)

        print('O caminho não existe')
        return None


if __name__ == "__main__":

    mapa = {
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Zerind': [('Arad', 75), ('Oradea', 71)],
        'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
        'Timisoara': [('Lugoj', 111), ('Arad', 118)],
        'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
        'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
        'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
        'Craiova': [('Rimnicu', 146), ('Pitesti', 138), ('Drobeta', 120)],
        'Rimnicu': [('Pitesti', 97), ('Sibiu', 80), ('Craiova', 146)],
        'Sibiu': [('Fagaras', 99), ('Oradea', 151), ('Arad', 140), ('Rimnicu', 80)],
        'Fagaras': [('Bucareste', 211), ('Sibiu', 99)],
        'Pitesti': [('Bucareste', 101), ('Craiova', 138), ('Rimnicu', 97)],
        'Bucareste': [('Giurgiu', 90), ('Urziceni', 85), ('Fagaras', 211), ('Pitesti', 101)],
        'Urziceni': [('Hirsova', 98), ('Vaslui', 142), ('Bucareste', 85)],
        'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
        'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
        'Iasi': [('Neamt', 87), ('Vaslui', 92)],
        'Giurgiu': [('Bucareste', 90)],
        'Eforie': [('Hirsova', 86)],
        'Neamt': [('Iasi', 87)]
    }

    grafo = Grafo(mapa)
    grafo.a_star('Arad', 'Bucareste')
