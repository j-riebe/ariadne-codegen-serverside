from __future__ import annotations

import sys
from typing import TypedDict

if sys.version_info >= (3, 11):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired

from graphql import GraphQLResolveInfo

from generated.scalars import ID


class Issue(TypedDict):
    id: ID
    text: str
    responses: NotRequired[list[ID]]


issue_db: list[Issue] = [
    {"id": "1", "text": "First issue"},
    {"id": "2", "text": "Second issue", "responses": ["2-1"]},
    {"id": "2-1", "text": "Response to second issue"},
]


async def resolve__query__issue(obj: None, info: GraphQLResolveInfo, id_: str) -> None | Issue:
    return next((issue for issue in issue_db if issue["id"] == id_), None)


def resolve__issue__id(obj: Issue, info: GraphQLResolveInfo) -> ID:
    return obj["id"]


def resolve__issue__text(obj: Issue, info: GraphQLResolveInfo) -> str:
    return obj["text"]


def resolve__issue__parent(obj: Issue, info: GraphQLResolveInfo) -> None | Issue:
    return next((issue for issue in issue_db if obj["id"] in issue.get("responses", [])), None)
