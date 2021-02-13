from pydantic import BaseSettings
from typing import Union

class Config(BaseSettings):
    KAFKA_CONNECT_INIT_CONNECTORS_PATH: str = "/connectors/"

    KAFKA_CONNECT_INIT_TIMEOUT: int = 120
    KAFKA_CONNECT_URL: str

configs = Config()
