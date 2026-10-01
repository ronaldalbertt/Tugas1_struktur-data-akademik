from src.models.array import Array
from src.models.linked_list import LinkedList
from src.models.queue import Queue
from src.models.stack import Stack
from src.services.mahasiswa_reader import MahasiswaReader


class AkademikService:
    def __init__(self, nama_file):
        self.array_mahasiswa = Array()
        self.linked_list_mahasiswa = LinkedList()
        self.undo_stack = Stack()
        self.antrean = Queue()

        self._muat_data(nama_file)

    def _muat_data(self, nama_file):
        reader = MahasiswaReader(nama_file)
        data_mahasiswa = reader.baca_data()

        for mahasiswa in data_mahasiswa:
            self.array_mahasiswa.add_last(mahasiswa)
            self.linked_list_mahasiswa.add_last(mahasiswa)

    def tampilkan_mahasiswa(self):
        print("\n=== DATA MAHASISWA (ARRAY/LIST) ===")
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

        self.tambah_mahasiswa(nim, nama, prodi, ipk)

    def tambah_mahasiswa(self, nim, nama, prodi, ipk):
        # Menambah data pada Array dan Linked List.
        indeks_baru = len(self.array_mahasiswa) + 1
        mahasiswa_baru = self._buat_mahasiswa(
            indeks_baru, nim, nama, prodi, ipk
        )

        self.array_mahasiswa.add_last(mahasiswa_baru)
        self.linked_list_mahasiswa.add_last(mahasiswa_baru)

        # Stack menyimpan operasi terakhir untuk fitur Undo.
        self.undo_stack.push({
            "aksi": "tambah",
            "nim": nim
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

            index = self.array_mahasiswa.find_nim(nim)

            if index != -1:
                self.array_mahasiswa.remove_at(index)
                self.linked_list_mahasiswa.remove_at(index)
                print(f"Undo berhasil: data NIM {nim} dihapus kembali.")
            else:
                print("Data untuk undo tidak ditemukan.")

    def tambah_ke_antrean_dari_input(self):
        print("\n=== TAMBAH KE ANTREAN ===")

        nim = input("Masukkan NIM mahasiswa: ").strip()

        index = self.array_mahasiswa.find_nim(nim)

        if index == -1:
            print("Mahasiswa tidak ditemukan.")
            return

        mahasiswa = self.array_mahasiswa.at(index)
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

        # Pencarian menggunakan Linked List.
        index = self.linked_list_mahasiswa.find_nim(nim)

        if index == -1:
            print("Mahasiswa tidak ditemukan.")
            return

        mahasiswa = self.linked_list_mahasiswa.at(index)

        print("Data ditemukan:")
        mahasiswa.info()
        print("Index Linked List:", index)

    @staticmethod
    def _buat_mahasiswa(indeks, nim, nama, prodi, ipk):
        from src.models.mahasiswa import Mahasiswa
        return Mahasiswa(indeks, nim, nama, prodi, ipk)
