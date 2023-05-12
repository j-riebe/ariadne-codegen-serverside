from __future__ import annotations

import typing as t

from graphql import GraphQLResolveInfo

from generated.resolver_type_base import Resolvable
from generated.resolver_type_check_protocols import T_co, T_contra
from generated.scalars import ID


class QueryIssueResolver(t.Protocol[T_co]):
    def __call__(self, obj: None, info: GraphQLResolveInfo, id_: ID) -> Resolvable[T_co | None]: ...


class IssueIdResolver(t.Protocol[T_contra]):
    def __call__(self, obj: T_contra, info: GraphQLResolveInfo) -> Resolvable[ID]: ...


class IssueTextResolver(t.Protocol[T_contra]):
    def __call__(self, obj: T_contra, info: GraphQLResolveInfo) -> Resolvable[str]: ...


class IssueParentResolver(t.Protocol[T_contra, T_co]):
    def __call__(self, obj: T_contra, info: GraphQLResolveInfo) -> Resolvable[T_co | None]: ...
