from login_user import start_program, tampilkan_banner
from dfss import dfs, goa
from bfss import Bfs
import time

if __name__ == "__main__":
    while True:
        tampilkan_banner()
        time.sleep(2)
        # start_program()
        
        print("="*50)
        print(f" INVESTIGASI GUA MISTERIUS - USER:")
        print("1. Cari Harta Karun dengan metode DFS (Depth First Search)")
        print("2. Cari Harta Karun dengan metode BFS (Breadth First Search)")
        print("3. Keluar")
        
        pilihan = input("Pilih metode (1/2/3): ").strip()
        
        if pilihan == "1":
            print("\n 🔍 MEMULAI PENELUSURAN DFS 🔍")
            dfs(goa, "Goa Tengkorak")
            
        elif pilihan == "2":
            print("\n 🌿 MEMULAI PENELUSURAN BFS 🌿")
            Bfs(goa, "Goa Tengkorak")
            
        elif pilihan == "3":
            print("Menghentikan program...")
            time.sleep(3)
            break