from enum import Enum

from vitamins import Vitamins
from elements import Elements

def is_micronutrient(s: str) -> str:
    def is_enum_value(s: str, e: Enum) -> bool:
        try:
            _ = e[s]
            return True
        except KeyError as _:
            return False

    return is_enum_value(s, Vitamins) or is_enum_value(s, Elements)


