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
    with open(f"./save/{args.folder}/{fileName}.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        i = 0
        for lines in file:
            if i == 0:
                temp = lines
            else:
                matriks[i - 1] = splits((lines)[0], fileName)
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
# Misal kalau print(user) bakal keluar [['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang']]
# Kalau print(aksesData(user) [['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggrang'], None, None, None, None,


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
if os.path.exists(f"./save/{args.folder}"):
    print("Loading...")
    time.sleep(0.5)
    print("Selamat datang di program \"Manajerial Candi\"\nSilahkan masukkan username Anda")
    while True:
        masukan = input(">>> ")
        getData(user, "user")
        getData(candi, "candi")
        getData(bahan_bangunan, "bahan_bangunan")
        # Semua data csv ada di matriks user, candi, bahan_bangunan. Tinggal dipakai
        if masukan == "login":
            commands.login()
        # elif masukan == "fungsi kalian"
            # commands.fungsi kalian jangan lupa tambahin ()
            # tulis fungsi kalian di file commands.py, kalau perlu parameter tinggal akses yang ada
        else:
            # print()
            continue
else:
    print(f"Folder “{args.folder}” tidak ditemukan")
    exit()
