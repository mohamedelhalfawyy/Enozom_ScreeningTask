from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import declarative_base

base = declarative_base()


class Models:
    def __init__(self, databaseEngine):
        self.databaseEngine = databaseEngine

    class Country(base):
        __tablename__ = "country"

        country_code = Column("country_code", VARCHAR(45), primary_key=True)
        country_name = Column("country_name", VARCHAR(255), )

        def __int__(self, country_code, country_name):
            self.country_code = country_code
            self.country_name = country_name

        def __repr__(self):
            return f"{self.country_code} {self.country_name}"

    def get_countries(self):
        base.metadata.create_all(bind=self.databaseEngine)
