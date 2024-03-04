import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


def scrape_spotahome_rent_data(url_link):
    """
    Scrapes the rent data from the spotahome website.
    :param url_link: URL of the website to scrape.
    :return: DataFrame of the rent data
    """

    response = requests.get(url_link)

    soup = BeautifulSoup(response.text, features="html.parser")

    search_title = soup.find('h1', class_="search-title__title").text
    total_entries = int(search_title.split(' ')[0])
    print(f"Total entries found: {total_entries}")

    entries_scraped = 0
    page_num = 1

    csv_file_path = 'scraped_data.csv'
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Reference Number', 'City', 'House Type', 'Available From', 'Price', 'Additional Info',
             'Ad Title', 'Link'])

    while entries_scraped < total_entries:
        url_page = url_link + 'page:' + str(page_num)

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/91.0.4472.124 Safari/537.36"

        headers = {'User Agent': user_agent}

        response = requests.get(url_page, headers=headers)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, features="html.parser")

            house_cards = soup.find_all('div', class_='HomecardContent_homecard-content__w-eHe')

            csv_file_path = 'scraped_data.csv'

            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)

                for card in house_cards:

                    try:
                        link = 'https://www.spotahome.com' + card.find('a').get('href')

                        ad_ref_numb = link.split('/')[-1]

                        ad_ref = ''.join(filter(str.isdigit, ad_ref_numb))

                        city = link.split('/')[-3]

                        house_type = card.find('span',
                                               class_='HomecardContent_homecard-content__type--'
                                                      'rebranding-style__H9Qga').text

                        available_from = card.find('span',
                                                   class_='HomecardContent_homecard-content__available-from--rebranding'
                                                          '-style__X''-SyS').text

                        ad_title = card.find('p', class_='HomecardContent_homecard-content__title--rebranding'
                                                         '-style__QCkw9').text

                        price = card.find('span', class_='Price_price__nTFG1').text

                        price_format = price.split(' ')[0]

                        additional_info = card.find('div',
                                                    class_='BaseChip_chip__label__xuuUp '
                                                           'BaseChip_chip__label--spaced__kuM8p').text.lower()

                    except AttributeError:
                        continue

                    writer.writerow([ad_ref, city, house_type, available_from, price_format, additional_info, ad_title,
                                     link])

                    entries_scraped += 1

            page_num += 1
            print(f"Printing Page: {page_num}")

        else:
            print(f"Failed to retrieve page {page_num}")
            break

    print("Data has been written to the CSV file.")


def include_property_features(file, link_col):
    """
    Includes additional property features by accessing each property link.
    :param file: dataframe to be concatenated
    :param link_col: column with access link
    :return: csv file with additional property information
    """

    def scrape_data(link):
        response = requests.get(link)

        ad_ref_numb = link.split('/')[-1]

        ad_ref = ''.join(filter(str.isdigit, ad_ref_numb))

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            try:

                property_details = soup.find('div', class_='property-title__details').find_all('span')

                try:

                    bedrooms = 'No info'
                    flatmates = 'No info'
                    bathrooms = 'No info'
                    area = 'No info'

                    for detail in property_details:
                        if 'm2' in detail:
                            area = detail.get_text().strip()
                            area_ind = area.find(' ')
                            area = area[:area_ind]
                        # Assign the elements to 'Bedrooms' and 'Bathrooms' based on their positions
                        elif 'bedrooms' in detail:
                            bedrooms = detail.get_text().strip()
                            bedrooms_ind = bedrooms.find(' ')
                            bedrooms = bedrooms[:bedrooms_ind]
                        elif 'bathrooms' in detail:
                            bathrooms = detail.get_text().strip()
                            bathrooms_ind = bathrooms.find(' ')
                            bathrooms = bathrooms[:bathrooms_ind]
                        elif 'flatmates' in detail:
                            flatmates = detail.get_text().strip()
                            flatmates_ind = flatmates.find(' ')
                            flatmates = flatmates[:flatmates_ind]

                    # # Needs selenium for 'Show all' button stimulation to retrieve all property features
                    # found_features = soup.find_all('div', class_='listing-tag')
                    #
                    # features = {
                    #     'Furnished': 'Not collected',
                    #     'A/C': 'Not collected',
                    #     'Dishwasher': 'Not collected',
                    #     'Washing machine': 'Not collected',
                    #     'Equipped kitchen': 'Not collected',
                    #     'Oven': 'Not collected',
                    #     'TV': 'Not collected',
                    #     'Pool access': 'Not collected',
                    #     'Balcony or terrace': 'Not collected',
                    #     'Parking available': 'Not collected'
                    # }
                    #
                    # for feature in found_features:
                    #     feature_name = feature.find('span', class_='listing-tag__text').get_text(strip=True)
                    #     is_not_included = 'listing-tag--not-included' in feature.get('class', [])
                    #     status = 'No' if is_not_included else 'Yes'
                    #
                    #     if feature_name in features:
                    #         features[feature_name] = status

                    # return [ad_ref, bedrooms, bathrooms, area] + list(features.values())

                    return [ad_ref, bedrooms, flatmates, bathrooms, area]

                except AttributeError as e:
                    print("Error:", e)

            except AttributeError as e:
                print("Error:", e)

    with open('rental_properties.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(
                ['Reference Number', 'Bedrooms', 'Flatmates', 'Bathrooms', 'Area'])

            # writer.writerow(
            #     ['Reference Number', 'Bedrooms', 'Bathrooms', 'Area', 'Furnished', 'A/C', 'Dishwasher',
            #      'Washing machine', 'Equipped kitchen', 'Oven', 'TV', 'Pool access', 'Balcony or terrace',
            #      'Parking Available'])

            file = pd.read_csv(file, sep=',')
            total_rows = len(file)
            for idx, link in enumerate(file[link_col], start=1):
                row = scrape_data(link)
                if row:
                    writer.writerow(row)
                    print(f'Added additional info to property {idx} out of {total_rows}.')
                else:
                    print(f'Failed to scrape data from link {idx} out of {total_rows}.')

            print('Property features have been extracted')

        else:
            print('CSV file exists and is not empty.')


if __name__ == "__main__":
    # url = "https://www.spotahome.com/s/barcelona--spain/"
    # scrape_spotahome_rent_data(url)
    scrapped_data = 'clean_data.csv'
    include_property_features(scrapped_data, 'Link')
