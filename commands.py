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
        writer = csv.writer(file, delimiter=";")
        writer.writerows(user)
    with open(f'{path}/candi.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(candi)
    with open(f'{path}/bahan_bangunan.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(bahan_bangunan)
    print(f"Berhasil menyimpan data di folder {path}!")
    return


def summonjin(user):
    # Input Jenis Jin
    print("Jenis jin yang dapat dipanggil:")
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - bertugas membangun candi")
    jj = int(input("Masukan nomor jenis jin yang dipanggil: "))
    if jj == 1:
        print('Memilih jin "Pengumpul".')
        # Input username jin pengumpul dan password
        username = input("Masukan username jin: ")
        password = input("Masukan password jin: ")
        i = 0
        if len(password) > 5 and len(password) < 25:
            while True:
                if user[i] != None:
                    i += 1
                else:
                    user[i] = [username, password, jj]
                    print("Mengumpulkan sesajen...")
                    print("Menyerahkan sesajen...")
                    print("Membacakan mantra...")
                    print()
                    print("Jin", username, "berhasil dipanggil!")
                    return user
        else:
            print("Password panjangnya harus 5-25 karakter!")

    elif jj == 2:
        print('Memilih jin "Pembangun". ')
        # Input username Jin Pembangun dan password
        username = input("Masukan username jin: ")
        password = input("Masukan password jin: ")
        i = 0
        if len(password) > 5 and len(password) < 25:
            while True:
                if user[i] != None:
                    i += 1
                else:
                    user[i] = [username, password, jj]
                    print("Mengumpulkan sesajen...")
                    print("Menyerahkan sesajen...")
                    print("Membacakan mantra...")
                    print()
                    print("Jin", username, "berhasil dipanggil!")
                    return user
        else:
            print("Password panjangnya harus 5-25 karakter!")
    else:
        # Diluar jenis jin
        print("Tidak ada jenis jin bernomor", "'" + str(jj) + "'")
        return user
