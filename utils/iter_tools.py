from typing import TypeVar, Iterable, Generator

T = TypeVar('T')

def filter_by_step(items: Iterable[T], step: int = 3) -> Generator[T, None, None]:
    """Yields items from an iterable at specified intervals.

    :param items: An iterable containing elements to be filtered
    :param step: The interval at which to yield items. Items whose position is
        divisible by this value will be yielded. Defaults to 3
    :yields: Elements from the input iterable at positions divisible by the step value

    :Example:

    >>> list(filter_by_step([1, 2, 3, 4, 5, 6], step=2))
    [2, 4, 6]
    >>> list(filter_by_step(range(1, 7), step=3))
    [3, 6]
    """
    for item in items:
        if item % step == 0:
            yield item


