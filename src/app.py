import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from src.context import get_context
from src.resolvers import Query

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(  # type: ignore
    schema,
    context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
