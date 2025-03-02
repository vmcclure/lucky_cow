import strawberry
from strawberry.types import Info

from src.context import Context
from src.types import Book


@strawberry.type
class Query:
    @strawberry.field
    async def books(
        self,
        info: Info[Context, None],
        author_ids: list[int] | None = None,
        search: str | None = None,
        limit: int | None = None,
    ) -> list[Book]:
        # конкретно здесь не увидел необходимости оборачивать в доп слой с безнес логикой, если вдруг логика появится
        # просто в контексте создадим сервис и туда уже будем прокидывать коннекты, интеграции и тд

        return await info.context.union_repo.get_books_with_autor(
            author_ids, search, limit
        )
