from typing import Any

from databases import Database
from databases.interfaces import Record

from src.types import Book, Author


class GetBooksWithAutor:
    def __init__(self, database):
        self.database = database

    QUERY = """
        SELECT b.title as title, a.name as name 
        FROM books as b join authors as a on b.author_id = a.id 
        {query_filters}{query_limit}
        """

    async def __call__(
        self,
        author_ids: list[int] | None = None,
        search: str | None = None,
        limit: int | None = None,
    ) -> list[Book]:
        filters = []
        values: dict[str, Any] = {}
        query_filters = ""
        query_limit = ""

        if author_ids:
            filters.append("b.author_id = ANY (:author_ids)")
            values["author_ids"] = author_ids
        if search:
            filters.append("b.title ILIKE :search")
            values["search"] = f"%{search}%"

        if filters:
            query_filters = f"WHERE {' and '.join(filters)} "

        if limit:
            query_limit = "LIMIT :book_limit"
            values["book_limit"] = limit

        query = self.QUERY.format(query_filters=query_filters, query_limit=query_limit)

        result_rows: list[Record] = await self.database.fetch_all(query, values)

        return [
            Book(title=row["title"], author=Author(name=row["name"]))
            for row in result_rows
        ]


class UnionRepository:
    def __init__(self, database: Database) -> None:
        self.get_books_with_autor = GetBooksWithAutor(database=database)
