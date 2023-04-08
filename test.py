def splits(baris, fileName):
    baris += ";"
    barisBaru = [None for _ in range(3)]
    j = 0
    kata = ""
    if fileName == "user":
        panjang = 3
    i = 0
    while True:
        if j == 3:
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


print(splits(["hallo;hello;holla"][0], "user"))
