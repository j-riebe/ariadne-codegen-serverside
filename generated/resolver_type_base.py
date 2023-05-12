import typing as t

_T = t.TypeVar("_T")

SimpleResolvable = t.Union[_T, t.Awaitable[_T]]  # mypy doesn't get this when using pipe (|) syntax
CallableResolvable = t.Callable[[], SimpleResolvable[_T]] | t.Awaitable[t.Callable[[], SimpleResolvable[_T]]]

Resolvable = SimpleResolvable[_T] | CallableResolvable[_T]
Iterable = t.Iterable[_T] | t.AsyncIterable[_T]
