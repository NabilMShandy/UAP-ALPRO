import time
import random
from art import art_2
# Penelusuran Depth First Seearch (DFS)
def dfs(graf, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    time.sleep(0.5)
    print(start, end="")
    time.sleep(0.5)
    print(end=" -> ")

    # Fungsi mengembalikan nilai True
    if start == "Harta Karun":
        print("Ditemukan")
        print(art_2)
        return True

    # Karena disini ada pemanggilan rekursif, maka returnnya harus sama yakni True supaya rekursifnya berhenti
    for neighbor in graf[start]:
        if neighbor not in visited:
            if dfs(graf, neighbor, visited):
                return True
            else:
                print("Tidak ditemukan!")
                print(f"Kembali dari {start}")
goa = {
    "Goa Tengkorak": ["Mulut Goa", "Lorong Pertama", "Celah Batu"],
    "Mulut Goa": ["Kawah Hitam", "Lorong Pertama"],
    "Pos Penjaga Depan": ["Mulut Goa", "Kawah Hitam"],
    "Celah Belakang": ["Lorong Pertama"],
    "Kawah Hitam": ["Air Garam", "Gudang Logistik Preman"],
    "Gudang Logistik Preman": ["Kawah Hitam"],
    "Celah Batu": ["Lorong Kedua", "Celah Kristal", "Mulut Goa", "Tanjakan Gypsum"],
    "Celah Kristal": ["Tanjakan Gypsum", "Air Terjun", "Tempat Istirahat Preman"],
    "Tempat Istirahat Preman": ["Celah Kristal"],
    "Lorong Pertama": ["Air Terjun"],
    "Air Terjun": ["Persimpangan 4", "Tanjakan Gypsum", "Ngarai Asam"],
    "Tanjakan Gypsum": ["Celah Kristal", "Puncak Sunyi"],
    "Puncak Sunyi": ["Tanjakan Gypsum"],
    "Ngarai Asam": ["Lorong Ketiga", "Lorong Misterius", "Lorong Monster"],
    "Lorong Monster": ["Kandang Anjing Penjaga"],
    "Kandang Anjing Penjaga": ["Ngarai Asam"],
    "Lorong Misterius": ["Lorong Monster", "Celah Batu", "Ruang Ritual Rahasia"],
    "Ruang Ritual Rahasia": ["Lorong Misterius"],
    "Lorong Kedua": ["Kolam Asam Klorida"],
    "Persimpangan 4": ["Celah Batu", "Kolam Asam Klorida", "Ruang Penyiksaan"],
    "Ruang Penyiksaan": ["Persimpangan 4"],
    "Kolam Asam Klorida": ["Celah Batu", "Dermaga Bawah Tanah"],
    "Dermaga Bawah Tanah": ["Kolam Asam Klorida"],
    "Lorong Ketiga": ["Ngarai Asam", "Mulut Goa"],
    "Air Garam": ["Ranjau Mematikan"],
    "Ranjau Mematikan": ["Air Garam"],
}

harta = "Harta Karun"
node_acak = random.choice(list(goa.keys()))
if harta not in goa:
    if node_acak != "Harta Karun":
        goa[node_acak].append(harta)
        goa[harta] = []