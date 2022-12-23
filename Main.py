import Configurations.Database as database
import Database.InsertData as db
import Services.ApiService as apiService
import os
import sys


class Main:
    # # Here we get the engine to access the mysql database
    # engine = database.database_connection()
    #
    # # Here we get all of the data from the api
    # data = apiService.get_countries()
    #
    # # Here we make a reference for the database instance
    # databaseObject = db.InsertData(engine, data)
    #
    # # Here we call the insert countries data to send data to database
    # databaseObject.insert_countries()
    #
    # # Here we call the insert countries information data to send data to database
    # databaseObject.insert_countries_info()
    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Configurations.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    Main()
