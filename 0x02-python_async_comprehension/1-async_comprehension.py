#!/usr/bin/env python3
"""
Module provides an async list....
"""
from typing import List
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns:
        List[float]: a list of floats generated by the
        async_generator
    """
    return [num async for num in async_generator()]