# Game of Life

Semplice implementazione del gioco della vita di Conway in Python.

L'obiettivo di questo progetto è realizzare una piccola e semplice versione del gioco della vita di Conway, in modo da poterlo utilizzare come esempio per spiegare il funzionamento di alcuni concetti di programmazione legati a Python.

In questo progetto cercheremo di limitare il più possibile l'uso di librerie e strumenti esterni.
In particolare non utilizzeremo nessuna libreria grafica, ma cercheremo di utilizzare solamente il terminale.

Ricordiamo che questo progetto è stato realizzato per la quinta serata del corso di Python Base, vi raccomandiamo di seguire anche la video registrazione della serata qui.

Per qualsiasi domanda, dubbio, perplessità o se volete aiutarci vi ricordiamo che potete contattarci sui nostri canali social.

## Regole del gioco

Si tratta in realtà di un gioco senza giocatori:
- La sua evoluzione è determinata dal suo stato iniziale
- Non necessita di alcun input da parte di giocatori umani. 
- Si svolge su una griglia di caselle quadrate (celle) che si estende all'infinito in tutte le direzioni
- Questa griglia è detta mondo. 
- Ogni cella ha 8 vicini, che sono le celle ad essa adiacenti, includendo quelle in senso diagonale. 
- Ogni cella può trovarsi in due stati: viva o morta (o accesa e spenta, on e off). 
- Lo stato della griglia evolve in intervalli di tempo discreti, cioè scanditi in maniera netta. 
- Gli stati di tutte le celle in un dato istante sono usati per calcolare lo stato delle celle all'istante successivo. 
- Tutte le celle del mondo vengono quindi aggiornate simultaneamente nel passaggio da un istante a quello successivo: passa così una generazione.

Come funzionano le **transizioni**?

Le transizioni dipendono unicamente dallo stato delle celle vicine in quella generazione:
- Qualsiasi cella viva con meno di due celle vive adiacenti muore, come per effetto d'isolamento;
- Qualsiasi cella viva con due o tre celle vive adiacenti sopravvive alla generazione successiva;
- Qualsiasi cella viva con più di tre celle vive adiacenti muore, come per effetto di sovrappopolazione;
- Qualsiasi cella morta con esattamente tre celle vive adiacenti diventa una cella viva, come per effetto di riproduzione.


## Sviluppi futuri, esercizi e suggerimenti

Come esercizio e come sviluppi futuri vi lasciamo alcuni spunti:
- Cambiare la scrittura del progetto: dalle funzioni alle classi
- Provare ad utilizzare numpy per la gestione della matrice
- Provare ad integrarlo in Pygame
- Aggiugnere altre features: numero di vivi, overpopolazione, sottopopolazione, e tutto quello che vi viene in mente
- Provare ad integrare la lettura della matrice utilizzando un file di testo


## Link e materiale di riferimento

- Wikipedia: https://it.wikipedia.org/wiki/Gioco_della_vita
- Esempio di implementazione in Python usando numpy, pygame e altre librerie:
  - https://www.geeksforgeeks.org/conways-game-life-python-implementation/
  - https://github.com/mwharrisjr/Game-of-Life
  - https://inventwithpython.com/bigbookpython/project13.html
  - https://beltoforion.de/en/recreational_mathematics/game_of_life.php
  - https://matgomes.com/conways-game-of-life-python/
  - https://betterprogramming.pub/how-to-write-conwells-game-of-life-in-python-c6eca19c4676
  - https://www.youtube.com/watch?v=cRWg2SWuXtM&ab_channel=NeuralNine