def login(user, banyakData):
    Username = str(input("Username: "))
    Password = str(input("Password: "))

    for i in range (banyakData):
        if Username == user[i][0]:
            if Password == user[i][1]:
                print(f"Selamat datang {Username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                return [Username, user[i][2]]
            else:
                print("Password salah!")
                return []
    print("Username tidak terdaftar!")
    return []

