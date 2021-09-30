# inisiasi jumlah awal setiap elemen (mention, hashtag, url)
mention = 0
hashtag = 0
url     = 0
try:
    masukan = input("Masukkan nama file input: ")
    keluaran = input("Masukkan nama file output: ")
    file_input = open(masukan, "r") #membaca file input
    kalimat_per_baris = file_input.readlines() #daftar kalimat per baris yg ada di file input

    #jika file inputnya kosong
    if kalimat_per_baris == []: 
        raise ValueError ("File ada tapi kosong :(") # akan di set menjadi ValueError dan akan langsung masuk ke exception
    file_output = open(keluaran, "w") #membuat dan/atau menulis file output
    
    #iterasi untuk mengambil kalimat baris demi baris
    for baris in kalimat_per_baris: 
        baris = baris.split() #kalimat disimpan dalam bentuk per kata
        baris.append("\n")
        for kata in baris:
            #jika ada suatu kata berawalan "@" maka di file output akan dituliskan sebagai (M)
            if "@" in kata:
                kata = "(M)"
                mention += 1 #jumlah mention bertambah 1
            #jika ada suatu kata berawalan "#" maka di file output akan dituliskan sebagai (H)
            elif "#" in kata:
                kata = "(H)"
                hashtag += 1 #jumlah hashtag bertambah 1
            #jika ada suatu kata berawalan "www." maka di file output akan dituliskan sebagai (U)
            elif "www." in kata:
                kata = "(U)"
                url += 1 #jumlah url akan bertambah 1
            
            #menuliskan kalimat per baris di file output
            if kata == "\n":
                print(kata, file=file_output, end="")
            else:
                print(kata, file=file_output, end=" ")
    
    print(file=file_output)
    print(15*"#", file=file_output)
    print(f"Mention : {mention:>5}", file=file_output)
    print(f"Hashtag : {hashtag:>5}", file=file_output)
    print(f"Url     : {url:>5}", file=file_output)
    print(f"Output berhasil ditulis pada {keluaran}")
    print("Program selesai. Tekan enter untuk keluar...")

    file_input.close() #menutup file input
    file_output.close() #menutup file output

#jika file input tidak ada
except FileNotFoundError:
    print("File input tidak ditemukan")
    print("Program selesai. Tekan enter untuk keluar...")

#jika file input ada tetapi kosong
except ValueError as err:
    print(err)
    print("Program selesai. Tekan enter untuk keluar...")
