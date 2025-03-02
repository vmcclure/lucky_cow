from functools import cache
from typing import AsyncGenerator

from databases import Database
from fastapi import Depends

from src.settings import Settings
from src.repositories import UnionRepository


def get_settings() -> Settings:
    return Settings()


@cache
class CachedDatabase(Database):
    ...


async def get_database(
    settings: Settings = Depends(get_settings),
) -> AsyncGenerator[CachedDatabase, None]:
    db = CachedDatabase(settings.POSTGRE_DSN)
    async with db:
        yield db


async def get_union_repository_dependency(
    database: CachedDatabase = Depends(get_database),
) -> UnionRepository:
    return UnionRepository(database=database)
