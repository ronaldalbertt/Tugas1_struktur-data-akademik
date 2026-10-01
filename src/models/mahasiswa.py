class Mahasiswa:
    def __init__(self, indeks, nim, nama, prodi, ipk):
        self.indeks = indeks
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.ipk = ipk

    def predikat(self):
        if self.ipk >= 3.50:
            return "Sangat Memuaskan"
        elif self.ipk >= 3.00:
            return "Memuaskan"
        elif self.ipk >= 2.75:
            return "Cukup"
        else:
            return "Kurang"

    def info(self):
        print(
            f"NIM: {self.nim} | "
            f"Nama: {self.nama} | "
            f"Prodi: {self.prodi} | "
            f"IPK: {self.ipk:.2f} | "
            f"Predikat: {self.predikat()}"
        )

    def __repr__(self):
        return f"{self.nim} - {self.nama}"
