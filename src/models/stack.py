class Stack:
    """Stack dengan prinsip LIFO."""

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)
