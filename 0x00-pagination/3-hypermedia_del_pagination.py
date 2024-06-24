#!/usr/bin/env python3
"""Implement a simple helper function."""
import csv
from typing import Dict, List


class Server:
    """Paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cache a dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Implement another helper function"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary."""
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        temp_1 = []
        temp_2 = 0
        next_index = None
        temp_3 = index if index else 0
        for i, temp_4 in data.items():
            if i >= temp_3 and temp_2 < page_size:
                temp_1.append(temp_4)
                temp_2 += 1
                continue
            if temp_2 == page_size:
                next_index = i
                break
        resltt = {
            'index': index,
            'next_index': next_index,
            'page_size': len(temp_1),
            'data': temp_1,
        }
        return resltt
