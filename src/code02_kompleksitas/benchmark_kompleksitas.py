import time
from collections import deque

from src.models.hash_table import HashTable


def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data[tengah] == target:
            return tengah
        if data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1


def waktu_rata_rata_ns(fungsi, pengulangan):
    waktu_mulai = time.perf_counter_ns()
    for _ in range(pengulangan):
        fungsi()
    waktu_selesai = time.perf_counter_ns()
    return (waktu_selesai - waktu_mulai) / pengulangan


def benchmark_search():
    print("=== BENCHMARK PENCARIAN NIM ===")
    print("Target dibuat sebagai elemen terakhir agar linear search mendekati worst case.")
    print(f"{'n':>7} | {'Linear (us)':>14} | {'Binary (us)':>14} | {'Hash (us)':>12}")
    print("-" * 57)

    for n in [1000, 5000, 10000, 20000]:
        data = list(range(1, n + 1))
        target = n

        hash_table = HashTable()
        for value in data:
            hash_table.put(value, value)

        pengulangan = 200

        linear_ns = waktu_rata_rata_ns(
            lambda: linear_search(data, target), pengulangan
        )
        binary_ns = waktu_rata_rata_ns(
            lambda: binary_search(data, target), pengulangan
        )
        hash_ns = waktu_rata_rata_ns(
            lambda: hash_table.get(target), pengulangan
        )

        print(
            f"{n:7d} | {linear_ns / 1000:14.3f} | "
            f"{binary_ns / 1000:14.3f} | {hash_ns / 1000:12.3f}"
        )


def benchmark_queue():
    print("\n=== BENCHMARK DEQUEUE ===")
    print("Pengukuran dilakukan pada operasi dequeue/popleft.")
    print(f"{'n':>7} | {'list.pop(0) us':>16} | {'deque.popleft us':>18}")
    print("-" * 50)

    for n in [1000, 5000, 10000, 20000]:
        jumlah_operasi = min(100, n)
        data_list = list(range(n))
        data_deque = deque(range(n))

        list_ns = waktu_rata_rata_ns(
            lambda: data_list.pop(0), jumlah_operasi
        )

        deque_ns = waktu_rata_rata_ns(
            lambda: data_deque.popleft(), jumlah_operasi
        )

        print(
            f"{n:7d} | {list_ns / 1000:16.3f} | "
            f"{deque_ns / 1000:18.3f}"
        )


def main():
    benchmark_search()
    benchmark_queue()


if __name__ == "__main__":
    main()
