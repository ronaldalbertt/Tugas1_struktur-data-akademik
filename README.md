# Sistem Akademik Mahasiswa - Struktur Data

Program ini dibuat untuk studi kasus sistem akademik mahasiswa dan latihan struktur data linear.

## Struktur Data yang Digunakan

1. **Array/List**
    - Menyimpan data mahasiswa secara berurutan.
    - Akses berdasarkan indeks secara langsung.
    - Implementasi: `src/models/array.py`.

2. **Linked List**
    - Menyimpan data dalam node yang saling terhubung.
    - Cocok untuk pembahasan penyisipan dan penghapusan dinamis.
    - Implementasi: `src/models/linked_list.py`.

3. **Stack**
    - Digunakan untuk fitur Undo.
    - Prinsip: LIFO (Last In First Out).
    - Operasi utama: `push` dan `pop` O(1).
    - Implementasi: `src/models/stack.py`.

4. **Queue**
    - Digunakan untuk antrean pengolahan mahasiswa.
    - Prinsip: FIFO (First In First Out).
    - Implementasi menggunakan `collections.deque` sehingga `enqueue` dan `dequeue` O(1).
    - Implementasi: `src/models/queue.py`.

5. **Hash Table**
    - Digunakan untuk pencarian mahasiswa berdasarkan key NIM.
    - Operasi `get`, `put`, `contains`, dan `remove` rata-rata O(1); worst case dapat O(n).
    - Implementasi sederhana berbasis `dict` Python pada `src/models/hash_table.py`.

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
│   ├── code02_kompleksitas/
│   │   └── benchmark_kompleksitas.py
│   ├── models/
│   │   ├── array.py
│   │   ├── hash_table.py
│   │   ├── linked_list.py
│   │   ├── linked_list_node.py
│   │   ├── mahasiswa.py
│   │   ├── queue.py
│   │   └── stack.py
│   └── services/
│       ├── akademik_service.py
│       └── mahasiswa_reader.py
├── .gitignore
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

## Menjalankan Benchmark Kompleksitas

```bash
python -m src.code02_kompleksitas.benchmark_kompleksitas
```

Benchmark membandingkan:

- Linear search pada data tidak terurut: O(n) worst case.
- Binary search pada data terurut: O(log n) worst case.
- Hash Table lookup: O(1) rata-rata, O(n) worst case.
- `list.pop(0)` dibandingkan dengan `deque.popleft()` untuk dequeue.

Angka waktu benchmark adalah hasil eksperimen pada komputer saat program dijalankan. Angka tersebut dapat berubah karena perangkat dan kondisi sistem, sehingga digunakan sebagai bukti percobaan, bukan sebagai pengganti analisis Big-O

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
