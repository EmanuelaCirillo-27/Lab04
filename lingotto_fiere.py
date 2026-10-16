from operator import attrgetter
from espositore import Espositore
from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium

import csv

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome

        self.stands=[]
        self.espositori=[]

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
                        if len(row)>4:
                            if row[4].isdigit():
                                prese_extra=int(row[4])
                                stand_extra=StandPreseExtra(codice,superficie,padiglione,prezzo,prese_extra)
                                self.stands.append(stand_extra)

                            elif row[4].isalpha():
                                posizione=row[4]
                                stand_premium = StandPremium(codice, superficie, padiglione, prezzo, posizione)
                                self.stands.append(stand_premium)

                        else:
                            stand_standard=Stand(codice, superficie, padiglione, prezzo)
                            self.stands.append(stand_standard)

                    if codice[0:2]=='ES':
                        nome=row[1]
                        cognome=row[2]

                        espositore=Espositore(codice,nome,cognome)
                        self.espositori.append(espositore)

        except FileNotFoundError:
            return None


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato=None
        espositore_trovato=None

        for stand in self.stands:
            if codice_stand==stand.codice:
                stand_trovato=stand

        if stand_trovato is None:
            raise Exception(f'Stand {codice_stand} non trovato')

        for espositore in self.espositori:
            if codice_espositore==espositore.codice:
                espositore_trovato=espositore

        if espositore_trovato is None:
            raise Exception(f'Espositore {codice_espositore} non trovato')

        if not stand_trovato.disponibile:
            raise Exception(f'Stand {codice_stand} non disponibile')

        for s in self.stands:
            if s is not None and s.espositore==espositore_trovato:
                raise Exception(f'Espositore {codice_espositore} già assegnato allo stand {s.codice}')

        stand_trovato.disponibile=False
        stand_trovato.espositore=espositore_trovato


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        for e in self.espositori:
            associato=None
            for s in self.stands:
                if s.espositore==e:
                    associato=s

            if associato != None:
                print(f'Espositore {e}, stand associato {associato.codice}')
            else:
                print(f'Espositore {e}')




    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stands, key=attrgetter('prezzo'))
