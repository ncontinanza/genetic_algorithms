from typing import List

from knapsack_types import Genome, Item

def generate_items(num: int) -> List[Item]:
    return [Item(f"item{i}", i, i) for i in range(1, num+1)]


def from_genome(genome: Genome, items: List[Item]) -> List[Item]:
    result = []
    for i, item in enumerate(items):
        if genome[i] == 1:
            result += [item]

    return result


def to_string(items: List[Item]):
    return f"[{', '.join([t.name for t in items])}]"


def value(items: List[Item]):
    return sum([t.value for t in items])


def weight(items: List[Item]):
    return sum([p.weight for p in items])


def print_stats(items: List[Item]):
    print(f"Items: {to_string(items)}")
    print(f"Value {value(items)}")
    print(f"Weight: {weight(items)}")
