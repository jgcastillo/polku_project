from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from polku_backend.shared.config import settings

# Creamos el motor de base de datos asíncrono usando la URL de nuestra configuración
engine = create_async_engine(settings.database_url, echo=True, future=True)

# Creamos una fábrica de sesiones asíncronas
# expire_on_commit=False evita que los objetos se desvinculen de la sesión después de un commit
async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)