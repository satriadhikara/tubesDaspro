# Commands
import os
from random import randint

# F-01


def login(user, banyakData):
    username = str(input("Username: "))
    password = str(input("Password: "))

    for i in range(banyakData):
        if username == user[i][0]:
            if password == user[i][1]:
                print(f"Selamat datang {username}!")
                print(
                    "Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return [username, user[i][2]]
            else:
                print("Password salah!")
                return []
    print("Username tidak terdaftar!")
    return []

# F03


def summonJin(user, banyakData):
    # Input Jenis Jin
    print("Jenis jin yang dapat dipanggil:")
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - bertugas membangun candi")
    jj = input("Masukan nomor jenis jin yang dipanggil: ")

    if jj == '1':
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
                        print("Jin {username} berhasil dipanggil!")
                        return user
            else:
                print("Password panjangnya harus 5-25 karakter!")
                return user
        else:
            print("Username sudah digunakan.")
            return user
    elif jj == '2':
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
                return user
        else:
            print("Username sudah digunakan.")
            return user
    else:
        # Diluar jenis jin
        print(f"Tidak ada jenis jin bernomor '{jj}'")
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


def hapusJin(user, banyakDataUser, candi, banyakDataCandi):
    username = input("Masukan username jin : ")
    while True:
        validasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username}, (Y/N)? ")
        if validasi == 'Y' or validasi == 'y':
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
        elif validasi == 'N' or validasi == 'n':
            print("Jin tetap berada di alam gaib.")
            return (user, candi)

# F05


def ubahJin(user, banyakData):
    username = input("Masukan username jin : ")
    for i in range(banyakData):
        if user[i][0] == username:
            if user[i][2] == "pengumpul":
                while True:
                    validasi = input(
                        "Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
                    if validasi == "Y" or validasi == 'y':
                        user[i][2] = "pembangun"
                        print("Jin telah berhasil diubah.")
                        return user
                    elif validasi == "N" or validasi == 'n':
                        user[i][2] = user[i][2]
                        return user
            elif user[i][2] == "pembangun":
                while True:
                    validasi = input(
                        "Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
                    if validasi == "Y" or validasi == 'y':
                        user[i][2] = "pengumpul"
                        print("Jin telah berhasil diubah.")
                        return user
                    elif validasi == "N" or validasi == 'n':
                        user[i][2] = user[i][2]
                        return user
    else:
        print("Tidak ada jin dengan username tersebut.")
        return user

# F-06


def bangun(candi, bahan_bangunan, banyakDataCandi, username):
    cukup = 0
    pasir = randNumber(1,5)
    batu = randNumber(1,5)
    air = randNumber(1,5)
    maks = 0
    for i in range(1, banyakDataCandi):
        if maks < int(candi[i][0]):
            maks = int(candi[i][0])
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
            candi[banyakDataCandi] = [maks + 1, username, pasir, batu, air]
            bahan_bangunan[1][2] -= pasir
            bahan_bangunan[2][2] -= batu
            bahan_bangunan[3][2] -= air
        print("Candi berhasil dibangun")
        print(f"Sisa candi yang perlu dibangun: {jumlah}.")
        return candi, bahan_bangunan
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
        return candi, bahan_bangunan

# F-07


def kumpul(bahan_bangunan):
    pasir = randNumber(0,5)
    batu = randNumber(0,5)
    air = randNumber(0,5)
    bahan_bangunan[1][2] += pasir
    bahan_bangunan[2][2] += batu
    bahan_bangunan[3][2] += air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return bahan_bangunan

# F-08


# batch kumpul
def batchKumpul(user, banyakData, bahan_bangunan):
    banyakJin = 0
    for i in range(banyakData):
        if user[i][2] == "pengumpul":
            banyakJin += 1

    if banyakJin != 0:
        jumlahPasir = 0
        jumlahBatu = 0
        jumlahAir = 0
        j = 0
        while j <= banyakJin:
            pasir = randNumber(0,5)
            batu = randNumber(0,5)
            air = randNumber(0,5)
            jumlahPasir += pasir
            jumlahBatu += batu
            jumlahAir += air
            j += 1
        print(f"Mengerahkan {banyakJin} jin untuk mengumpulkan bahan.")
        print(
            f"Jin menemukan total {jumlahPasir} pasir , {jumlahBatu} batu , dan {jumlahAir} air.")
        bahan_bangunan[1][2] += jumlahPasir
        bahan_bangunan[2][2] += jumlahBatu
        bahan_bangunan[3][2] += jumlahAir
        return bahan_bangunan

    else:
        print(
            "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

# batch bangun


def batchBangun(user, banyakDataUser, bahan_bangunan, candi, banyakDataCandi):
    banyakJin = 0
    for i in range(banyakDataUser):
        if user[i][2] == "pembangun":
            banyakJin += 1
    print(banyakJin)
    jin = [None for _ in range(banyakJin)]
    for i in range(banyakJin):
        if user[i + 3][2] == "pembangun":
            jin[i] = user[3 + i][0]
    candiBaru = [None for _ in range(banyakJin)]
    if banyakJin != 0:
        jumlahPasir = 0
        jumlahBatu = 0
        jumlahAir = 0
        for i in range(banyakJin):
            pasir = randNumber(1,5)
            batu = randNumber(1,5)
            air = randNumber(1,5)
            jumlahPasir += pasir
            jumlahBatu += batu
            jumlahAir += air
            candiBaru[i] = [pasir, batu, air]
        cukup = 0
        if bahan_bangunan[1][2] >= jumlahPasir:
            cukup += 1
        if bahan_bangunan[2][2] >= jumlahBatu:
            cukup += 1
        if bahan_bangunan[3][2] >= jumlahAir:
            cukup += 1
        if cukup == 3:
            jumlah = 100 - (banyakDataCandi - 1) - banyakJin
            maks = 0
            for i in range(1, banyakDataCandi):
                if maks < candi[i][0]:
                    maks = candi[i][0]
            for i in range(banyakJin):
                candi[banyakDataCandi + i] = [maks + 1 + i, jin[i],
                                              candiBaru[i][0], candiBaru[i][1], candiBaru[i][2]]
            print(
                f"Mengerahkan {banyakJin} jin untuk membangun candi dengan total bahan {jumlahPasir} pasir, {jumlahBatu} batu, dan {jumlahAir} air.")
            print(f"Jin berhasil membangun total {banyakJin} candi.")
            bahan_bangunan[1][2] -= jumlahPasir
            bahan_bangunan[2][2] -= jumlahBatu
            bahan_bangunan[3][2] -= jumlahAir
            return (candi, bahan_bangunan)
        else:
            print(
                f"Mengerahkan {banyakJin} jin untuk membangun candi dengan total bahan {jumlahPasir} pasir, {jumlahBatu} batu, dan {jumlahAir} air.")
            kurangPasir = jumlahPasir - bahan_bangunan[1][2]
            kurangBatu = jumlahBatu - bahan_bangunan[2][2]
            kurangAir = jumlahAir - bahan_bangunan[3][2]
            if kurangPasir <= 0 and kurangBatu <= 0:
                print(f"Bangun gagal. Kurang {kurangAir} air.")
            elif kurangPasir <= 0 and kurangAir <= 0:
                print(f"Bangun gagal. Kurang {kurangBatu} batu.")
            elif kurangBatu <= 0 and kurangAir <= 0:
                print(f"Bangun gagal. Kurang {kurangPasir} pasir.")
            elif kurangPasir <= 0:
                print(
                    f"Bangun gagal. Kurang {kurangBatu} batu , dan {kurangAir} air.")
            elif kurangBatu <= 0:
                print(
                    f"Bangun gagal. Kurang {kurangPasir} pasir , dan {kurangAir} air.")
            elif kurangAir <= 0:
                print(
                    f"Bangun gagal. Kurang {kurangPasir} pasir , dan {kurangBatu} batu.")
            else:
                print(
                    f"Bangun gagal. Kurang {kurangPasir} pasir , {kurangBatu} batu , dan {kurangAir} air.")
    else:
        print(
            "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

# F-09


def laporanJin(user, banyakDataUser, banyakDataCandi, candi, bahan_bangunan):
    total = 0
    totalPengumpul = 0
    totalPembangun = 0
    for i in range(banyakDataUser):
        if user[i][2] == "pengumpul":
            totalPengumpul += 1
        elif user[i][2] == "pembangun":
            totalPembangun += 1
    total = totalPembangun + totalPengumpul

    ada = False
    banyak = [0 for _ in range(banyakDataUser)]
    for i in range(1, banyakDataCandi):
        for j in range(banyakDataUser):
            if candi[i][1] == user[j][0]:
                indeksUser = j
                break
        banyak[indeksUser] += 1
        ada = True
    maks = min = banyak[3]
    maksJin = minJin = user[3][0]
    for i in range(3, banyakDataUser):
        if banyak[i] > maks:
            maks = banyak[i]
            maksJin = user[i][0]
        if banyak[i] < min:
            min = banyak[i]
            minJin = user[i][0]

    print(f"Total Jin: {total}")
    print(f"Total Jin Pengumpul: {totalPengumpul}")
    print(f"Total Jin Pembangun: {totalPembangun}")
    if ada == True:
        print(f"Jin Terajin: {maksJin}")
        print(f"Jin Termalas: {minJin}")
    else:
        print("Jin Terajin: -")
        print("Jin Termalas: -")
    print(f"Jumlah Pasir: {bahan_bangunan[1][2]} unit")
    print(f"Jumlah Batu: {bahan_bangunan[2][2]} unit")
    print(f"Jumlah Air: {bahan_bangunan[3][2]} unit")

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


def ayamBerkokok(totalcandi):
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
            if i != banyakDataUser - 1:
                file.write("\n")
    with open(f'{path}/candi.csv', 'w', newline='') as file:
        for i in range(banyakDataCandi):
            for j in range(5):
                file.write(str(candi[i][j]))
                if j != 4:
                    file.write(";")
            if i != banyakDataCandi - 1:
                file.write("\n")
    with open(f'{path}/bahan_bangunan.csv', 'w', newline='') as file:
        for i in range(banyakDataBahan):
            for j in range(3):
                file.write(str(bahan_bangunan[i][j]))
                if j != 2:
                    file.write(";")
            if i != banyakDataBahan - 1:
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
   Untuk menyimpan data permainan
10. exit
   Untuk keluar dari permainan""")

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
   Untuk menyimpan data permainan
5. exit
   Untuk keluar dari permainan""")

    elif akun == "pengumpul":
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi
3. save
   Untuk menyimpan data permainan
4. exit
   Untuk keluar dari permainan""")

    elif akun == "pembangun":
        print(f"""
=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi
3. save
   Untuk menyimpan data permainan
4. exit
   Untuk keluar dari permainan""")

    else:  # Pemain belum login
        print(f"""
=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. load
   Untuk memuat file eksternal ke dalam permainan
3. save
   Untuk menyimpan data permainan
4. exit
   Untuk keluar dari permainan""")

# F-16


def exitProgram(user, banyakDataUser, candi, banyakDataCandi, bahan_bangunan, banyakDataBahan):
    while True:
        prompt = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if prompt == 'y' or prompt == 'Y':
            save(user, banyakDataUser, candi, banyakDataCandi,
                 bahan_bangunan, banyakDataBahan)
            exit()
        elif prompt == 'n' or prompt == 'N':
            exit()


# B-01


def lcg(seed: int = 177013, a: int = 1103515245, c: int = 12345, m: int = 2**31):      
# Kalo 'seed' terserah (JoJo ending true ending) 'a', 'c', 'm' tersebut banyak digunakan karena panjang setiap periode dari loop yang sangat panjang                                                                        
    while True:
        seed = (a * seed + c) % m  
        yield seed / m
# Membuat generator yang memuat nilai 0 sampai 1 dalam float sehingga menggunakan 'yield'

def rounding(x: float):                                     
# Karena generator float dan jika diubah menjadi integer terjadi floor division
# Fungsinya agar nanti bilangan float dibulatkan ke bilangan bulat terdekat
    temp = int(x)
    if x % 1 < 0.5:
        return temp
    else:
        return temp + 1
    
def randNumber(minimum: int, maximum: int):
# randint dengan nilai minimum dan maximum
    return rounding(next(generator) * (maximum - minimum) + minimum)

generator = lcg()


# B-05


def gantiPassword(user, banyakData):
    username = input("Username: ")
    password = input("Password: ")

    for i in range(banyakData):
        if username == user[i][0]:
            if password == user[i][1]:
                validasi = input(
                    "Apakah anda ingin mengganti password ? (Y/N): ")
                if validasi == "Y":
                    newPass = input("Masukan password baru: ")
                    user[i][1] = newPass
                    user[i][0] = user[i][0]
                    print(f"Password berhasil diubah")
                    return user
                else:
                    print("Password tidak diubah")
            else:
                print("Password salah")
    else:
        print("Username tidak ditemukan")
