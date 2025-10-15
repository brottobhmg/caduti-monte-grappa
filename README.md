# Caduti Monte Grappa

Progetto di scraping web per la raccolta dei dati sui caduti italiani della Prima Guerra Mondiale sepolti al Sacrario del Monte Grappa.

## Descrizione

Questo script Python estrae automaticamente i dati dal sito ufficiale del Monte Grappa (montegrappa.org) riguardanti i soldati italiani caduti durante la Grande Guerra. I dati vengono organizzati e salvati in formato CSV per facilitarne l'analisi e la consultazione.

Il Monte Grappa, situato nelle Prealpi Venete, fu teatro di sanguinose battaglie durante la Prima Guerra Mondiale. Il Sacrario Militare conserva i resti di migliaia di soldati italiani e austro-ungarici.

## Caratteristiche

- Scraping automatico di tutte le pagine del database online
- Estrazione di informazioni complete per ogni caduto
- Salvataggio in formato CSV per facile consultazione
- Gestione automatica della paginazione (23 pagine totali, ~2284 record)

## Requisiti

- Python 3.x
- requests
- beautifulsoup4

## Installazione

```bash
pip install requests beautifulsoup4
```

## Utilizzo

Esegui lo script per scaricare tutti i dati:

```bash
python main.py
```

Lo script creerà un file `caduti.csv` contenente tutti i dati dei caduti.

## Struttura Dati

Il file CSV generato contiene le seguenti colonne:

- **tomba**: Numero identificativo della tomba
- **grado**: Grado militare (es. Soldato, Caporale, Tenente, ecc.)
- **cognome**: Cognome del caduto
- **nome**: Nome del caduto
- **corpo**: Corpo militare di appartenenza (numero)
- **data**: Data di morte (formato gg/mm/aaaa)
- **luogo**: Luogo di morte
- **medaglia**: Eventuali medaglie al valore

## Esempio di Output

```csv
tomba,grado,cognome,nome,corpo,data,luogo,medaglia
1,Soldato,Acerbi,Primo,207,25/07/1918,Galleria V.E.,
2,Soldato,Acerbis,Santo,139,18/09/1918,Val Piana,
3,Caporale,Adami,Gio Batta,22,,Galleria V.E.,
```

## Fonte Dati

I dati provengono dal sito ufficiale: [montegrappa.org](https://www.montegrappa.org)

## Note

- Lo script rispetta la struttura del sito sorgente
- Alcuni campi potrebbero essere vuoti se i dati non sono disponibili
- La prima esecuzione crea il file CSV, le successive sovrascrivono i dati esistenti

## Licenza

Questo progetto è fornito come strumento di archiviazione storica. I dati appartengono alle fonti ufficiali.

## Contatti

Per informazioni sul Sacrario del Monte Grappa: [www.montegrappa.org](https://www.montegrappa.org)