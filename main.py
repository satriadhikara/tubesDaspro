# Tubes Daspro
# Cara ngerun tulis
# python main.py <folder yg ada datanya misalnya folder test>
# Bahan csv cuman contoh kalau mau diubah juga gapapa isinya asal sesuai template

# Import module dan file commands
import os
import sys
import math
import time
import argparse
import datetime
import commands
import csv

# Matriks database
user = [None for _ in range(1000)]
candi = [None for _ in range(1000)]
bahan_bangunan = [None for _ in range(1000)]


# Fungsi - fungsi (jangan diapa2in)

# Masukin data csv ke matriks


def getData(matriks, fileName):
    with open(f"{args.folder}/{fileName}.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        i = 0
        for lines in file:
            matriks[i] = splits((lines)[0], fileName)
            i += 1


# Fungsi split (cuman buat data)
def splits(baris, fileName):
    baris += ";"
    j = 0
    kata = ""
    if fileName == "candi":
        panjang = 5
    else:
        panjang = 3
    barisBaru = [None for _ in range(panjang)]
    i = 0
    while True:
        if j == panjang:
            break
        elif baris[i] == ";":
            barisBaru[j] = kata
            kata = ""
            j += 1
            i += 1
        else:
            kata += baris[i]
            i += 1
    return barisBaru

# Fungsi akses data yang ada (gaada None-nya)
# Misal kalau print(aksesData(user) bakal keluar [['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang']]
# Kalau print(user) [['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'], None, None, None, None,


def aksesData(matriks):
    matriksBaru = [None for _ in range(banyakData(matriks))]
    for i in range(banyakData(matriks)):
        matriksBaru[i] = matriks[i]
    return matriksBaru

# Fungsi banyaknya data matriks


def banyakData(matriks):
    i = 0
    while matriks[i] != None:
        i += 1
    return i


parser = argparse.ArgumentParser(description="List fish in aquarium.")
parser.add_argument("folder", type=str)
args = parser.parse_args()
if os.path.exists(f"{args.folder}"):
    print("Loading...")
    time.sleep(0.5)
    print("Selamat datang di program \"Manajerial Candi\"\nSilahkan masukkan username Anda")
    # Semua data csv ada di matriks user, candi, bahan_bangunan atau getData("nama matriks"). Tinggal dipakai
    getData(user, "user")
    getData(candi, "candi")
    getData(bahan_bangunan, "bahan_bangunan")
    for i in range(1, 4):
        bahan_bangunan[i][2] = int(bahan_bangunan[i][2])
    sesi = []
    while True:
        masukan = input(">>> ")
        if masukan == "save":
            commands.save(aksesData(user), aksesData(
                candi), aksesData(bahan_bangunan))
        # elif masukan == "fungsi kalian"
            # commands.fungsi kalian jangan lupa tambahin ()
            # tulis fungsi kalian di file commands.py, kalau perlu parameter tinggal akses yang ada
        elif masukan == "summonjin":
            jin = 0
            for i in range(banyakData(user)):
                if jin == 100:
                    print("Jin telah maksimal(100)")
                    break
                else:
                    if str(user[i][2]) == "1" or str(user[i][2]) == "2":
                        jin += 1
            else:
                user = commands.summonjin(user, banyakData(user))
        elif masukan == "hapusjin":
            user = commands.hapusjin(user, banyakData(user))
        elif masukan == "login":
            if sesi == []:
                sesi = commands.login(aksesData(user), banyakData(user))
            else:
                print("Login gagal!")
                print(
                    f"Anda telah login dengan username {sesi[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        elif masukan == "logout":
            if sesi == []:
                print("Logout gagal!")
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
            else:
                print("Logout berhasil")
                sesi = []
        elif masukan == "exit":
            commands.exitProgram(aksesData(user), aksesData(
                candi), aksesData(bahan_bangunan))
        elif masukan == "kumpul":
            bahan_bangunan = commands.kumpul(bahan_bangunan)
        else:
            # print()
            continue
else:
    print(f"Folder “{args.folder}” tidak ditemukan")
    exit()
