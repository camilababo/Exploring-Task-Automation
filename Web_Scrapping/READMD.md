## Web Scrapping Rental Data

This project contains scripts to compile and extract information on rental properties and respective features:

- [explore_city_rental_prices.py](explore_city_rental_prices.py): Scrapes _rentahome_'s website to extracts information on all properties listed, saving their reference number, city, type of property, rental information, price, soonest availability, title and link. A second function retrieves properties' features such as number of rooms, flatmates, bathrooms and area.
- [retrieve_specific_neighbourhood.py](retrieve_specific_neighbourhood.py): Extracts the most common neighbourhood's names to retrieve information on properties's specific locations.

An analysis was also performed on ll extracted information and can be explored in:
- [barcelona-rental-properties-analysis.ipynb](barcelona-rental-properties-analysis.ipynb).

Extracted data:
- [barcelona_rental_data.csv](barcelona_rental_data.csv): Compiled data on Barcelona's rental properties.
- [scrapped_data.csv](scraped_data.csv): Scraped data without properties features.
- [clean_data.csv](clean_data.csv): Scraped data with information on specific neighbourhoods.
- [additional_rental_data.csv](additional_rental_data.csv): Scrapped data on properties features.
