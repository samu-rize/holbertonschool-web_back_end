#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each element in the input iterable.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
