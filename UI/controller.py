import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None


    def fillDDYear(self):
        listaAnniStagioni = self._model.getYearSeasons()
        for anno in listaAnniStagioni:
            self._view._ddAnno.options.append(ft.dropdown.Option(text=anno, data=anno, on_click=self.handleDDYearSelection))

    def handleDDYearSelection(self, e):
        self._anno = e.control.data

    def handleCreaGrafo(self,e):

        if self._anno is None:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text("DEVI SELESZIONARE UN GIORNO"))
            self._view.update_page()

        self._model.buildGraph(self._anno)
        numNodi, numArchi = self._model.getNumeriGrafo()
        bestDriver, bestScore = self._model.getBestDriver()

        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {numArchi}"))
        self._view.txt_result.controls.append(ft.Text(f"Best Driver: {bestDriver}, with score: {bestScore} "))
        self._view.update_page()



    def handleCerca(self, e):
        pass

