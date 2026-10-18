class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.disponibile=True
        self.espositore=None

    def __str__(self):
        return f'{self.codice} - {self.superficie}mq - Padiglione: {self.padiglione} - Prezzo: {self.prezzo}£ - Disponibilità: {self.disponibile}'
