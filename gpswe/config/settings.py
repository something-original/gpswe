from typing import Optional
from pydantic import BaseModel


class ServerSettings(BaseModel):
    """
    Пользовательские настройки библиотеки
    """

    BUFF_SIZE: Optional[int] = 8192
    HOST: Optional[str] = "0.0.0.0"
    PORT: Optional[int] = 10500
    WIALON_PROTOCOL_VERSION: Optional[str] = "2.0"
    EGTS_PROTOCOL_VERSION: Optional[str] = "1.0"
    POSTGRES_DB: Optional[str] = "gpswe_test"
    POSTGRES_USER: Optional[str] = "test"
    POSTGRES_PASSWORD: Optional[str] = "pass"
    POSTGRES_HOST: Optional[str] = "0.0.0.0"
    POSTGRES_PORT: Optional[str] = "5432"

settings = ServerSettings()
