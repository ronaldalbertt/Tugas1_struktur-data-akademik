# Sistem Akademik Mahasiswa - Struktur Data

Program ini dibuat untuk studi kasus sistem akademik mahasiswa dan latihan struktur data linear.

## Struktur Data yang Digunakan

1. **Array/List**
   - Menyimpan data mahasiswa secara berurutan.
   - Implementasi pada `src/models/array.py`.

2. **Linked List**
   - Menyimpan data dalam node yang saling terhubung.
   - Implementasi pada `src/models/linked_list.py` dan `src/models/linked_list_node.py`.

3. **Stack**
   - Digunakan untuk fitur Undo.
   - Prinsip: LIFO.
   - Implementasi pada `src/models/stack.py`.

4. **Queue**
   - Digunakan untuk antrean pengolahan mahasiswa.
   - Prinsip: FIFO.
   - Implementasi pada `src/models/queue.py`.

## Struktur Folder

```text
struktur-data-akademik/
├── main.py
├── data/
│   ├── data_mahasiswa_dummy.csv
│   └── data_mahasiswa_dummy_200.csv
├── src/
│   ├── code01_linear_sd/
│   │   ├── main_array.py
│   │   ├── main_linked_list.py
│   │   └── main_list.py
│   ├── models/
│   │   ├── array.py
│   │   ├── linked_list.py
│   │   ├── linked_list_node.py
│   │   ├── mahasiswa.py
│   │   ├── queue.py
│   │   └── stack.py
│   └── services/
│       ├── akademik_service.py
│       └── mahasiswa_reader.py
├── requirements.txt
└── README.md
```

## Menjalankan Program Utama

Dari folder `struktur-data-akademik`:

```bash
python main.py
```

## Menjalankan Latihan Linear Structure

```bash
python -m src.code01_linear_sd.main_array
python -m src.code01_linear_sd.main_linked_list
python -m src.code01_linear_sd.main_list
```

### Fungsi masing-masing file

- `main_array.py`: contoh operasi add, find, dan remove pada struktur Array.
- `main_linked_list.py`: contoh operasi add, find, dan remove pada Linked List.
- `main_list.py`: membandingkan akses berdasarkan index pada Python List dan Linked List menggunakan data dummy 200 mahasiswa.

Program menggunakan `time.perf_counter()` untuk memperlihatkan waktu eksekusi. Waktu tersebut hanya sebagai hasil percobaan pada komputer saat program dijalankan; analisis kompleksitas tetap mengacu pada pertumbuhan operasi terhadap ukuran input.

## Menu Program Utama

1. Tampilkan data mahasiswa
2. Tambah mahasiswa
3. Undo operasi terakhir
4. Tambah mahasiswa ke antrean
5. Proses antrean
6. Cari mahasiswa berdasarkan NIM
7. Keluar
