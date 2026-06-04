class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_val = self.stack[-1][1]

            self.stack.append((val, min(min_val, val)))
    
    def pop(self) -> None:
        if not self.stack:
            raise IndexError('The stack is empty')
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError('The stack is empty')
        return self.stack[-1][0]
            
    def get_min(self) -> int:
        if not self.stack:
            raise IndexError('The stack is empty')
        return self.stack[-1][1]
