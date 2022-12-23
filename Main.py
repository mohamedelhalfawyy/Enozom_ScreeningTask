import Configurations.Database as database
import Database.InsertData as db
import Services.ApiService as apiService


class Main:
    # Here we get the engine to access the mysql database
    engine = database.database_connection()

    # Here we get all of the data from the api
    data = apiService.get_countries()

    # Here we make a reference for the database instance
    databaseObject = db.InsertData(engine, data)

    # Here we call the insert countries data to send data to database
    databaseObject.insert_countries()

    # Here we call the insert countries information data to send data to database
    databaseObject.insert_countries_info()
