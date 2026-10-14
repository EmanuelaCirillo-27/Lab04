from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.posizione = posizione

    def calcolo_prezzo(self):
        prezzo_finale=self.prezzo*1.30
        self.prezzo=prezzo_finale

    def __str__(self):
        return f'{super().__str__()} - {self.posizione}'