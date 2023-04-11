from redis_om import (
    HashModel,
    Field,
    Migrator
)


class UserData(HashModel):
    phone: str = Field(index=True)
    address: str


Migrator().run()