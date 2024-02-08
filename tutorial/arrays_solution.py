from typing import Iterable, Tuple


def min_max(arr: Iterable[int]) -> Tuple[int, int]:
    """Get the min and max of an iterable.
    
    parameters
    ----------
    arr: Iterable[int]
        List with integer values.
    
    returns
    -------
    tuple[int, int]
        minimum and maximum value of arr.
    """
    return min(arr), max(arr)
