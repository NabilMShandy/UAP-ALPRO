import time
from collections import deque
from art import art_2

def Bfs(graf,start):
     queue = deque([start])
     # Set untuk mencatat Tempat di Dungeon yang sudah dikunjungi agar tidak terjadi looping
     visited = {start}

     print(f"{start}", end="")
     counter = 0
     hitung_waktu = 0
     while queue:
         current= queue.popleft()
         if current == "Harta Karun" :
             print("==> DITEMUKAN! <==")
             print(art_2)
             return True

         if current in graf:
             for tetangga in graf[current]:
                 if tetangga not in visited:
                     visited.add(tetangga)
                     queue.append(tetangga)
                     time.sleep(0.5)
                     print(f" ==>> {tetangga}", end="")
                     hitung_waktu+=1
                     counter += 1
                     if counter == 3:
                        print()
                        counter = 0
                        
     print("\n tidak ditemukan!")
     return False

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
    "Air Garam": ["Harta Karun", "Ranjau Mematikan"],
    "Ranjau Mematikan": ["Air Garam"],
    "Harta Karun": [],
}