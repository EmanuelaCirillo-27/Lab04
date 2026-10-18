from operator import attrgetter
from espositore import Espositore
from stand import Stand
from stand_prese_extra import StandPreseExtra
from stand_premium import StandPremium

import csv

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome # Inizializzo il nome del centro fieristico

        self.stands=[] # Lista che tiene traccia di tutti i tipi di stand presi dal file
        self.espositori=[] # Lista che tiene traccia di tutti gli espositori presi dal file

    """Aggiungere setter e getter se necessari"""
    # Definisco i metodi getter e setter per permettere all'utente di poter modificare il nome del
    # centro fieristico
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome=nuovo_nome




    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        # Una volta aperto il file in lettura, scandisco riga per riga e assegno ad ogni elemento di essa
        # un nominativo per poi andare a caratterizzare il singolo stand/espositore grazie alla classe Stand/Espositore,
        # dividendo i 2 tipi di elementi presenti nello stesso file facendo un controllo sul primo elemento di ogni
        # riga (codice), e controllando quali sono le prime 2 lettere che lo caratterizzano

        try:
            with open(file_path) as f:
                reader=csv.reader(f)

                for row in reader:
                    codice=row[0]
                    if codice[0:2]=='ST':
                        superficie=row[1]
                        padiglione=row[2]
                        prezzo=int(row[3])

                        # La classe Stand ha come attributi comuni a tutti i tipi di stand codice, superficie,
                        # padiglione e prezzo. Alcuni stand contengono una colonna in più nel file che, in base
                        # al tipo di stand, contiene o il numero di prese extra, o la posizione. Per capire quindi
                        # quali righe del file hanno la colonna in più controllo se la lunghezza della riga è >4
                        # (il conteggio parte da 1 in questo caso)

                        if len(row)>4:
                            if row[4].isdigit():
                                prese_extra=int(row[4])
                                stand_extra=StandPreseExtra(codice,superficie,padiglione,prezzo,prese_extra)
                                self.stands.append(stand_extra)

                            elif row[4].isalpha():
                                posizione=row[4]
                                stand_premium = StandPremium(codice, superficie, padiglione, prezzo, posizione)
                                self.stands.append(stand_premium)

                            # Essendo i primi 4 attributi comuni a tutti gli stand, creo delle classi figlie della classe
                            # Stand, le quali ereditano gli attributi della classe padre e in più posso aggiungere
                            # quegli attributi e quelle funzioni caratterizzanti dello stand. In particolare uso
                            # .isdigit() e .isalpha() per capire se nella posizione 4 della riga (partendo da 0)
                            # sia presente un valore unicamente numerico o unicamente composto da lettere.
                            # Infine aggiungo alla lista stand il tipo di stand che viene creato (con prese extra o premium)

                        else:
                            stand_standard=Stand(codice, superficie, padiglione, prezzo)
                            self.stands.append(stand_standard)

                            # Se la riga aveva solo 4 elementi, aggiungo alla lista stand uno stand standard

                    if codice[0:2]=='ES':
                        nome=row[1]
                        cognome=row[2]

                        espositore=Espositore(codice,nome,cognome)
                        self.espositori.append(espositore)

                        # Nel caso che la riga era caratterizzata da un espositore, creo l'elemento espositore grazie
                        # alla classe Espositore, per poi aggiungerlo alla lista espositore definita all'inizio

        except FileNotFoundError:
            return None


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # Creo delle variabili inizializzate a None
        stand_trovato=None
        espositore_trovato=None

        # Per singolo stand all'interno del sistema che contiene tutti gli stand, controllo se il codice dato
        # dall'utente coincida o meno con uno dei codici presenti all'interno del sistema, se è così
        # la variabile stand_trovato di aggiorna con lo stand stesso
        for stand in self.stands:
            if codice_stand==stand.codice:
                stand_trovato=stand

        # Se invece lo stand non è stato trovato all'interno del sistema, la variabile rimarrà None,
        # in questo caso scatenerà errore
        if stand_trovato is None:
            raise Exception(f'Stand {codice_stand} non trovato')

        # Per singolo espositore all'interno del sistema che contiene tutti gli espositori, controllo se il codice dato
        # dall'utente coincida o meno con uno dei codici presenti all'interno del sistema, se è così
        # la variabile espositore_trovato di aggiorna con l'espositore stesso
        for espositore in self.espositori:
            if codice_espositore==espositore.codice:
                espositore_trovato=espositore

        # Se invece l'espositore non è stato trovato all'interno del sistema, la variabile rimarrà None,
        # in questo caso scatenerà errore
        if espositore_trovato is None:
            raise Exception(f'Espositore {codice_espositore} non trovato')

        # La classe Stand contiene un attributo disponibile inizializzato a True per indicare che quello
        # stand è libero. Se questo valore però è False, vuol dire che è già stato occupato da qualcuno
        # e quindi scatena l'eccezione
        if not stand_trovato.disponibile:
            raise Exception(f'Stand {codice_stand} non disponibile')

        # La classe Stand contiene un attributo Espositore inizializzato a None, per indicare che lo stand non è
        # associato a nessun espositore. Per ogni stand all'interno della lista stand, controlla se l'attributo espositore
        # di quello stand è uguale all'espositore dato dall'utente, in caso affermativo vuol dire che quell'espositore
        # era già stato assegnato ad uno stand precedentemente e quindi scatena l'eccezione
        for s in self.stands:
            if s is not None and s.espositore==espositore_trovato:
                raise Exception(f'Espositore {codice_espositore} già assegnato allo stand {s.codice}')

        # Se tutti i controlli passano, allora lo stand sarà non più disponibile e sarà associato all'espositore
        # dato dall'utente
        stand_trovato.disponibile=False
        stand_trovato.espositore=espositore_trovato


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        # Ciclo per singolo espositore all'interno del sistema che contiene tutti gli espositori e definisco
        # una variabile inizializzata a None.
        # Ciclo per singolo stand all'interno del sistema che contiene tutti gli stand, controllo se l'attributo
        # espositore dello stand sia uguale all'espositore considerato nel ciclo, in caso affermativo,
        # assegno lo stand alla variabile associato. (Questa uguaglianza è possibile grazie alla funzione
        # __eq__() definita all'interno della classe Espositore)
        for e in self.espositori:
            associato=None
            for s in self.stands:
                if s.espositore==e:
                    associato=s

            if associato != None:
                print(f'Espositore {e}, stand associato {associato.codice}') # Se la variabile associato è diversa
                                                                            # da None, vuol dire che l'espositore
                                                                            # era associato a uno stand
            else:
                print(f'Espositore {e}') # Altrimenti vuol dire che non era associato ad alcuno stand




    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # Utilizzo la funzione sorted per poter ordinare per prezzo gli stand
        return sorted(self.stands, key=attrgetter('prezzo'))
