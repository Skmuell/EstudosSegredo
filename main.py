from repositories.user_repository import create_user
from tables import create_tables

if __name__ == "__main__":
    create_tables()
    create_user(email="admin", username="admin", password="admin", is_active=True)
