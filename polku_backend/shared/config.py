from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Configuración de la Base de Datos
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def database_url(self) -> str:
        """
        Genera la URL de conexión asíncrona para PostgreSQL.
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Carga las variables desde un archivo .env si existe (útil para desarrollo local)
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()