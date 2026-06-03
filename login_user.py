import time
import os
from art import art_1
file_user = "users.txt"

def registrasi():
    print("\n === DAFTAR AKUN BARU ===")
    user_baru = input("Buat Username: ")
    pass_baru = input("Buat Password: ")

    with open(file_user, 'a') as  f:
        f.write(f"{user_baru}:{pass_baru}")
    print("Akun berhasil dibuat! Silakan login")

def login():
    if not os.path.exists(file_user):
        print("Belum ada akun, silakan daftar!")
        return False

    print("\n 🏴‍☠️ === LOGIN === 🏴‍☠️")
    user_input = input("Username: ")
    pass_input = input("Pass: ")

    with open(file_user, 'r') as f:
        for baris in f:
            u, p = baris.strip().split(":")
            if user_input == u and pass_input == p:
                print("Login berhasil!")
                print(art_1)
                return True

    print("Username atau password salah!")
    return False

def start_program():
    pilih = input("1. Login\n2. Daftar Akun\nPilih: ")
    if pilih == "1":
        if login():
            time.sleep(3)
            print("Memasuki Program...")
            
            if os.name == 'nt':
                os.system('cls')
    else:
        registrasi()