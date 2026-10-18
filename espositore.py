class Espositore:
    def __init__(self,codice,nome,cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    # Implemento il metodo __eq__, per dire a Python quando due espositori devono essere considerati uguali.
    def __eq__(self,other):
        if isinstance(other, Espositore): # Verifico che l'oggetto con cui confronto l'espositore (other),
                                                # è effettivamente un'istanza della classe Espositore
                                                # (cioè un oggetto creato proprio da questa Classe)

            return self.codice == other.codice # Se il controllo precedente è andato a buon fine, stabilisco
                                                # il criterio di uguaglianza: due espositori sono considerati uguali
                                                # solo se hanno lo stesso codice (restituisce True)

        return False # Altrimenti restituisce False



    def __str__(self):
        return f'{self.codice} - {self.nome} - {self.cognome}'