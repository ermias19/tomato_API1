                  #TOMATO_API1
Documentazione sull'API di pomodoro
Benvenuti nella documentazione per l'API Tomato! Questa guida fornisce una panoramica dell'API Tomato basata su Django e dei suoi componenti essenziali.

Modelli
1. Modello di ristorante
Campi:
resto_id: campo intero (chiave primaria)
nome_resto: CharField
2. Modello di ricetta
Campi:
Recipe_id: campo intero (chiave primaria)
Nome ricetta: CharField
Ristorante: ForeignKey per il modello Ristorante (on_delete=models.CASCADE)
3. Modello degli ingredienti
Campi:
ing_id: campo intero (chiave primaria)
Nome ingrediente: CharField
4. Modello degli ingredienti del ristorante
Campi:
Ristorante: ForeignKey per il modello Ristorante (on_delete=models.CASCADE)
ingrediente: modello ForeignKey to Ingredient (on_delete=models.CASCADE)
5. Modello degli ingredienti della ricetta
Campi:
ricetta: ForeignKey per il modello della ricetta (on_delete=models.CASCADE)
Ingrediente: ForeignKey al modello Ingrediente (on_delete=models.CASCADE)
Visualizzazioni
1. Ristorante_vista
Descrizione: fornisce endpoint API per la creazione e l'elenco dei ristoranti.
Metodi:
OTTIENI: Elenca tutti i ristoranti.
POST: Crea un nuovo ristorante.
2. Vista_dettaglio_ristorante
Descrizione: fornisce endpoint API per il recupero, l'aggiornamento e l'eliminazione di un ristorante specifico.
Metodi:
GET: recupera i dettagli di un ristorante specifico.
METTI/PATCH: Aggiorna i dettagli di un ristorante specifico.
ELIMINA: elimina un ristorante specifico.
3. restorant_spec_recipt
Descrizione: fornisce l'endpoint API per elencare le ricette associate a un ristorante specifico.
Metodi:
OTTIENI: Elenca tutte le ricette associate a un ristorante specifico.
4. Vista_ingrediente
Descrizione: fornisce endpoint API per la creazione e l'elenco degli ingredienti.
Metodi:
OTTIENI: elenca tutti gli ingredienti.
POST: crea un nuovo ingrediente.
5. Vista_dettaglio_ingrediente
Descrizione: fornisce endpoint API per il recupero, l'aggiornamento e l'eliminazione di un ingrediente specifico.
Metodi:
GET: recupera i dettagli di un ingrediente specifico.
METTI / PATCH: aggiorna i dettagli di un ingrediente specifico.
ELIMINA: elimina un ingrediente specifico.
6. inred_resto_recipt
Descrizione: fornisce endpoint API per creare ed elencare le relazioni ristorante-ingrediente in base a un ingrediente specifico.
Metodi:
GET: elenca tutte le relazioni ristorante-ingrediente basate su un ingrediente specifico.
POST: crea una nuova relazione ristorante-ingrediente.
7. Visualizzazione_ricetta
Descrizione: fornisce endpoint API per la creazione e l'elenco delle ricette.
Metodi:
OTTIENI: Elenca tutte le ricette.
POST: crea una nuova ricetta.
8. Visualizzazione_dettagli_ricetta
Descrizione: fornisce endpoint API per il recupero, l'aggiornamento e l'eliminazione di una ricetta specifica.
Metodi:
GET: recupera i dettagli di una ricetta specifica.
METTI / PATCH: aggiorna i dettagli di una ricetta specifica.
ELIMINA: Elimina una ricetta specifica.
9. ricetta_ing_recipt
Descrizione: fornisce endpoint API per creare ed elencare le relazioni ricetta-ingrediente in base a una ricetta specifica.
Metodi:
GET: elenca tutte le relazioni ricetta-ingrediente in base a una ricetta specifica.
POST: crea una nuova relazione ricetta-ingrediente.
Dockerfile
Immagine di base:
Utilizza Python 3.10 come immagine di base per il contenitore Docker.
Configurazione dell'ambiente:
Imposta la modalità senza buffer per Python.
Directory di lavoro:
Imposta la directory di lavoro su /code/.
Requisiti per la copia:
Copia il file require.txt nel contenitore.
Installa le dipendenze:
Installa le dipendenze Python specificate in requisiti.txt.
Copia codice:
Copia tutti i file dalla directory locale alla directory /code/ all'interno del contenitore.
Esegui migrazioni:
Applica le migrazioni del database Django.
Porta esposta:
Informa Docker che l'applicazione utilizza la porta 8000.
Comando predefinito:
Imposta il comando predefinito per eseguire il server di sviluppo Django.

#pomodoro_API1
Documentazione sull'API di pomodoro
Benvenuti nella documentazione per l'API Tomato! Questa guida fornisce una panoramica dell'API Tomato basata su Django e dei suoi componenti essenziali.

Modelli
1. Modello di ristorante
Campi:
resto_id: campo intero (chiave primaria)
nome_resto: CharField
2. Modello di ricetta
Campi:
Recipe_id: campo intero (chiave primaria)
Nome ricetta: CharField
Ristorante: ForeignKey per il modello Ristorante (on_delete=models.CASCADE)
3. Modello degli ingredienti
Campi:
ing_id: campo intero (chiave primaria)
Nome ingrediente: CharField
4. Modello degli ingredienti del ristorante
Campi:
Ristorante: ForeignKey per il modello Ristorante (on_delete=models.CASCADE)
ingrediente: modello ForeignKey to Ingredient (on_delete=models.CASCADE)
5. Modello degli ingredienti della ricetta
Campi:
ricetta: ForeignKey per il modello della ricetta (on_delete=models.CASCADE)
Ingrediente: ForeignKey al modello Ingrediente (on_delete=models.CASCADE)
Visualizzazioni
1. Ristorante_vista
Descrizione: fornisce endpoint API per la creazione e l'elenco dei ristoranti.
Metodi:
OTTIENI: Elenca tutti i ristoranti.
POST: Crea un nuovo ristorante.
2. Vista_dettaglio_ristorante
Descrizione: fornisce endpoint API per il recupero, l'aggiornamento e l'eliminazione di un ristorante specifico.
Metodi:
GET: recupera i dettagli di un ristorante specifico.
METTI/PATCH: Aggiorna i dettagli di un ristorante specifico.
ELIMINA: elimina un ristorante specifico.
3. restauro
#####################################english version is included in the specific .py files######################################################33 
