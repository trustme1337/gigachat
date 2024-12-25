import os
from pydantic import BaseModel, Field

class TgBot(BaseModel):
    token: str = Field(..., env="TG_BOT_TOKEN")

class GigaChat(BaseModel):
    token: str = Field(..., env="GIGACHAT_TOKEN")

class Config(BaseModel):
    tg_bot: TgBot
    gigachat_token: str


def load_config() -> Config:
    return Config(
        tg_bot=TgBot(token=os.getenv("TG_BOT_TOKEN", "7646939242:AAEz74joS6w32MisRZlSEGNS_QktGKZzbpQ")),
        gigachat_token=os.getenv("GIGACHAT_TOKEN", "NTQwY2M1ODMtNTM5OC00ZDk3LTg2MDAtMmJjODhjYjdhYWIxOjMxNGVhMjI1LTczMzYtNDc3NC05Zjk2LWRjMTFlZjRkNmQyZA==")
    )
