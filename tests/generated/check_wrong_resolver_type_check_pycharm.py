import typing as t

if t.TYPE_CHECKING:
    from graphql import GraphQLResolveInfo

    import generated.scalars
    from mypackage import wrong_resolvers as resolvers
    from generated.resolver_type_base import Resolvable

    T = t.TypeVar("T")
    T_contra = t.TypeVar("T_contra", contravariant=True)
    T_co = t.TypeVar("T_co", covariant=True)


    def validate_issue_pycharm_friendly(
        query__issue__resolver: t.Callable[[None, GraphQLResolveInfo, generated.scalars.ID], Resolvable[T | None]],
        issue__id__resolver: t.Callable[[T, GraphQLResolveInfo], generated.scalars.ID],
        issue__text__resolver: t.Callable[[T, GraphQLResolveInfo], str],
        issue__parent__resolver: t.Callable[[T, GraphQLResolveInfo], T | None],
    ) -> None: ...


    validate_issue_pycharm_friendly(
        query__issue__resolver=resolvers.resolve__query__issue,
        issue__id__resolver=resolvers.resolve__issue__id,
        issue__text__resolver=resolvers.resolve__issue__text,
        issue__parent__resolver=resolvers.resolve__issue__parent,
    )
