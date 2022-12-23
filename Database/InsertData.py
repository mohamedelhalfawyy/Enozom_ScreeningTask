import pandas as pd


class InsertData:
    def __init__(self, databaseEngine, data):
        self.databaseEngine = databaseEngine
        self.data = data

    # Here we insert the countries data to the database
    def insert_countries(self):
        # We get the data and covert it to dataframe
        countries_df = pd.DataFrame(self.data)

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

    def insert_countries_info(self):
        # We get the data and covert it to dataframe
        countries_df = pd.DataFrame(self.data)

        # Here we remove the unsued coloumn iso3
        countries_df.drop(['iso3', 'country'], axis=1, inplace=True)

        # We rename the columns name to match the database coloumns
        countries_df.rename(columns={'code': 'country_code'}, inplace=True)

        countries_df['populationCounts'] = countries_df['populationCounts'].to_dict()

        tempCodeList = []
        tempYearList = []
        tempValueList = []

        temp_df = pd.DataFrame()

        # Here we filter the data to be able to put it in the database as in the format
        for i in range(countries_df['populationCounts'].size):
            for j in range(len(countries_df['populationCounts'][i])):
                tempCodeList.append(countries_df['country_code'][i])
                tempYearList.append(countries_df['populationCounts'][i][j]['year'])
                tempValueList.append(countries_df['populationCounts'][i][j]['value'])

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
