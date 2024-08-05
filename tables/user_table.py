from settings.db_settings import SqlAlchemyBaseEntity
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func


class UserTable(SqlAlchemyBaseEntity):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
