from collections import defaultdict
from typing import List, Dict

class Cidade:
	def __init__(self, heuristica):
		self.heuristica = heuristica
		self.adjacencias = {}
	
	def insere(self, vizinho, custo:int):
		self.adjacencias[vizinho] = custo

	def obtem_heuristica(self):
		return self.heuristica

class Grafo:
	
	def __init__(self):
		self.cidades = {}
		self.grafo = defaultdict(list) #criamos esse atributo para fazer um dicionario de listas e facilitar a implementacao

	def adiciona_cidade(self, nome, heuristica_cidade) -> Cidade:
		nova_cidade = Cidade(heuristica_cidade)
		self.cidades[nome] = nova_cidade
		return nova_cidade

	def adiciona_custo(self, cidade_origem, cidade_destino, custo):
		self.grafo[cidade_origem].append(cidade_destino) #cria uma aresta ligando um vertice u e um vertice v
		vertice_origem = self.obtem_cidade(cidade_origem)
		vertice_destino = self.obtem_cidade(cidade_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, custo)

	def obtem_cidade(self, nome_cidade:str) -> Cidade:
		if nome_cidade in self.cidades:
			return self.cidades[nome_cidade]
		else:
			return None

	def vizinhos(self, nodo):
		return self.grafo[nodo] #retorna o vizinho desse nodo especifico

if __name__ == "__main__":

	mapa = Grafo()

	mapa.adiciona_cidade("Arad", 366)
	mapa.adiciona_cidade("Bucareste", 0)
	mapa.adiciona_cidade("Craiova", 160)
	mapa.adiciona_cidade("Drobeta", 242)
	mapa.adiciona_cidade("Eforie", 161)
	mapa.adiciona_cidade("Fagaras", 176)
	mapa.adiciona_cidade("Giurgiu", 77)
	mapa.adiciona_cidade("Hirsova", 151)
	mapa.adiciona_cidade("Iasi", 226)
	mapa.adiciona_cidade("Lugoj", 244)
	mapa.adiciona_cidade("Mehadia", 241)
	mapa.adiciona_cidade("Neamt", 234)
	mapa.adiciona_cidade("Oradea", 380)
	mapa.adiciona_cidade("Pitesti", 100)
	mapa.adiciona_cidade("Rimnicu Vilcea", 193)
	mapa.adiciona_cidade("Sibiu", 253)
	mapa.adiciona_cidade("Timisoara", 329)
	mapa.adiciona_cidade("Urziceni", 80)
	mapa.adiciona_cidade("Vaslui", 199)
	mapa.adiciona_cidade("Zerind", 374)

	mapa.adiciona_custo("Arad","Sibiu", 140)
	mapa.adiciona_custo("Arad","Zerind", 75)
	mapa.adiciona_custo("Arad", "Timisoara", 118)
	mapa.adiciona_custo("Zerind", "Oradea", 71)
	mapa.adiciona_custo("Oradea", "Sibiu", 151)
	mapa.adiciona_custo("Timisoara", "Lugoj", 111)
	mapa.adiciona_custo("Lugoj", "Mehadia", 70)
	mapa.adiciona_custo("Mehadia", "Drobeta", 75)
	mapa.adiciona_custo("Drobeta", "Craiova", 120)
	mapa.adiciona_custo("Craiova", "Pitesti", 138)
	mapa.adiciona_custo("Craiova", "Rimnicu Vilcea", 146)
	mapa.adiciona_custo("Rimnicu Vilcea", "Sibiu", 80)
	mapa.adiciona_custo("Rimnicu Vilcea", "Pitesti", 101)
	mapa.adiciona_custo("Sibiu", "Fagaras", 99)
	mapa.adiciona_custo("Fagaras", "Bucareste", 211)
	mapa.adiciona_custo("Bucareste", "Giurgiu", 90)
	mapa.adiciona_custo("Bucareste", "Urzicene", 85)
	mapa.adiciona_custo("Urzicene", "Hirsova", 98)
	mapa.adiciona_custo("Urzicene", "Vaslui", 142)
	mapa.adiciona_custo("Vaslui", "Iasi", 92)
	mapa.adiciona_custo("Iasi", "Neamt", 87)
	mapa.adiciona_custo("Hirsova", "Eforie", 86)