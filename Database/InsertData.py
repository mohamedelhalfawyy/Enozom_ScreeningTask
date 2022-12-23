import pandas as pd
from sqlalchemy.orm import sessionmaker

import Services.ApiService as apiService
from Models.models import Models


class InsertData:
    def __init__(self, databaseEngine):
        self.databaseEngine = databaseEngine

    # Here we insert the countries data to the database
    def insert_countries(self):
        # Here we get all of the data from the api
        data = apiService.get_countries()

        Session = sessionmaker(bind=self.databaseEngine)
        session = Session()

        model = Models(self.databaseEngine)

        results = session.query(model.Country).values(model.Country.country_code)

        apiData = pd.DataFrame(results)

        # We get the data and covert it to dataframe
        countries_df = pd.DataFrame(data)
        temp_df = pd.DataFrame(data)

        # Here we check if the country exists in our DB through ocuntry code
        for i in range(apiData.size):
            for j in range(temp_df['code'].size):
                if apiData['country_code'][i] == temp_df['code'][j]:
                    countries_df.drop(j, inplace=True)
                    break

        tata = countries_df.copy()
        # Here we remove the unsued coloumn iso3
        countries_df.drop(['iso3', 'populationCounts'], axis=1, inplace=True)

        # We rename the columns name to match the database coloumns
        countries_df.rename(columns={'country': 'country_name', 'code': 'country_code'}, inplace=True)

        # Here we append all the data as batch insert into the database to decrease the num of visits
        rowsAffected = countries_df.to_sql(
            name="country",
            con=self.databaseEngine,
            if_exists='append',
            index=False, )

        print(f"\nNumber of rows affected for country table insertion: {rowsAffected}")

        self.insert_countries_info(tata)

    def insert_countries_info(self, countriesInfo_df):

        # Here we remove the unsued coloumn iso3
        countriesInfo_df.drop(['iso3', 'country'], axis=1, inplace=True)

        # We rename the columns name to match the database coloumns
        countriesInfo_df.rename(columns={'code': 'country_code'}, inplace=True)

        countriesInfo_df['populationCounts'] = countriesInfo_df['populationCounts'].to_dict()

        tempCodeList = []
        tempYearList = []
        tempValueList = []

        temp_df = pd.DataFrame()


        countriesInfo_df.reset_index(inplace=True)


        # Here we filter the data to be able to put it in the database as in the format
        for i in range(countriesInfo_df['populationCounts'].size):
            for j in range(len(countriesInfo_df['populationCounts'][i])):
                tempCodeList.append(countriesInfo_df['country_code'][i])
                tempYearList.append(countriesInfo_df['populationCounts'][i][j]['year'])
                tempValueList.append(countriesInfo_df['populationCounts'][i][j]['value'])

        temp_df['country_code'] = tempCodeList
        temp_df['year'] = tempYearList
        temp_df['value'] = tempValueList

        # Here we append all the data as batch insert into the database to decrease the num of visits
        rowsAffected = temp_df.to_sql(
            name="country_population",
            con=self.databaseEngine,
            if_exists='append',
            index=False, )

        print(f"\nNumber of rows affected for countryPopulation table insertion: {rowsAffected}")
