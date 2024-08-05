from settings.db_settings import repository
from tables.user_table import UserTable


@repository
def create_user(email: str, username: str, password: str, is_active: bool, **kwargs):
    session = kwargs.get("session")
    user = UserTable(
        email=email, username=username, password=password, is_active=is_active
    )
    session.add(user)
