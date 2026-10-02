from src.services.akademik_service import AkademikService


def main():
    service = AkademikService("data/data_mahasiswa_dummy.csv")

    while True:
        print("\n========================================")
        print("         SISTEM AKADEMIK MAHASISWA")
        print("========================================")
        print("1. Tampilkan data mahasiswa")
        print("2. Tambah mahasiswa")
        print("3. Undo operasi terakhir")
        print("4. Tambah mahasiswa ke antrean")
        print("5. Proses antrean")
        print("6. Cari mahasiswa berdasarkan NIM")
        print("7. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            service.tampilkan_mahasiswa()
        elif pilihan == "2":
            service.tambah_mahasiswa_dari_input()
        elif pilihan == "3":
            service.undo()
        elif pilihan == "4":
            service.tambah_ke_antrean_dari_input()
        elif pilihan == "5":
            service.proses_antrean()
        elif pilihan == "6":
            service.cari_mahasiswa_dari_input()
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
