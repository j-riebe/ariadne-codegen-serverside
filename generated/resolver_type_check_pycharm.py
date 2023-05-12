import typing as t

if t.TYPE_CHECKING:
    from graphql import GraphQLResolveInfo

    from mypackage import resolvers
    from .scalars import ID
    from .resolver_type_base import Resolvable

    T = t.TypeVar("T")
    T_contra = t.TypeVar("T_contra", contravariant=True)
    T_co = t.TypeVar("T_co", covariant=True)


    def validate_issue_pycharm_friendly(
        query__issue__resolver: t.Callable[[None, GraphQLResolveInfo, ID], Resolvable[T | None]],
        issue__id__resolver: t.Callable[[T, GraphQLResolveInfo], ID],
        issue__text__resolver: t.Callable[[T, GraphQLResolveInfo], str],
        issue__parent__resolver: t.Callable[[T, GraphQLResolveInfo], T | None],
    ) -> None:
        """
        PyCharms doesn't detect typing mistakes when using protocols yet (2023.1.1).

        But when using Callable explicitly it works.
        """


    validate_issue_pycharm_friendly(
        query__issue__resolver=resolvers.resolve__query__issue,
        issue__id__resolver=resolvers.resolve__issue__id,
        issue__text__resolver=resolvers.resolve__issue__text,
        issue__parent__resolver=resolvers.resolve__issue__parent,
    )
