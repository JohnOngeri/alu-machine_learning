#!/usr/bin/env python3
"""
defines a function that adds squares from i to n
"""


def summation_i_squared(n):
    """
    The moduleuses squares formula to add squares upto n
    """
    if isinstance(n, int) and n >= 1:
        return (n * (n + 1) * (2 * n + 1))
    else:
        return None
