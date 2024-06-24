#!/usr/bin/env python3
"""Implement a simple helper function."""
import csv
from typing import List, Tuple


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
        """Implement task 1."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        temp_1, temp_2 = index_range(page, page_size)
        temp_3 = self.dataset()
        if temp_1 > len(temp_3):
            return []
        return temp_3[temp_1:temp_2]
