#!/usr/bin/env python3
"""Implement a simple helper function."""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Implement a simple helper function."""
    temp_1 = (page - 1) * page_size
    temp_2 = temp_1 + page_size
    return (temp_1, temp_2)


class Server:
    """Paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache a dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        temp_1, temp_2 = index_range(page, page_size)
        data = self.dataset()
        if temp_1 > len(data):
            return []
        return data[temp_1:temp_2]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Implement hypermedia pagination."""
        page_data = self.get_page(page, page_size)
        temp_1, temp_2 = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if temp_2 < len(self.__dataset) else None,
            'prev_page': page - 1 if temp_1 > 0 else None,
            'total_pages': total_pages,
        }
        return page_info