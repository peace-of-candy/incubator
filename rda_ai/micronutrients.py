from enum import Enum

from elements import Elements
from vitamins import Vitamins


def is_enum_value(s: str, e: Enum) -> bool:
    try:
        _ = e[s]
        return True
    except KeyError as _:
        return False

def is_vitamin(s: str) -> bool:
    return is_enum_value(s, Vitamins)

def is_mineral(s: str) -> bool:
    return is_enum_value(s, Elements)

def is_micronutrient(s: str) -> bool:
    return is_vitamin(s) or is_mineral(s)

def micronutrient_from_string(s: str):
    if is_mineral(s):
        return Elements[s]
    elif is_vitamin(s):
        return Vitamins[s]
    else:
        return None

all_micronutrients = [e for e in Elements] + [v for v in Vitamins]
