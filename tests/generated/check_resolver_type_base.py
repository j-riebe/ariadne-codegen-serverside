from generated.resolver_type_base import SimpleResolvable, CallableResolvable, Resolvable, Iterable  # type: ignore


def int_factory() -> int:
    return 1


async def async_int_factory() -> int:
    return 1


class IntIterator:
    def __iter__(self):
        yield 1


class AsyncIntIterator:
    async def __aiter__(self):
        yield 1


def check_simple() -> SimpleResolvable[int]:
    if ...: return 1
    if ...: return async_int_factory()
    return  # type: ignore


def check_callable() -> CallableResolvable[int]:
    if ...: return lambda: 1
    if ...: return async_int_factory
    return  # type: ignore


def check_resolvable() -> Resolvable[int]:
    if ...: return 1
    if ...: return lambda: 1
    if ...: return async_int_factory
    if ...: return async_int_factory()
    return  # type: ignore


def check_iterable() -> Iterable[Resolvable[int]]:
    if ...: return IntIterator()
    if ...: return AsyncIntIterator()
    # Todo: With the current definition of Iterable[Resolvable] there should also be
    #  sync and async iterators of the sync and async int_factory.
    #  Check if this is really supported by ariadne.
    return  # type: ignore
