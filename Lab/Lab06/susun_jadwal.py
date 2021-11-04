MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24
HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]
MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["ddp 1 b", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["manbis", HARI[4] + JAM[13] + 1, HARI[4] + JAM[15] + 40],
["matdis 1 a", HARI[4] + JAM[9] + 0, HARI[4] + JAM[13] + 0],
["matdis 1 b", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]

# function untuk mengubah total waktu (start-time atau end-time) ke dalam format "hari, jam.menit"
def time_converter(time):
    days = ["Senin,", "Selasa,", "Rabu,", "Kamis,", "Jumat,", "Sabtu,", "Minggu,"]
    hari = time // MENIT_DALAM_HARI
    jam = (time % MENIT_DALAM_HARI) // MENIT_DALAM_JAM
    menit = ((time % MENIT_DALAM_HARI) % MENIT_DALAM_JAM)
    return f"{days[hari]:<8}{jam:02d}.{menit:02d}  "

# daftar matkul yang disediakan
matkul_tersedia = {nama for nama,start,end in MATKUL_TERSEDIA}
jadwal = []

cond = True
while cond:
    print("""=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
""")
    # leading dan trailing spaces pada input perintah dihilangkan menggunakan strip()
    # kemudian input diubah menjadi lowercase (agar insensitive case) 
    perintah = input("Masukkan pilihan: ").strip().lower()

    # jika perintah adalah add matkul
    if perintah == "1":
        # untuk input matkul juga dilakukan hal yg sama dengan input perintah
        matkul = input("Masukkan nama matkul: ").strip().lower()

        if matkul not in matkul_tersedia:
            print("Matkul tidak ditemukan")

        # jika input matkul tersedia, maka akan ditambahkan matkul tsb dan jadwalnya ke list jadwal
        else: 
            pilihan = [[nama,start,end] for nama,start,end in MATKUL_TERSEDIA if nama == matkul]
            jadwal.extend(pilihan)

    # jika perintah adalah drop matkul
    elif perintah == "2":
        matkul = input("Masukkan nama matkul: ").strip().lower()
        # daftar matkul yang telah ditambahkan sebelumnya
        matkul_diambil = {nama for nama,start,end in jadwal}

        if matkul not in matkul_diambil:
            print("Matkul tidak ditemukan")

        # jika input matkul tersedia, maka matkul tsb akan dihapus dari list jadwal
        else:
            jadwal2 = jadwal[:]
            for nama in jadwal2:
                if nama[0] == matkul:
                    jadwal.remove(nama)

    # jika perintah adalah cek ringkasan
    elif perintah == "3":
        temp = False
        indeks = []

        # jika ada jam matkul yg beririsan maka "temp" menjadi True
        # dan index matkul yg jamnya beririsan akan disimpan ke list indeks
        for i in range(len(jadwal)):
            for j in range(i+1, len(jadwal)):
                if (jadwal[i][1] <= jadwal[j][1] <= jadwal[i][2]):
                    temp = True
                    indeks.append((i, j))

        # jika ada matkul yg bentrok
        if temp:
            for i,j in indeks:
                print(f"    {jadwal[i][0]} bentrok dengan {jadwal[j][0]}")
        
        # jika tidak ada matkul yg bentrok
        else:
            print("Tidak ada mata kuliah yang bermasalah")

    # jika perintah adalah lihat daftar matkul
    elif perintah == "4":

        # jika belum ada matkul yg ditambahkan
        if len(jadwal) == 0:
            print("Tidak ada mata kuliah yang diambil")

        # jika sudah ada matkul yg ditambahkan
        else:
            print("daftar matkul:")
            for element in jadwal:
                # mendapatkan waktu start-time
                start = time_converter(element[1])
                # mendapatkan waktu end-time
                end = time_converter(element[2])
                print(f"    {element[0].upper():<14}{start} s/d {end}")

    # jika perintah adalah selesai
    elif perintah == "5":
        print("Terima kasih!")
        # cond akan menjadi False dan akan keluar dari loop sehingga program akan berakhir
        cond = False

    # jika perintah yg dimasukkan tidak valid
    else:
        print("Maaf, pilihan tidak tersedia")
    print()