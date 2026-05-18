from collections import deque

class MyQueue:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.popleft()

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
    

test1 = MyQueue()
test1.push(0)
test1.push(1)
print(test1.pop())
print(test1.peek())