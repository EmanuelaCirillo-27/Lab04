class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo

    def __str__(self):
        return f'{self.codice} - {self.superficie} - {self.padiglione} - {self.prezzo}'
