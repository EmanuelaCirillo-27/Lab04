from espositore import Espositore
from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium

import csv

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome

        self.stand=[]
        self.espositore=[]

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome=nuovo_nome




    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path) as f:
                reader=csv.reader(f)

                for row in reader:
                    codice=row[0]
                    if codice[0:2]=='ST':
                        superficie=row[1]
                        padiglione=row[2]
                        prezzo=int(row[3])
                        if row[4]!="":
                            if row[4].isdigit():
                                prese_extra=int(row[4])
                                stand_extra=StandPreseExtra(codice,superficie,padiglione,prezzo,prese_extra)
                                self.stand.append(stand_extra)

                            if row[4].isalpha():
                                posizione=row[4]
                                stand_premium = StandPremium(codice, superficie, padiglione, prezzo, posizione)
                                self.stand.append(stand_premium)

                        stand_standard=Stand(codice, superficie, padiglione, prezzo)
                        self.stand.append(stand_standard)

                    if codice[0:2]=='ES':
                        nome=row[1]
                        cognome=row[2]

                        espositore=Espositore(codice,nome,cognome)
                        self.espositore.append(espositore)

        except FileNotFoundError:
            return None




    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
