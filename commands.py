import os
import csv


def login():
    return


def save(user, candi, bahan_bangunan):
    folder = input("Masukkan nama folder: ")
    print("\nSaving...\n")
    folder += "/"
    jumlah = 0
    for i in range(len(folder)):
        if folder[i] == "/":
            jumlah += 1
    i = 0
    batas = 0
    path = ""
    while batas != jumlah:
        if folder[i] != "/":
            path += folder[i]
            i += 1
        else:
            if os.path.exists(path) == False:
                print(f"Membuat folder {path}...")
                os.mkdir(path)
            batas += 1
            path += folder[i]
            i += 1
    with open(f'{path}/user.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user)
    with open(f'{path}/candi.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(candi)
    with open(f'{path}/bahan_bangunan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(bahan_bangunan)
    print(f"Berhasil menyimpan data di folder {path}!")
    return
