# Tubes Daspro

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
user = [[None for i in range(3)] for j in range(1000)]
candi = [[None for i in range(4)] for j in range(1000)]
bahan_bangunan = [[None for i in range(3)] for j in range(1000)]


# Fungsi - fungsi

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

# Fungsi akses data yang ada (bukan None)


def aksesData(matriks):
    matriksBaru = [None for _ in range(banyakData(matriks))]
    for i in range(banyakData(matriks)):
        matriksBaru[i] = matriks[i]
    return matriksBaru


def banyakData(matriks):
    i = 0
    while matriks[i][0] != None:
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
        if masukan == "login":
            commands.login()
else:
    print(f"Folder “{args.folder}” tidak ditemukan")
    exit()
