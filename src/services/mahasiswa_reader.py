import csv

from src.models.mahasiswa import Mahasiswa
from src.models.linked_list import LinkedList


class MahasiswaReader:
    def __init__(self, nama_file):
        self.nama_file = nama_file

    def baca_data(self):
        daftar_mahasiswa = []

        with open(self.nama_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for baris in reader:
                mahasiswa = Mahasiswa(
                    int(baris["indeks"]),
                    baris["nim"],
                    baris["nama"],
                    baris["prodi"],
                    float(baris["ipk"])
                )
                daftar_mahasiswa.append(mahasiswa)

        return daftar_mahasiswa

    def baca_data_as_linked_list(self):
        daftar_mahasiswa = LinkedList()

        with open(self.nama_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for baris in reader:
                mahasiswa = Mahasiswa(
                    int(baris["indeks"]),
                    baris["nim"],
                    baris["nama"],
                    baris["prodi"],
                    float(baris["ipk"])
                )
                daftar_mahasiswa.add_last(mahasiswa)

        return daftar_mahasiswa
