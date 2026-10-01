class Array:
    """Implementasi struktur data array-like menggunakan Python list."""

    def __init__(self):
        self.data = []

    # Menambah data di awal
    def add_first(self, data):
        self.data.insert(0, data)

    # Menambah data di akhir
    def add_last(self, data):
        self.data.append(data)

    # Menambah data berdasarkan index
    def add_at(self, index, data):
        self.data.insert(index, data)

    # Menghapus data pertama
    def remove_first(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)

    # Menghapus data terakhir
    def remove_last(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    # Menghapus data berdasarkan index
    def remove_at(self, index):
        if index < 0 or index >= len(self.data):
            return None
        return self.data.pop(index)

    # Mencari data secara linear
    def find(self, data):
        if data in self.data:
            return self.data.index(data)
        return -1

    # Mencari mahasiswa berdasarkan NIM secara linear
    def find_nim(self, nim):
        for index, mahasiswa in enumerate(self.data):
            if mahasiswa.nim == nim:
                return index
        return -1

    # Mendapatkan data berdasarkan index
    def at(self, index):
        if index < 0 or index >= len(self.data):
            return None
        return self.data[index]

    # Menampilkan data
    def display(self):
        if len(self.data) == 0:
            print("Data kosong.")
            return

        for index, data in enumerate(self.data):
            print(f"{index}.", end=" ")
            if hasattr(data, "info"):
                data.info()
            else:
                print(data)

    def __len__(self):
        return len(self.data)
