import time

from src.models.linked_list import LinkedList


def main():
    linked_list = LinkedList()

    print("=== ADD DATA ===")
    waktu_mulai = time.perf_counter()
    linked_list.add_first("Ahmad")
    linked_list.add_last("Budi")
    linked_list.add_last("Citra")
    linked_list.add_at(1, "Dewi")
    waktu_selesai = time.perf_counter()
    linked_list.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu:", durasi, "detik")

    print("\n=== FIND DATA ===")
    data_cari = "Citra"
    waktu_mulai = time.perf_counter()
    index = linked_list.find(data_cari)
    waktu_selesai = time.perf_counter()
    print("Data", data_cari, "berada pada index:", index)
    durasi = waktu_selesai - waktu_mulai
    print("Waktu:", durasi, "detik")

    print("\n=== REMOVE DATA ===")
    waktu_mulai = time.perf_counter()
    print("Hapus pertama:", linked_list.remove_first())
    waktu_selesai = time.perf_counter()
    linked_list.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu:", durasi, "detik")

    waktu_mulai = time.perf_counter()
    print("Hapus terakhir:", linked_list.remove_last())
    waktu_selesai = time.perf_counter()
    linked_list.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu:", durasi, "detik")

    waktu_mulai = time.perf_counter()
    print("Hapus index 1:", linked_list.remove_at(1))
    waktu_selesai = time.perf_counter()
    linked_list.display()
    durasi = waktu_selesai - waktu_mulai
    print("Waktu:", durasi, "detik")


if __name__ == "__main__":
    main()
