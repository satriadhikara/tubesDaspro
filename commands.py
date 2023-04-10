import os
import csv
from random import randint


def bangun(candi, bahan_bangunan, banyakDataCandi, user):
    cukup = 0
    pasir = randint(1, 5)
    batu = randint(1, 5)
    air = randint(1, 5)
    if bahan_bangunan[1][2] >= pasir:
        cukup += 1
    if bahan_bangunan[2][2] >= batu:
        cukup += 1
    if bahan_bangunan[3][2] >= air:
        cukup += 1
    if cukup == 3:
        jumlah = 100 - (banyakDataCandi - 1)
        if jumlah != 0:
            jumlah -= 1
            candi[banyakDataCandi] = [banyakDataCandi, user, pasir, batu, air]
            bahan_bangunan[1][2] -= pasir
            bahan_bangunan[2][2] -= batu
            bahan_bangunan[3][2] -= air
        print("Candi berhasil dibangun")
        print(f"Sisa candi yang perlu dibangun: {jumlah}.")
        return candi
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")


def kumpul(bahan_bangunan):
    pasir = randint(0, 5)
    batu = randint(0, 5)
    air = randint(0, 5)
    bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] += air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return bahan_bangunan


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

# F03


def summonjin(user, banyakData):
    # Input Jenis Jin
    print("Jenis jin yang dapat dipanggil:")
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - bertugas membangun candi")
    jj = int(input("Masukan nomor jenis jin yang dipanggil: "))

    if jj == 1:
        print('Memilih jin "Pengumpul".')
        # Input username jin pengumpul dan password
        username = input("Masukan username jin: ")
        cek = False
        for i in range(banyakData):
            if user[i][0] != username:
                cek = True
            else:
                cek = False

        if cek == True:
            password = input("Masukan password jin: ")
            i = 0
            if len(password) >= 5 and len(password) <= 25:
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
            print("Username sudah digunakan.")
            return user

    elif jj == 2:
        print('Memilih jin "Pembangun". ')
        # Input username Jin Pembangun dan password
        username = input("Masukan username jin: ")
        cek = False
        for i in range(banyakData):
            if user[i][0] != username:
                cek = True
            else:
                cek = False

        if cek == True:
            password = input("Masukan password jin: ")
            i = 0
            if len(password) >= 5 and len(password) <= 25:
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
            print("Username sudah digunakan.")
            return user
    else:
        # Diluar jenis jin
        print("Tidak ada jenis jin bernomor", "'" + str(jj) + "'")
        return user

# F04


def hapusjin(user, banyakData):
    username = input("Masukan username jin : ")
    validasi = input(
        f"Apakah anda yakin ingin menghapus jin dengan username {username}, (Y/N)? ")
    if validasi == 'Y':
        for i in range(banyakData):
            if user[i][0] == username:
                user[i] = None
                print("Jin telah berhasil dihapus dari alam gaib.")
                return user
        else:
            print("Tidak ada jin dengan username tersebut.")
            return user
    else:
        print("Jin tetap berada di alam gaib.")
        return user

# F05


def ubahjin(user, banyakData):
    username = input("Masukan username jin : ")
    for i in range(banyakData):
        if user[i][0] == username:
            if user[i][2] == "1":
                validasi = input(
                    "Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
                if validasi == "Y":
                    user[i][2] = 2
                    print("Jin telah berhasil diubah.")
                    return user
                else:
                    user[i][2] = user[i][2]
                    return user
            elif user[i][2] == "2":
                validasi = input(
                    "Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
                if validasi == "Y":
                    user[i][2] = 1
                    print("Jin telah berhasil diubah.")
                    return user
                else:
                    user[i][2] = user[i][2]
                    return user
    else:
        print("Tidak ada jin dengan username tersebut.")
        return user


def login(user, banyakData):
    Username = str(input("Username: "))
    Password = str(input("Password: "))

    for i in range(banyakData):
        if Username == user[i][0]:
            if Password == user[i][1]:
                print(f"Selamat datang {Username}!")
                print(
                    "Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return [Username, user[i][2]]
            else:
                print("Password salah!")
                return []
    print("Username tidak terdaftar!")
    return []


def exitProgram(user, candi, bahan_bangunan):
    while True:
        prompt = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if prompt == 'y':
            save(user, candi, bahan_bangunan)
        exit()
