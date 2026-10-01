import time

from src.services.mahasiswa_reader import MahasiswaReader


def main():
    reader = MahasiswaReader("data/data_mahasiswa_dummy_200.csv")

    # Versi Python list (array-like)
    list_mahasiswa = reader.baca_data()

    # Versi Linked List
    linked_list_mahasiswa = reader.baca_data_as_linked_list()

    # Menggunakan index tengah agar data mudah diuji.
    index_uji = 98

    print("=== AKSES DATA BERDASARKAN INDEX ===")
    print("Jumlah data:", len(list_mahasiswa))
    print("Index yang diuji:", index_uji)

    waktu_mulai = time.perf_counter()
    mahasiswa_list = list_mahasiswa[index_uji]
    waktu_selesai = time.perf_counter()
    durasi_list = waktu_selesai - waktu_mulai

    print("\nPython List:")
    mahasiswa_list.info()
    print("Waktu akses:", durasi_list, "detik")

    waktu_mulai = time.perf_counter()
    mahasiswa_linked_list = linked_list_mahasiswa.at(index_uji)
    waktu_selesai = time.perf_counter()
    durasi_linked_list = waktu_selesai - waktu_mulai

    print("\nLinked List:")
    mahasiswa_linked_list.info()
    print("Waktu akses:", durasi_linked_list, "detik")

    print("\n=== KESIMPULAN OPERASI ===")
    print("Python List : akses index langsung -> O(1)")
    print("Linked List : harus menelusuri node -> O(n)")


if __name__ == "__main__":
    main()
