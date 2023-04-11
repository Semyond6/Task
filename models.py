from redis_om import (
    HashModel,
    Field,
    Migrator
)


class UserData(HashModel):
    """Класс пользовательских данных."""
    
    phone: str = Field(primary_key= True, index=True)
    address: str


Migrator().run()