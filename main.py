# Tubes Daspro
# Cara ngerun tulis
# python main.py <folder yg ada datanya misalnya folder test>
# Bahan csv cuman contoh kalau mau diubah juga gapapa isinya asal sesuai template

# Import module dan file commands
import os
# import sys
# import math
import time
import argparse
# import datetime
import commands

# Matriks database
user = [None for _ in range(1000)]
candi = [None for _ in range(1000)]
bahan_bangunan = [None for _ in range(5)]


# Fungsi - fungsi (jangan diapa2in)

# Masukin data csv ke matriks


def getData(matriks, fileName):
    with open(f"save/{args.folder}/{fileName}.csv", "r") as file:
        contents = file.read()
    # Tipe data "contents" itu string jadi boleh pake len
    contents += "\n"
    total = 0
    for i in range(len(contents)):
        if contents[i] == '\n':
            total += 1
    kata = ""
    j = 0
    temp = [None for _ in range(total)]
    for i in range(len(contents)):
        if contents[i] == '\n':
            temp[j] = kata
            kata = ""
            j += 1
        else:
            kata += contents[i]
    for i in range(total):
        if temp[i] != '':
            matriks[i] = splits(temp[i], fileName)

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


parser = argparse.ArgumentParser(description="")
parser.add_argument("folder", type=str)
args = parser.parse_args()
if os.path.exists(f"save/{args.folder}"):
    print("Loading...")
    time.sleep(0.5)
    print("Selamat datang di program \"Manajerial Candi\"\nSilahkan lakukan login")
    # Semua data csv ada di matriks user, candi, bahan_bangunan atau getData("nama matriks"). Tinggal dipakai
    getData(user, "user")
    getData(candi, "candi")
    getData(bahan_bangunan, "bahan_bangunan")
    for i in range(1, 4):
        bahan_bangunan[i][2] = int(bahan_bangunan[i][2])
    for i in range(1, banyakData(candi)):
        candi[i][2] = int(candi[i][2])
        candi[i][3] = int(candi[i][3])
        candi[i][4] = int(candi[i][4])
    sesi = []
    while True:
        masukan = input(">>> ")
        # F-01
        if masukan == "login":
            if sesi == []:
                sesi = commands.login(aksesData(user), banyakData(user))
            else:
                print("Login gagal!")
                print(
                    f"Anda telah login dengan username {sesi[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        # F-02
        elif masukan == "logout":
            if sesi == []:
                print("Logout gagal!")
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
            else:
                print("Logout berhasil")
                sesi = []
        # F-03
        elif masukan == "summonjin":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan summonjin")
            elif sesi[1] == "bandung_bondowoso":
                if (banyakData(user) - 3) >= 100:
                    print(
                        "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
                else:
                    user = commands.summonjin(user, banyakData(user))
            else:
                print("Anda tidak mempunyai akses")
        # F-04
        elif masukan == "hapusjin":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan hapusjin")
            elif sesi[1] == "bandung_bondowoso":
                user, candi = commands.hapusjin(
                    user, banyakData(user), candi, banyakData(candi))
            else:
                print("Anda tidak mempunyai akses")
        # F-05
        elif masukan == "ubahjin":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan ubahjin")
            elif sesi[1] == "bandung_bondowoso":
                user = commands.ubahjin(user, banyakData(user))
            else:
                print("Anda tidak mempunyai akses")
        # F-06
        elif masukan == "bangun":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan bangun")
            elif sesi[1] == "pembangun":
                candi = commands.bangun(
                    candi, bahan_bangunan, banyakData(candi), sesi[0])
            else:
                print("Anda tidak mempunyai akses")
        # F-07
        elif masukan == "kumpul":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan kumpul")
            elif sesi[1] == "pengumpul":
                bahan_bangunan = commands.kumpul(bahan_bangunan)
            else:
                print("Anda tidak mempunyai akses")

        # @Jebe kurang ini
        # F-08
        # F-09

        # F-10
        elif masukan == "laporancandi":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan laporancandi")
            elif sesi[1] == "bandung_bondowoso":
                commands.laporanCandi(candi, banyakData(candi))
            else:
                print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso")
        # F-11
        elif masukan == "hancurkancandi":
            if sesi == []:
                print(
                    "Anda belum login, silahkan login terlebih dahulu sebelum melakukan hancurkancandi")
            elif sesi[1] == "roro_jonggrang":
                candi = commands.hancurkanCandi(candi, banyakData(candi))
            else:
                print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang")
        # F-12
        elif masukan == "ayamberkokok":
            commands.ayamberkokok(banyakData(candi) - 1)
        # F-14
        elif masukan == "save":
            commands.save(aksesData(user), banyakData(user), aksesData(
                candi), banyakData(candi), aksesData(bahan_bangunan), banyakData(bahan_bangunan))
        # F-15
        elif masukan == "help":
            if sesi == []:
                commands.bantuan("")
            else:
                commands.bantuan(sesi[1])
        # F-16
        elif masukan == "exit":
            commands.exitProgram(aksesData(user), banyakData(user), aksesData(
                candi), banyakData(candi), aksesData(bahan_bangunan), banyakData(bahan_bangunan))
        else:
            print("""Command tidak ditemukan
Masukkan command “help” untuk daftar command yang dapat kamu panggil.""")
            continue
else:
    print(f"Folder “{args.folder}” tidak ditemukan")
    exit()
