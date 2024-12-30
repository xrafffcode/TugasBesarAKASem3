import time
import matplotlib.pyplot as plt

# Dataset contoh (diperbesar untuk uji performa)
lowongan_kerja = [{"id": i, "title": f"Job {i}", "location": "Location A", "salary": 10000 + i} for i in range(1, 600)]

# Fungsi Iteratif
def linear_search_iterative(jobs, criteria_key, criteria_value):
    for job in jobs:
        if job[criteria_key] == criteria_value:
            return job
    return None

# Fungsi Rekursif
def linear_search_recursive(jobs, index, criteria_key, criteria_value):
    if index == len(jobs):
        return None
    if jobs[index][criteria_key] == criteria_value:
        return jobs[index]
    return linear_search_recursive(jobs, index + 1, criteria_key, criteria_value)

# Ukuran masukan untuk eksperimen
input_sizes = [10, 100, 1000, 5000, 10000]
iterative_times = []
recursive_times = []

# Eksperimen pengukuran waktu
for size in input_sizes:
    dataset = lowongan_kerja[:size]
    search_key = "id"
    search_value = size  # Cari elemen terakhir

    # Waktu Iteratif
    start = time.time()
    linear_search_iterative(dataset, search_key, search_value)
    end = time.time()
    iterative_times.append(end - start)

    # Waktu Rekursif
    start = time.time()
    linear_search_recursive(dataset, 0, search_key, search_value)
    end = time.time()
    recursive_times.append(end - start)

# Plot hasil eksperimen
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, iterative_times, label="Iteratif", marker='o')
plt.plot(input_sizes, recursive_times, label="Rekursif", marker='s')

plt.title("Perbandingan Running Time Linear Search")
plt.xlabel("Ukuran Masukan (Jumlah Lowongan Kerja)")
plt.ylabel("Waktu Eksekusi (detik)")
plt.legend()
plt.grid(True)
plt.show()
