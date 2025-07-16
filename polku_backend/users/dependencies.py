from collections.abc import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlmodel.ext.asyncio.session import AsyncSession

from polku_backend.shared.dependencies import get_session
from polku_backend.users.domain.models import User

async def get_user_db(
    session: AsyncSession = Depends(get_session),
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    """
    Dependencia para obtener el adaptador de base de datos de usuarios.
    """
    yield SQLAlchemyUserDatabase(session, User)