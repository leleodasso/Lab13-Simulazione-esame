import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def getYearSeasons(self):
        return DAO.getYearSeasons()

    def buildGraph(self, anno):
        self.grafo.clear()

        #nodi
        listaNodi = DAO.getPilotiAnnoTraguardo(anno)
        print(len(listaNodi))
        print(listaNodi)
        self.grafo.add_nodes_from(listaNodi)

        #archi
        for u in listaNodi:
            for v in listaNodi:
                if u != v:
                    arcoOrientato = DAO.getNumVittorie(u,v,anno)
                    if arcoOrientato[0]>0:
                        self.grafo.add_edge(u,v, weight = arcoOrientato[0])



    def getNumeriGrafo(self):
        return self.grafo.number_of_nodes(), self.grafo.number_of_edges()

    def getBestDriver(self):
        bestScore = 0
        for nodo in self.grafo.nodes():
            sommaEntranti = 0
            sommaUscenti = 0
            for predecessore in self.grafo.predecessors(nodo):
                sommaEntranti = sommaEntranti + self.grafo[predecessore][nodo]["weight"]
            for successore in self.grafo.successors(nodo):
                sommaUscenti = sommaUscenti + self.grafo[nodo][successore]["weight"]
            if sommaUscenti - sommaEntranti > bestScore:
                bestScore = sommaUscenti - sommaEntranti
                bestDriver = nodo.driverRef
        return bestDriver, bestScore



