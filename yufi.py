import string


def enkripsi(nama_file, kunci, hasil_file):
    file = open(f"{nama_file}.txt").read()
    if file == '\n':
        file = ''
    teks = ""
    for i in range(len(file)):
        if file[i].isupper():
            if len(kunci) < len(file):
                kunci += kunci[i % len(kunci)]
            elif len(kunci) > len(file):
                kunci = kunci[i:len(file)]
            letter_index = (file.index(file[i]) + kunci.index(kunci[i])) % 26
            teks += string.ascii_uppercase[letter_index]
        elif file[i].islower():
            if len(kunci) < len(file):
                kunci += kunci[i % len(kunci)]
            elif len(kunci) > len(file):
                kunci = kunci[i:len(file)]
            letter_index = (file.index(file[i]) + kunci.index(kunci[i])) % 26
            teks += string.ascii_lowercase[letter_index]
        else:
            teks += file[i]

    print(
        f'\nPlain Text = {file}\nKey = {kunci}\nCipher text = {teks}\n\n--Enkripsi Selesai--')
    tulis_ulang = open(f'{hasil_file}.txt', 'w+')
    tulis_ulang.write(teks)


def dekripsi(nama_file, kunci, hasil_file):
    file = open(f"{nama_file}.txt").read()
    if file == '\n':
        file = ''
    teks = ""
    for i in range(len(file)):
        if file[i].isupper():
            if len(kunci) < len(file):
                kunci += kunci[i % len(kunci)]
            elif len(kunci) > len(file):
                kunci = kunci[i:len(file)]
            letter_index = (file.index(file[i]) - kunci.index(kunci[i])) % 26
            teks += string.ascii_uppercase[letter_index]
        elif file[i].islower():
            if len(kunci) < len(file):
                kunci += kunci[i % len(kunci)]
            elif len(kunci) > len(file):
                kunci = kunci[i:len(file)]
            letter_index = (file.index(file[i]) - kunci.index(kunci[i])) % 26
            teks += string.ascii_lowercase[letter_index]
        else:
            teks += file[i]

    print(
        f'\nCipher Text = {file}\nKey = {kunci}\nPlain text = {teks}\n\n--Dekripsi Selesai--')
    tulis_ulang = open(f'{hasil_file}.txt', 'w+')
    tulis_ulang.write(teks)


mode = int(input('Pilih Mode: \n[1] Enkripsi\n[2] Dekripsi\nMasukkan Mode: '))
match mode:
    case 1:
        print('\n--Mode Enkripsi--')
        nama_file = input('Masukkan Nama File: ')
        kunci = input('Masukkan kunci: ')
        hasil_file = input('Masukkan Nama File Hasil: ')
        enkripsi(nama_file, kunci, hasil_file)
    case 2:
        print('\n--Mode Dekripsi--')
        nama_file = input('Masukkan Nama File: ')
        kunci = input('Masukkan kunci: ')
        hasil_file = input('Masukkan Nama File Hasil: ')
        dekripsi(nama_file, kunci, hasil_file)
    case _:
        print('\nMaaf pilihan anda tidak tersedia!!!\n')