class Queue:
    """Queue dengan prinsip FIFO."""

    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)

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
