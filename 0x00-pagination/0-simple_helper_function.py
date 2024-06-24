#!/usr/bin/env python3
"""Implement a simple helper function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Implement a simple helper function."""
    temp_1 = (page - 1) * page_size
    temp_2 = temp_1 + page_size
    return (temp_1, temp_2)
