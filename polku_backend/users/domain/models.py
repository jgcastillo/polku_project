from uuid import UUID

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlmodel import Field, SQLModel

class User(SQLModel, SQLAlchemyBaseUserTableUUID, table=True):
    # Heredamos de SQLModel y de la clase base de fastapi-users.
    # Ahora, redefinimos los campos para que SQLModel/Pydantic los entiendan.

    # El campo 'id' ya está bien definido por SQLAlchemyBaseUserTableUUID,
    # pero lo redefinimos para que SQLModel lo reconozca como llave primaria.
    id: UUID = Field(default=None, primary_key=True)

    # Redefinimos los campos de la clase base con tipos estándar de Python
    # y las opciones de columna de base de datos que necesitamos.
    email: str = Field(max_length=320, unique=True, index=True, nullable=False)
    hashed_password: str = Field(max_length=1024, nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    is_superuser: bool = Field(default=False, nullable=False)
    is_verified: bool = Field(default=False, nullable=False)

    # Aquí puedes seguir añadiendo tus campos personalizados
    full_name: str | None = Field(default=None)