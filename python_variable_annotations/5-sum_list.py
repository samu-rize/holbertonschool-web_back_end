#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""


def sum_list(input_list: list[float]) -> float:
    """
    this is a type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float.
    """
    s: float = 0.0
    value: float= 0.0
    for value in input_list:
        s += value
    return (s)
