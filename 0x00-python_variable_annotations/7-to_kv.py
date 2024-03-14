#!/usr/bin/env python3
"""
type-annotated function to_kv that takes a string.
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple of the string & square of v as float"""
    return (k, float(v * v))
