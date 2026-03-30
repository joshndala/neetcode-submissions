class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(0)

    def top(self) -> int:
        if self.stack:
            return self.stack[0]

    def getMin(self) -> int:
        if self.stack:
            return min(self.stack) 
