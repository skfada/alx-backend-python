#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
