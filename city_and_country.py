import pandas as pd
import settings

class CountryWithCity:

    def __init__(self):
        self.df = pd.read_csv(settings.COUNTRY_CITY_CSV_FILE)
        self.unq_city = set(self.df['city'].values)
        self.unq_country = set(self.df['country'].values)

    def get_city(self, string):
        string = string.strip().split(' ')
        for val in string:
            if val.lower() in self.unq_city:
                return val

    def get_country(self, string):
        string = string.strip().split(' ')
        for val in string:
            if val.lower() in self.unq_country:
                return val

    def get_country_by_city(self, city):
        country = self.df[self.df['city'] == city.lower()]['country'].values[0]
        return country



        # string = string.strip().split(' ')
        # country = None
        # city = None
        # for val in string:
        #     if val.lower() in self.unq_country:
        #         country = val.lower()
        # cities = set(self.df[self.df['country'] == country]['city'].values)
        # for val in string:
        #     if val.lower() in cities:
        #         city = val.lower()
        # return country, city
        
