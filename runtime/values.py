from enum import Enum
class ValueType(Enum):
    Number = 1


class RuntimeVal:
    def __init__(self, type:ValueType) -> None:
        self.type = type

class NumberVal(RuntimeVal):
    def __init__(self) -> None:
        self.type = "number"
        self.value = ValueType.Number