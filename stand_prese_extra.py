from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, prese_extra):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.prese_extra = prese_extra
        self.calcolo_prezzo()

    def calcolo_prezzo(self):
        prezzo_finale=self.prezzo*(1+0.07*self.prese_extra)
        self.prezzo=prezzo_finale

    def __str__(self):
        return f'{super().__str__()} - Prese Extra: {self.prese_extra}'