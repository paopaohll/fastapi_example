from typing import List
from typing import Tuple
from typing import Set

import dis


def process_list(items: List[str]):
    for item in items:
        print(item.title())


def process_tuple(items_t: Tuple[int, int, str], items_s: Set[str]):
    pass


def add():
    global n
    n = n + 1


def foo():
    lst.sort()


if __name__ == "__main__":
    # fruit_list = ["apple", "banana", "watermelon"]
    # process_list(items=fruit_list)

    # t = ("apple", "banana", "watermelon")
    # print(t)
    # n = 0
    # print(dis.dis(add))
    lst = [4, 1, 3, 2]
    print(dis.dis(foo))
