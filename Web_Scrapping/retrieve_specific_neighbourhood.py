import pandas as pd


def extract_specific_location(data_frame, column_name, encoding, neighborhoods_list):
    """
    Extracts words from ad's title to find accommodation's specific location.
    :param data_frame: scraped file
    :param column_name: name of column to find locations
    :param encoding: dataset's encoding
    :param neighborhoods_list: list of neighborhood names
    :return: csv file with further information on location
    """

    data_frame = pd.read_csv(data_frame, sep=',', encoding=encoding)

    def keep_neighborhood_words(text, neighborhood_names):
        words = text.replace(',', '')
        words = words.split()
        filtered_words = [word for word in words if word in neighborhood_names]

        if not filtered_words:
            filtered_words.append('Barcelona')

        filtered_title = ' '.join(filtered_words)

        return filtered_title.strip()

    data_frame[column_name] = data_frame[column_name].str.replace(',', '')
    data_frame['Specific Location'] = data_frame[column_name].apply(lambda x: keep_neighborhood_words(x,
                                                                                                    neighborhoods_list))

    data_frame.to_csv('clean_data.csv', index=False, encoding='latin1')

    print('Data has been written to the CSV file.')


if __name__ == "__main__":
    csv_file = 'scraped_data.csv'
    col_name = 'Ad Title'
    neighborhoods = [
        "L'Esquerra", "de", "l'Eixample",
        "Eixample",
        "Passeig",
        "Esplugues", "de", "Llobregat",
        "Sant", "Feliu", "de", "Llobregat",
        "La", "Salut",
        "Poblenou",
        "Sant Gervasi",
        "L'Hospitalet",
        "San", "Gervasi-Galvany",
        "Poble-Sec",
        "Abando", "Indautxu",
        "Vallarca",
        "Cubelles",
        "Sentmenat",
        "Hospitalet", "de", "Llobregat",
        "El", "Raval",
        "Rosas",
        "Gràcia",
        "El", "Born",
        "El", "Gòtic",
        "Sant", "Antoni",
        "Sant", "Andreu",
        "El", "Poble", "Sec",
        "Porta",
        "Ciutat", "Vella",
        "Carrer", "de", "Balmes",
        "Barri", "Gòtic",
        "Barri", "Gotic",
        "Horta-Guinardó",
        "Catalunya",
        "Sitges",
        "Fabra", "I", "Puig",
        "Les", "Corts",
        "Bellaterra",
        "El", "Barri", "Gotic",
        "Tallers",
        "Carrer", "de", "Balmes",
        "Sants-Montjuïc",
        "Sant", "Adrià", "de", "Besòs",
        "Sant", "Cugat", "del", "Vallès",
        "Sarrià-Sant", "Gervasi",
        "Cornellà", "de", "Llobregat",
        "Mataró",
        "Can", "Baró",
        "Gervasi",
        "Montjuïc",
        "El", "Farró",
        "Sant", "Martí",
        "Horta", "Guinardó",
        "El", "Guinardó",
        "El", "Guinard",
        "Portaferrisa",
        "La", "Boquería",
        "La", "Paloma",
        "Cornellà",
        "Vila", "Olímpica",
        "Ciutadella", "Olímpica",
        "La", "Vila", "Olímpica", "del", "Poblenou",
        "La", "Dreta", "de", "l'Eixample",
        "La", "Esquerra", "de", "l'Eixample",
        "L'Esquerra", "de", "l'Eixample",
        "L'Dreta", "de", "l'Eixample",
        "Sant", "Andreu",
        "Terrassa",
        "Vallvidrera",
        "Guifré",
        "La", "Sagrada", "Família",
        "Plaça", "Espanya",
        "Gothic", "Quarter",
        "L'Hospitalet", "De", "Llo",
        "l'Eixample", "Dreta",
        "Camp", "de", "l'Arpa",
        "Segur", "de", "Calafell",
        "Badalona",
        "Sagrada", "Familia",
        "Horta",
        "Collblanc",
        "La", "Barceloneta",
        "L'Hospitalet", "de", "Llobregat",
        "El", "Carmel",
        "La", "Rambla",
        "Collblanc",
        "El", "Born",
        "El", "Clot",
        "Poble-sec",
        "Barri", "Gotic",
        "Navas",
        "Born",
        "Sants",
        "Gothic",
        "Madrid",
        "Gracia",
        "Gotico",
        "Nou Barris",
        "L'Eixample",
        "Port",
        "Bairro", "Gótico",
        "Castelldefels",
        "Fort", "Pienc",
        "Sants-Badal",
        "Las", "Ramblas",
        "Nou", "Barris",
        "Sabadell",
        "Sarrià",
        " Avenida", "Gaudi",
        "Universidad",
        "Navas",
        "Rosselló",
        "Provença",
        "Compte", "Borrell",
        "Fontana",
        "Pedralbes",
        "Olivella",
        "Valencia",
        "Gran", "Via",
        "Amadeu", "Torner",
        "Barrio",
        "Liceu"
        "El", "Prat", "de", "Llobregat",
        "Ciutat", "Vella",
    ]
    extract_specific_location(csv_file, col_name, encoding='latin1', neighborhoods_list=neighborhoods)
