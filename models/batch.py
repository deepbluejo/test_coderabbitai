from itertools import combinations

from typing import TypeVar, Iterable, Iterator

T = TypeVar('T')

def batch(items: Iterable[T], bsize: int) -> Iterator[list[T]]:
    if not isinstance(bsize, int):
        raise TypeError("bsize must be an integer")
    if bsize <= 0:
        raise ValueError("bsize must be positive")
    for i in range(0,len(items),bsize):
        yield items[i:i+bsize]
