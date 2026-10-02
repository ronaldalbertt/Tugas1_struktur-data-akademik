class HashTable:
    """Hash Table sederhana berbasis dictionary Python.

    Key digunakan untuk mengakses value secara langsung.
    Operasi get/put/contains/remove rata-rata O(1),
    tetapi worst case dapat menjadi O(n) karena collision.
    """

    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def contains(self, key):
        return key in self.data

    def remove(self, key):
        return self.data.pop(key, None)

    def __len__(self):
        return len(self.data)
