from collections import deque


class Queue:
    """Queue dengan prinsip FIFO menggunakan collections.deque."""

    def __init__(self):
        self.data = deque()

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.popleft()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        if len(self.data) == 0:
            print("Antrean kosong.")
            return

        print("Antrean:", " <- ".join(str(item) for item in self.data))

    def __len__(self):
        return len(self.data)
