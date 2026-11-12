import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = int(math.pow(2, 31))

    def push(self, val: int) -> None:
        newValue = StackValue(val, self.min_value)
        self.stack.append(newValue)

        if val < self.min_value:
            self.min_value = val

    def pop(self) -> None:
        self.min_value = self.stack[-1].prev_min
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.min_value

class StackValue:
    def __init__(self, value, prev_min):
        self.value = value
        self.prev_min = prev_min
