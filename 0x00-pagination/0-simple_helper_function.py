#!/usr/bin/env python3
"""Pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple containing start and end index corresponding to a page"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
