from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from mypackage import wrong_resolvers as resolvers
    from generated.resolver_signatures import (
        QueryIssueResolver,
        IssueIdResolver,
        IssueTextResolver,
        IssueParentResolver,
    )

    T = t.TypeVar("T")
    T_contra = t.TypeVar("T_contra", contravariant=True)
    T_co = t.TypeVar("T_co", covariant=True)


    def validate_issue(
        query__issue__resolver: QueryIssueResolver[T],
        issue__id__resolver: IssueIdResolver[T],
        issue__text__resolver: IssueTextResolver[T],
        issue__parent__resolver: IssueParentResolver[T, T],
    ) -> None: ...


    validate_issue(
        query__issue__resolver=resolvers.resolve__query__issue,
        issue__id__resolver=resolvers.resolve__issue__id,
        issue__text__resolver=resolvers.resolve__issue__text,
        issue__parent__resolver=resolvers.resolve__issue__parent,
    )
