from collections.abc import AsyncGenerator
from sqlmodel.ext.asyncio.session import AsyncSession
from polku_backend.shared.database import async_session_maker

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependencia de FastAPI que provee una sesión de base de datos por petición.
    """
    async with async_session_maker() as session:
        yield session