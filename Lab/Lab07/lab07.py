def tidak_valid():
    print("Perintah yang dimasukkan tidak valid")

print("Selamat datang! Silakan masukkan jadwal KA:")

jadwal = set()
tujuan = set()
daftar_kelas = {"Eksekutif": set(), "Bisnis": set(), "Ekonomi": set()}

# program akan terus meminta input hingga user memberikan input "selesai"
cond1 = True
while cond1:
    masukkan = input()
    if masukkan != "selesai":
        masukkan = tuple(masukkan.split())

        # menambahkan KA ke jadwal
        jadwal.add(masukkan)

        # menambahkan tujuan KA ke tujuan
        tujuan.add(masukkan[1])

        # jika nomor KA adalah 1xx, maka ia dimasukkan ke daftar kelas Eksekutif
        if masukkan[0][0] == "1":
            daftar_kelas["Eksekutif"].add(masukkan)
        
        # jika nomor KA adalah 2xx, maka ia dimasukkan ke daftar kelas Bisnis
        elif masukkan[0][0] == "2":
            daftar_kelas["Bisnis"].add(masukkan)

        # jika nomor KA adalah 3xx, maka ia dimasukkan ke daftar kelas Ekonomi
        elif masukkan[0][0] == "3":
            daftar_kelas["Ekonomi"].add(masukkan)

    # jika user memberikan input "selesai", maka akan keluar dari loop
    else:
        cond1 = False

print("""
Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
4. EXIT
""")

# program akan terus meminta input perintah hingga user memberikan perintah "EXIT"
cond2 = True
while cond2:
    perintah = input("Masukkan perintah: ")
    perintah = perintah.split()

    # jika perintah adalah INFO_TUJUAN
    if perintah[0] == "INFO_TUJUAN":
        print("KA di stasiun ini memiliki tujuan akhir:")

        # menampilkan semua tujuan KA yang ada
        for elem in tujuan:
            print(elem)


    # jika perintah adalah TUJUAN_KELAS
    elif perintah[0] == "TUJUAN_KELAS":

        # jika perintah dari user tidak lengkap atau kelas yang dimasukkan oleh user tidak tersedia
        if (len(perintah) != 3) or (perintah[2] not in daftar_kelas): 
            tidak_valid()
        
        else:
            counter = 0
            for kelas in daftar_kelas:

                # jika kelas KA yang ada sesuai dengan kelas yang diminta oleh user
                if kelas == perintah[2]:

                    # looping untuk setiap KA yang sesuai dengan kelas permintaan user
                    for (nomor,tujuan,jam,harga) in daftar_kelas[kelas]:

                        # jika tujuan KA yang ada sesuai dengan yang diminta oleh user
                        if tujuan == perintah[1]:
                            print(f"KA {nomor} berangkat pukul {jam} dengan harga tiket {harga}")
                        else:
                            counter += 1
            
            # jika tidak ada KA dengan tujuan dan kelas yang diminta oleh user
            if counter == len(daftar_kelas[perintah[2]]):
                print("Tidak ada jadwal KA yang sesuai.")


    # jika perintah adalah TUJUAN_JAM
    elif perintah[0] == "TUJUAN_JAM":

        # jika perintah dari user tidak lengkap
        if len(perintah) != 3:
            tidak_valid()

        else:
            counter = 0

            # looping untuk setiap KA yg ada
            for (nomor,tujuan,jam,harga) in jadwal:

                # jika tujuan KA yang ada sesuai dengan yang diminta oleh user
                # dan jam KA yang ada kurang dari sama dengan yang diminta oleh user
                if (tujuan == perintah[1]) and (int(jam) <= int(perintah[2])):
                    print(f"KA {nomor} berangkat pukul {jam} dengan harga tiket {harga}")
                else:
                    counter += 1

            # jika tidak ada KA dengan tujuan dan jam yang diminta oleh user
            if counter == len(jadwal):
                print("Tidak ada jadwal KA yang sesuai.")
        

    # jika perintah adalah EXIT
    elif perintah[0] == "EXIT":
        print("Terima kasih sudah menggunakan program ini!")
        cond2 = False # maka akan keluar dari loop


    # jika input user tidak ada di daftar perintah
    else:
        tidak_valid()
    print()
