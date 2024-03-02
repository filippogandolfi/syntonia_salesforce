import pandas as pd
import os
import glob

input_folder = 'input/'
output_folder = 'output/'


def convert_for_salesforce(df_azienda, df_privato):
    mandatory_columns_new = ["Cognome", "Nome", "Email", "Società", "Stato/Provincia", "Telefono",
                             "Tipologia Anagrafica",
                             "Codice Fiscale", "Partita Iva"]
    important_columns_new = ["Indicazioni Durata Nolo", "Marche Preferite", "Modello",
                             "Anticipo Offerta Sito", "Descrizione Richiesta Web", "Km Offerta Sito",
                             "Prezzo Offerta Sito",
                             "Alimentazione", "Extra", "Data Richiesta", "Promo", "Consenso Privacy",
                             "Consenso Promozioni e Newsletter"]
    optional_columns_new = ["Qualifica", "Via", "Città", "CAP", "Paese", "Indirizzo", "Cellulare", "Descrizione",
                            "Fonte del lead", "Stato", "Settore", "Valutazione", "Reddito annuale", "N. di dipendenti",
                            "ID titolare", "Attuale Modo di Finanziamento", "Canale preferenziale di comunicazione",
                            "Come ha conosciuto Syntonia?", "Commenti", "Conoscenza NLT", "Data Richiesta Appuntamento",
                            "Data esigenza consegna", "Descrizione Tipo Allestimento", "Descrizione Veicolo Permuta",
                            "Forma Giuridica", "Indicazioni di Budget", "Km Annui Percorsi", "Numero Auto",
                            "Numero Veicoli Commerciali", "Numero Veicoli Richiesti", "Parco Potenziale",
                            "Posta Certificata", "Veicolo In Permuta"]
    old_columns = ["Identificativo", "Tipo", "Agente", "Stato", "Cliente", "Indirizzo", "Città", "CAP", "Provincia",
                   "E-Mail", "Telefono", "Cellulare", "Fax", "Partita IVA", "Codice fiscale", "Nome referente",
                   "Cognome referente", "Forma giuridica", "Provenienza", "Km annui percorsi", "Fatturato", "GDPR",
                   "Marketing", "Note cliente", "Data creazione"]
    # Creating a dictionary for mapping old columns to new columns
    converter = {
        "Identificativo": None,
        "Tipo": None,
        "Agente": None,
        "Stato": None,
        "Cliente": "Società",
        "Indirizzo": "Via",
        "Città": "Città",
        "CAP": "CAP",
        "Provincia": "Stato/Provincia",
        "E-Mail": "Email",
        "Telefono": "Telefono",
        "Cellulare": "Cellulare",
        "Fax": None,
        "Partita IVA": "Partita Iva",
        "Codice fiscale": "Codice Fiscale",
        "Nome referente": "Nome",
        "Cognome referente": "Cognome",
        "Forma giuridica": "Forma Giuridica",
        "Provenienza": "Fonte del lead",
        "Km annui percorsi": "Km Annui Percorsi",
        "Fatturato": "Reddito annuale",
        "GDPR": "Consenso Privacy",
        "Marketing": "Consenso Promozioni e Newsletter",
        "Note cliente": "Note cliente",
        "Data creazione": "Data Richiesta"
    }

    # Creating a new dictionary
    new_dict = {}

    # Iterating over old dataframe and filling new dictionary
    for old_column in old_columns:
        new_column = converter.get(old_column)
        if new_column:
            print("new columns")

    print(new_dict)


def split_xls_files(input_folder, output_folder):
    files = glob.glob(f'{input_folder}/*.xlsx')
    # Find the latest file
    latest_file = max(files, key=os.path.getctime)
    # Load spreadsheet
    path = latest_file
    sheet_name = 'sheet01'

    xl = pd.read_excel(path, sheet_name=sheet_name, skiprows=2)
    df_azienda = xl[xl['Forma giuridica'] != 'Privato']
    df_privato = xl[xl['Forma giuridica'] == 'Privato']
    # df_azienda, df_privato = convert_for_salesforce(df_azienda, df_privato)
    df_azienda.to_excel('output/Azienda.xlsx', index=False)
    df_privato.to_excel('output/Privato.xlsx', index=False)
    return 'output/Azienda.xlsx', 'output/Privato.xlsx'
