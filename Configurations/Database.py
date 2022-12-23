from sqlalchemy import create_engine

import Components.Constants as Constants


def database_connection():
    connectionString = f"mysql+mysqlconnector://" \
                       f"{Constants.USERNAME}:" \
                       f"{Constants.PASSWORD}@" \
                       f"{Constants.HOST}:" \
                       f"{Constants.PORT}/" \
                       f"{Constants.DBNAME}"

    engine = create_engine(connectionString)

    return engine
