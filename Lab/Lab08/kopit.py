def tidak_valid():
    return "Maaf perintah tidak dikenali. Masukkan perintah yang valid."

# dictionaries untuk menampung rantai penularan
# penular sebagai key dan tertular sebagai values
rantai_penularan = dict()


# fungsi untuk mendapatkan rantai penularan 
def penularan(lst_input, kamus):

    # base case: jika panjang list adalah 0
    if len(lst_input) == 0:
        return kamus

    # recursive case
    else:

        # mendapatkan daftar nama dari elemen pertama di lst_input
        names = lst_input[0]
        names = names.split()

        # penular adalah nama pertama di list names
        penular = names[0]

        # tertular adalah nama selain penular
        tertular = names[1:]

        for nama in kamus:
            if penular in kamus[nama]:
                kamus[nama] += tertular

        # membuat dictionaries dengan key adalah penular dan values adalah tertular
        if penular not in kamus:
            kamus[penular] = tertular
        else:
            kamus[penular] += tertular 

        return penularan(lst_input[1:], kamus)


### MAIN PROGRAM ###
orang_terlibat = set()

print("Masukkan rantai penyebaran:")

# variable akumulator untuk menampung semua input
masukkan = []

# program akan terus meminta input hingga user memberi input "selesai"
masuk = input()
while masuk != "selesai":

    # menambahkan input ke dalam list masukkan
    masukkan.append(masuk)

    # mendapatkan nama orang yg ada di dalam rantai penularan 
    # dan ditambahkan ke set orang_terlibat
    for nama in masuk.split():
        orang_terlibat.add(nama)

    masuk = input()

# memanggil fungsi penularan
penularan(masukkan, rantai_penularan)

print("""
List perintah:
1. RANTAI_PENYEBARAN 
2. CEK_PENULARAN 
3. EXIT
""")

# program akan terus meminta input perintah hingga user memberi input "EXIT"
cond2 = True
while cond2:
    perintah = input("Masukkan perintah: ")
    perintah = perintah.split()


    if perintah[0] == "RANTAI_PENYEBARAN":
        penular = perintah[1]

        # jika nama_penular tidak ada di dalam rantai penyebaran
        if penular not in orang_terlibat:
            print(f"Maaf, nama {penular} tidak ada dalam rantai penyebaran.")

        else:
            print(f"Rantai penyebaran {penular}")
            print(f"- {penular}")

            # iterasi untuk mendapatkan semua nama_tertular yg tertular oleh nama_penular
            for tertular in rantai_penularan[penular]:
                print(f"- {tertular}")
    

    elif perintah[0] == "CEK_PENULARAN":
        tertular = perintah[1]
        penular = perintah[2]

        # jika nama penular dan atau nama tertular tidak ada di rantai penyebaran
        # maka, akan ditampilkan bahwa nama tsb tidak ada
        if (tertular not in orang_terlibat) and (penular not in orang_terlibat):
            print(f"Maaf, nama {tertular} dan {penular} tidak ada dalam rantai penyebaran.")
        elif tertular not in orang_terlibat:
            print(f"Maaf, nama {tertular} tidak ada dalam rantai penyebaran.")
        elif penular not in orang_terlibat:
            print(f"Maaf, nama {penular} tidak ada dalam rantai penyebaran.")

        # jika nama penular dan tertular ada di rantai penyebaran
        else:

            # jika tertular merupakan korban penularan dari penular
            if tertular in rantai_penularan[penular]:
                print("YA")

            # jika tertular bukan merupakan korban dari penular
            else:
                print("TIDAK")
    

    elif perintah[0] == "EXIT":
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
        cond2 = False
    

    # jika perintah tidak valid
    else:
        print(tidak_valid())
    print()
    
