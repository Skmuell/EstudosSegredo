from settings.db_settings import engine
from tables.user_table import UserTable

def create_tables():
    UserTable.metadata.create_all(bind=engine)
    