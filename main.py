# Tubes Daspro
# Cara ngerun tulis:
# python main.py <folder yg ada datanya misalnya folder new>

# Import module dan file commands
import os
import time
import argparse
import commands

# Fungsi - fungsi untuk data

# Masukin data csv ke matriks


def getData(matriks, fileName, path):
    with open(f"{path}/{fileName}.csv", "r") as file:
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


def main():
    # F-13 Load
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("folder", type=str, nargs="?")
    args = parser.parse_args()
    if args.folder == None:
        print("Tidak ada nama folder yang diberikan!\nUsage: python main.py <nama_folder>\n\nNote: Pemain baru silahkan memakai folder \"new\"")
    else:
        if os.path.exists(f"save/{args.folder}"):
            # Matriks database
            user = [None for _ in range(105)]
            candi = [None for _ in range(105)]
            bahan_bangunan = [None for _ in range(5)]
            path = f"save/{args.folder}"
            print("Loading...")
            time.sleep(0.5)
            print(
                "Selamat datang di program \"Manajerial Candi\"\nSilahkan lakukan login")
            # Semua data csv ada di matriks user, candi, bahan_bangunan atau getData("nama matriks").
            getData(user, "user", path)
            getData(candi, "candi", path)
            getData(bahan_bangunan, "bahan_bangunan", path)
            # Ubah tipe data yang angka menjadi integer (soalnya default csv string)
            for i in range(1, 4):
                bahan_bangunan[i][2] = int(bahan_bangunan[i][2])
            for i in range(1, banyakData(candi)):
                candi[i][0] = int(candi[i][0])
                candi[i][2] = int(candi[i][2])
                candi[i][3] = int(candi[i][3])
                candi[i][4] = int(candi[i][4])
            # List sesi ini kosong ketika belom login, dan berisi [username, role] jika sudah login
            sesi = []
            # Loopingan utama program
            while True:
                # Masukan input commands2
                masukan = input(">>> ")
                # F-01
                if masukan == "login":
                    if sesi == []:
                        # Fungsi login ini akan mengupdate list sesi menjadi [username, role] untuk menentukan akses
                        sesi = commands.login(
                            aksesData(user), banyakData(user))
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
                        # Maksimal jin yaitu 100 jadi kita bikin validasinya
                        if (banyakData(user) - 3) >= 100:
                            print(
                                "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
                        else:
                            # Fungsi summonJin ini akan mengupdate matriks user jadi bertambah jin nya
                            user = commands.summonJin(user, banyakData(user))
                    else:
                        print("Anda tidak mempunyai akses")
                # F-04
                elif masukan == "hapusjin":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan hapusjin")
                    elif sesi[1] == "bandung_bondowoso":
                        # Fungsi hapusJin mengupdate matriks user dan candi sehingga jin yang dipilih akan terhapus dan begitu juga candi yang dibikin oleh jin tersebut
                        user, candi = commands.hapusJin(
                            user, banyakData(user), candi, banyakData(candi))
                    else:
                        print("Anda tidak mempunyai akses")
                # F-05
                elif masukan == "ubahjin":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan ubahjin")
                    elif sesi[1] == "bandung_bondowoso":
                        # Fungsi ubahJin mengupdate matriks user sehingga jin yang dipilih dapat berubah role
                        user = commands.ubahJin(user, banyakData(user))
                    else:
                        print("Anda tidak mempunyai akses")
                # F-06
                elif masukan == "bangun":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan bangun")
                    elif sesi[1] == "pembangun":
                        # Fungsi bangun mengupdate matriks candi dan bahan_bangunan sehingga candi bertambah dan bahan_bangunan berkurang
                        candi, bahan_bangunan = commands.bangun(
                            candi, bahan_bangunan, banyakData(candi), sesi[0])
                    else:
                        print("Anda tidak mempunyai akses")
                # F-07
                elif masukan == "kumpul":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan kumpul")
                    elif sesi[1] == "pengumpul":
                        # Fungsi kumpul ini mengupdate matriks bahan_bangunan sehingga bahan_bangunan bertambah
                        bahan_bangunan = commands.kumpul(bahan_bangunan)
                    else:
                        print("Anda tidak mempunyai akses")
                # F-08
                    # batch kumpul
                elif masukan == "batchkumpul":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan batchkumpul")
                    elif sesi[1] == "bandung_bondowoso":
                        # Fungsi batchKumpul ini mengupdate matriks bahan_bangunan sehingga bahan_bangunan bertambah sesuai banyaknya jin pengumpul
                        bahan_bangunan = commands.batchKumpul(
                            user, banyakData(user), bahan_bangunan)
                    else:
                        print(
                            "Batch kumpul hanya dapat diakses oleh akun Bandung Bondowoso")
                    # batch bangun
                elif masukan == "batchbangun":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan batchbangun")
                    elif sesi[1] == "bandung_bondowoso":
                        # Fungsi batchBangun ini mengupdate matriks candi dan bahan_bangunan sehingga candi bertambah dan bahan_bangunan berkurang sesuai banyaknya jin pembangun
                        candi, bahan_bangunan = commands.batchBangun(
                            user, banyakData(user), bahan_bangunan, candi, banyakData(candi))
                    else:
                        print(
                            "Batch bangun hanya dapat diakses oleh akun Bandung Bondowoso")
                # F-09
                elif masukan == "laporanjin":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan laporanjin")
                    elif sesi[1] == "bandung_bondowoso":
                        # Procedure laporanJin ini memperlihatkan informasi tentang jin
                        commands.laporanJin(user, banyakData(
                            user), banyakData(candi), candi, bahan_bangunan)
                    else:
                        print(
                            "Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso")
                # F-10
                elif masukan == "laporancandi":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan laporancandi")
                    elif sesi[1] == "bandung_bondowoso":
                        # Procedure laporanCandi ini memperlihatkan informasi tentang candi
                        commands.laporanCandi(candi, banyakData(candi))
                    else:
                        print(
                            "Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso")
                # F-11
                elif masukan == "hancurkancandi":
                    if sesi == []:
                        print(
                            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan hancurkancandi")
                    elif sesi[1] == "roro_jonggrang":
                        # Fungsi candi ini mengupdate matriks candi sehingga candi berkurang
                        candi = commands.hancurkanCandi(
                            candi, banyakData(candi))
                    else:
                        print(
                            "Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang")
                # F-12
                elif masukan == "ayamberkokok":
                    # Procedure ayamBerkokok ini memperlihatkan akhirnya atau selesainya game ini
                    commands.ayamBerkokok(banyakData(candi) - 1)
                # F-14
                elif masukan == "save":
                    # Procedure save ini menyimpan semua matriks menjadi csv di dalam folder yang diinginkan
                    commands.save(aksesData(user), banyakData(user), aksesData(
                        candi), banyakData(candi), aksesData(bahan_bangunan), banyakData(bahan_bangunan))
                # F-15
                elif masukan == "help":
                    # Procedure help ini memperlihatkan apasaja commands yang bisa dilaksanakan sesuai role
                    if sesi == []:
                        commands.bantuan("")
                    else:
                        commands.bantuan(sesi[1])
                # F-16
                elif masukan == "exit":
                    # Procedure exit ini mengeluarkan program dengan adanya opsi save
                    commands.exitProgram(aksesData(user), banyakData(user), aksesData(
                        candi), banyakData(candi), aksesData(bahan_bangunan), banyakData(bahan_bangunan))
                # B-05 Ganti Password
                elif masukan == "gantipassword":
                    # Fungsi gantiPassword ini mengupdate matriks user sehingga password username bisa diganti
                    user = commands.gantiPassword(user, banyakData(user))
                else:
                    print("""Command tidak ditemukan
        Masukkan command “help” untuk daftar command yang dapat kamu panggil.""")
                    continue
        else:
            print(f"Folder “{args.folder}” tidak ditemukan")
            exit()


if __name__ == "__main__":
    main()
