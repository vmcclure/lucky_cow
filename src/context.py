from fastapi import Depends
from strawberry.fastapi import BaseContext

from src.dependencies import get_union_repository_dependency
from src.repositories import UnionRepository


class Context(BaseContext):
    def __init__(self, union_repo: UnionRepository) -> None:
        super().__init__()
        self.union_repo = union_repo


def get_context(
    union_repo: UnionRepository = Depends(get_union_repository_dependency),
) -> Context:
    return Context(union_repo=union_repo)
