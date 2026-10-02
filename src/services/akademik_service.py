from src.models.array import Array
from src.models.hash_table import HashTable
from src.models.linked_list import LinkedList
from src.models.queue import Queue
from src.models.stack import Stack
from src.services.mahasiswa_reader import MahasiswaReader


class AkademikService:
    def __init__(self, nama_file):
        self.array_mahasiswa = Array()
        self.linked_list_mahasiswa = LinkedList()
        self.indeks_nim = HashTable()
        self.undo_stack = Stack()
        self.antrean = Queue()

        self._muat_data(nama_file)

    def _muat_data(self, nama_file):
        reader = MahasiswaReader(nama_file)
        data_mahasiswa = reader.baca_data()

        for mahasiswa in data_mahasiswa:
            self.array_mahasiswa.add_last(mahasiswa)
            self.linked_list_mahasiswa.add_last(mahasiswa)
            self.indeks_nim.put(mahasiswa.nim, mahasiswa)

    def tampilkan_mahasiswa(self):
        print("\n=== DATA MAHASISWA (ARRAY) ===")
        self.array_mahasiswa.display()

    def tambah_mahasiswa_dari_input(self):
        print("\n=== TAMBAH MAHASISWA ===")

        nim = input("NIM   : ").strip()
        nama = input("Nama  : ").strip()
        prodi = input("Prodi : ").strip()
        ipk_teks = input("IPK   : ").strip()

        if nim == "" or nama == "" or prodi == "":
            print("Data tidak boleh kosong.")
            return

        try:
            ipk = float(ipk_teks)
        except ValueError:
            print("IPK harus berupa angka.")
            return

        if ipk < 0 or ipk > 4:
            print("IPK harus berada pada rentang 0 sampai 4.")
            return

        self.tambah_mahasiswa(nim, nama, prodi, ipk)

    def tambah_mahasiswa(self, nim, nama, prodi, ipk):
        if self.indeks_nim.contains(nim):
            print("NIM sudah terdaftar.")
            return

        indeks_baru = len(self.array_mahasiswa) + 1
        mahasiswa_baru = self._buat_mahasiswa(
            indeks_baru, nim, nama, prodi, ipk
        )

        self.array_mahasiswa.add_last(mahasiswa_baru)
        self.linked_list_mahasiswa.add_last(mahasiswa_baru)
        self.indeks_nim.put(nim, mahasiswa_baru)

        self.undo_stack.push({
            "aksi": "tambah",
            "nim": nim,
        })

        print("Mahasiswa berhasil ditambahkan.")

    def undo(self):
        print("\n=== UNDO ===")

        operasi = self.undo_stack.pop()

        if operasi is None:
            print("Tidak ada operasi yang dapat di-undo.")
            return

        if operasi["aksi"] == "tambah":
            nim = operasi["nim"]
            mahasiswa = self.indeks_nim.get(nim)

            if mahasiswa is None:
                print("Data untuk undo tidak ditemukan.")
                return

            index = self.array_mahasiswa.find_nim(nim)
            self.array_mahasiswa.remove_at(index)
            self.linked_list_mahasiswa.remove_at(index)
            self.indeks_nim.remove(nim)

            print(f"Undo berhasil: data NIM {nim} dihapus kembali.")

    def tambah_ke_antrean_dari_input(self):
        print("\n=== TAMBAH KE ANTREAN ===")

        nim = input("Masukkan NIM mahasiswa: ").strip()
        mahasiswa = self.indeks_nim.get(nim)

        if mahasiswa is None:
            print("Mahasiswa tidak ditemukan.")
            return

        self.antrean.enqueue(mahasiswa)

        print(f"{mahasiswa.nama} masuk ke antrean.")
        self.antrean.display()

    def proses_antrean(self):
        print("\n=== PROSES ANTREAN ===")

        mahasiswa = self.antrean.dequeue()

        if mahasiswa is None:
            print("Antrean kosong.")
            return

        print("Mahasiswa yang diproses:")
        mahasiswa.info()
        self.antrean.display()

    def cari_mahasiswa_dari_input(self):
        print("\n=== CARI MAHASISWA BERDASARKAN NIM ===")

        nim = input("Masukkan NIM: ").strip()
        mahasiswa = self.indeks_nim.get(nim)

        if mahasiswa is None:
            print("Mahasiswa tidak ditemukan.")
            return

        print("Data ditemukan:")
        mahasiswa.info()
        print("Pencarian menggunakan Hash Table: rata-rata O(1), worst case O(n)")

    @staticmethod
    def _buat_mahasiswa(indeks, nim, nama, prodi, ipk):
        from src.models.mahasiswa import Mahasiswa
        return Mahasiswa(indeks, nim, nama, prodi, ipk)
