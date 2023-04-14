# Commands
import os
import csv
from random import randint

# F-01


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
                        user[i] = [username, password, "pengumpul"]
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
                        user[i] = [username, password, "pembangun"]
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


def hapusCandi(username, candi, banyakData):
    for i in range(banyakData):
        if candi[i][1] == username:
            if i == (banyakData - 1):
                candi[i] = None
            elif i != (banyakData - 1):
                for j in range(i, banyakData - 1):
                    candi[j] = candi[j + 1]
                candi[banyakData - 1] = None
            return hapusCandi(username, candi, banyakData - 1)
    else:
        return candi


def hapusjin(user, banyakDataUser, candi, banyakDataCandi):
    username = input("Masukan username jin : ")
    validasi = input(
        f"Apakah anda yakin ingin menghapus jin dengan username {username}, (Y/N)? ")
    if validasi == 'Y':
        for i in range(banyakDataUser):
            if user[i][0] == username:
                candi = hapusCandi(username, candi, banyakDataCandi)
                if i == (banyakDataUser - 1):
                    user[i] = None
                elif i != (banyakDataUser - 1):
                    for j in range(i, banyakDataUser - 1):
                        user[j] = user[j + 1]
                    user[banyakDataUser - 1] = None
                print("Jin telah berhasil dihapus dari alam gaib.")
                return (user, candi)
        else:
            print("Tidak ada jin dengan username tersebut.")
            return (user, candi)
    else:
        print("Jin tetap berada di alam gaib.")
        return (user, candi)

# F05


def ubahjin(user, banyakData):
    username = input("Masukan username jin : ")
    for i in range(banyakData):
        if user[i][0] == username:
            if user[i][2] == "pengumpul":
                validasi = input(
                    "Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
                if validasi == "Y":
                    user[i][2] = "pembangun"
                    print("Jin telah berhasil diubah.")
                    return user
                else:
                    user[i][2] = user[i][2]
                    return user
            elif user[i][2] == "pembangun":
                validasi = input(
                    "Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
                if validasi == "Y":
                    user[i][2] = "pengumpul"
                    print("Jin telah berhasil diubah.")
                    return user
                else:
                    user[i][2] = user[i][2]
                    return user
    else:
        print("Tidak ada jin dengan username tersebut.")
        return user

# F-06


def bangun(candi, bahan_bangunan, banyakDataCandi, user):
    cukup = 0
    pasir = randint(1, 5)
    batu = randint(1, 5)
    air = randint(1, 5)
    maks = 0
    for i in range(1, banyakDataCandi):
        if maks < candi[i][0]:
            maks = candi[i][0]
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
            candi[banyakDataCandi] = [maks + 1, user, pasir, batu, air]
            bahan_bangunan[1][2] -= pasir
            bahan_bangunan[2][2] -= batu
            bahan_bangunan[3][2] -= air
        print("Candi berhasil dibangun")
        print(f"Sisa candi yang perlu dibangun: {jumlah}.")
        return candi
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

# F-07


def kumpul(bahan_bangunan):
    pasir = randint(0, 5)
    batu = randint(0, 5)
    air = randint(0, 5)
    bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] += air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return bahan_bangunan

# F-10


def hargaCandi(candiRow):
    return ((candiRow[2] * 10000) + (candiRow[3] * 15000) + (candiRow[4] * 7500))


def laporanCandi(candi, banyakData):
    totalPasir = 0
    totalBatu = 0
    totalAir = 0
    if banyakData > 1:
        maks = hargaCandi(candi[1])
        min = hargaCandi(candi[1])
        idMaks = 1
        idMin = 1
        for i in range(1, banyakData):
            totalPasir += int(candi[i][2])
            totalBatu += int(candi[i][3])
            totalAir += int(candi[i][4])
            if maks < hargaCandi(candi[i]):
                maks = hargaCandi(candi[i])
                idMaks = i
            if min > hargaCandi(candi[i]):
                min = hargaCandi(candi[i])
                idMin = i
        print(f"Total candi: {banyakData - 1}")
        print(f"Total pasir yang digunakan: {totalPasir}")
        print(f"Total batu yang digunakan: {totalBatu}")
        print(f"Total air yang digunakan: {totalAir}")
        print(f"ID Candi Termahal: {idMaks} (Rp {maks})")
        print(f"ID Candi Termural: {idMin} (Rp {min})")
    else:
        for i in range(1, banyakData):
            totalPasir += int(candi[i][2])
            totalBatu += int(candi[i][3])
            totalAir += int(candi[i][4])
        print(f"Total candi: {banyakData - 1}")
        print(f"Total pasir yang digunakan: {totalPasir}")
        print(f"Total batu yang digunakan: {totalBatu}")
        print(f"Total air yang digunakan: {totalAir}")
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")

# F-11


def hancurkanCandi(candi, banyakData):
    idCandi = int(input("Masukkan ID candi: "))
    for i in range(banyakData):
        if int(candi[i][0]) == idCandi:
            if i == (banyakData - 1):
                candi[i] = None
            elif i != (banyakData - 1):
                for j in range(i, banyakData - 1):
                    candi[j] = candi[j + 1]
                candi[banyakData - 1] = None
    else:
        print("Tidak ada candi dengan ID tersebut")
    return candi


# F12 - Ayam Berkokok


def ayamberkokok(totalcandi):
    print()
    print("Kukuruyuk.. Kukuruyuk..")
    print()
    print("Jumlah candi:", totalcandi)
    if (totalcandi < 100):
        print(f"""
Selamat, Roro Jonggrang memenangkan permainan!

*Bandung Bondowoso angry noise*
Roro Jonggrang dikutuk menjadi candi.""")
        exit()
    else:  # total candi >= 100
        print(f"""
Yah, Bandung Bondowoso memenangkan permainan!""")
        exit()

# F-14


def save(user, banyakDataUser, candi, banyakDataCandi, bahan_bangunan, banyakDataBahan):
    folder = "save/"
    temp = input("Masukkan nama folder: ")
    folder += temp
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
        for i in range(banyakDataUser):
            for j in range(3):
                file.write(str(user[i][j]))
                if j != 2:
                    file.write(";")
            file.write("\n")
    with open(f'{path}/candi.csv', 'w', newline='') as file:
        for i in range(banyakDataCandi):
            for j in range(5):
                file.write(str(candi[i][j]))
                if j != 4:
                    file.write(";")
            file.write("\n")
    with open(f'{path}/bahan_bangunan.csv', 'w', newline='') as file:
        for i in range(banyakDataBahan):
            for j in range(3):
                file.write(str(bahan_bangunan[i][j]))
                if j != 2:
                    file.write(";")
            file.write("\n")
    print(f"Berhasil menyimpan data di folder {path}!")
    return

# F15 - Help


def bantuan(akun):
    if akun == "bandung_bondowoso":
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. summonjin
   Untuk memanggil jin
3. hapusjin
   Untuk menghilangkan jin
4. ubahjin
   Untuk mengubah tipe jin
5. batchkumpul
   Untuk memerintahkan seluruh jin pengumpul mengumpulkan bahan
6. batchbangun
   Untuk memerintahkan seluruh jin pembangun membangun candi
7. laporanjin
   Untuk mengambil laporan kinerja seluruh jin
8. laporancandi
   Untuk mengambil laporan progress pembangunan candi
9. save
   Untuk menyimpan data
10. exit
   Untuk keluar dari permainan""")
        # opsi = int(input("Pilih nomor opsi yang akan dilakukan: "))
        # if (opsi == 1):
        #     logout()
        # elif (opsi == 2):
        #     summonjin()
        # elif (opsi == 3):
        #     hapusjin()
        # elif (opsi == 4):
        #     ubahjin()
        # elif (opsi == 5):
        #     batchkumpul()
        # elif (opsi == 6):
        #     batchbangun()
        # elif (opsi == 7):
        #     laporanjin()
        # elif (opsi == 8):
        #     laporancandi()
        # elif (opsi == 9):
        #     save()
        # elif (opsi == 10):
        #     keluar()
        # else:  # Opsi tidak valid
        #     print("Opsi anda tidak valid")
        #     bantuan()

    elif akun == "roro_jonggrang":
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
3. ayamberkokok
   Untuk menyelesaikan permainan
4. save
   Untuk menyimpan data
5. exit
   Untuk keluar dari permainan""")
        # opsi = int(input("Pilih nomor opsi yang akan dilakukan: "))
        # if (opsi == 1):
        #     logout()
        # elif (opsi == 2):
        #     hancurkancandi()
        # elif (opsi == 3):
        #     ayamberkokok()
        # elif (opsi == 4):
        #     save()
        # elif (opsi == 5):
        #     keluar()
        # else:  # Opsi tidak valid
        #     print("Opsi anda tidak valid")
        #     bantuan()

    elif akun == "pengumpul":
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi
3. exit
   Untuk keluar dari permainan""")
        # opsi = int(input("Pilih nomor opsi yang akan dilakukan: "))
        # if (opsi == 1):
        #     logout()
        # elif (opsi == 2):
        #     kumpul()
        # elif (opsi == 3):
        #     keluar()
        # else:  # Opsi tidak valid
        #     print("Opsi anda tidak valid")
        #     bantuan()

    elif akun == "pembangun":
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi
3. exit
   Untuk keluar dari permainan""")
        # opsi = int(input("Pilih nomor opsi yang akan dilakukan: "))
        # if (opsi == 1):
        #     logout()
        # elif (opsi == 2):
        #     bangun()
        # elif (opsi == 3):
        #     keluar()
        # else:  # Opsi tidak valid
        #     print("Opsi anda tidak valid")
        #     bantuan()

    else:  # Pemain belum login
        print(f"""
=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. load
   Untuk memuat file eksternal ke dalam permainan
3. exit
   Untuk keluar dari permainan""")
        # opsi = int(input("Pilih nomor opsi yang akan dilakukan: "))
        # if (opsi == 1):
        #     login()
        # elif (opsi == 2):
        #     load()
        # elif (opsi == 3):
        #     keluar()
        # else:  # Opsi tidak valid
        #     print("Opsi anda tidak valid")
        #     bantuan()


# F-16


def exitProgram(user, banyakDataUser, candi, banyakDataCandi, bahan_bangunan, banyakDataBahan):
    while True:
        prompt = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if prompt == 'y':
            save(user, banyakDataUser, candi, banyakDataCandi,
                 bahan_bangunan, banyakDataBahan)
        exit()
