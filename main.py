from settings.db_settings import SqlAlchemyBaseEntity, engine, get_session, repository
from sqlalchemy import Column, Integer, String


class Person(SqlAlchemyBaseEntity):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


def create_tables():
    Person.metadata.create_all(bind=engine)


@repository
def create_person(name: str, age: int, **kwargs):
    session = kwargs.get("session")
    person = Person(name="João", age=22)
    session.add(person)


if __name__ == "__main__":
    create_person(name="João", age=22)
    # create_tables()
    # with get_session() as session:
    #     person = Person(name="João", age = 22)
    #     session.add(person)
    #     session.commit()
    #     print("Chama na bota")
