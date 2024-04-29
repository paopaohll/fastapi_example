from typing import List
from typing import Tuple
from typing import Set


def process_list(items: List[str]):
    for item in items:
        print(item.title())


def process_tuple(items_t: Tuple[int, int, str], items_s: Set[str]):
    pass


if __name__ == "__main__":
    fruit_list = ["apple", "banana", "watermelon"]
    process_list(items=fruit_list)

    t = ("apple", "banana", "watermelon")
    print(t)
