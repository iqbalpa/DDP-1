def smile(happy, sad):
    """ menambahkan 9 happiness dan mengurangi 6 sadness jika ada emot smile"""
    return happy + 9, sad - 6
def sad(sad, anger):
    """menambahkan 10 sadness dan mengurangi 8 anger jika ada emot sad"""
    return sad + 10, anger - 8
def angry(anger, happy):
    """menambahkan 13 anger dan mengurangi 5 happiness jika ada emot anger"""
    return anger + 13, happy - 5
def checker(mood):
    """membuat nilai minimum = 0 dan nilai maksimum = 100, untuk setiap mood"""
    if mood > 100:
        mood = 100
    if mood < 0:
        mood = 0
    return mood

# nilai awal untuk masing-masing mood
happiness = 50
sadness = 50
anger = 50

nama_file = input("Masukkan nama file input: ")
print()
try:
    file_input = open(nama_file, "r")
    kalimat_per_baris = file_input.readlines() #daftar kalimat per baris dari file input
    
    # jika file input ada tapi kosong
    if len(kalimat_per_baris) == 0: 
        raise ValueError ("File input ada tapi kosong :(")

    kalimat_baru = []
    for baris in kalimat_per_baris: #mengambil setiap baris dari daftar kalimat per baris
        #jika Pak Chanek yg mengirim pesan
        if 'Pak Chanek:' in baris: 
            words = baris.split()
            for i in range(len(words)):
                #jika kata adalah '(smile)'
                if words[i] == '(smile)': 
                    happiness, sadness = smile(happiness, sadness) #nilai happiness dan sadness akan diperbarui
                    words[i] = '\U0001f603' #'(smile)' akan diubah jadi emoticon smile

                #jika kata adalah '(sad)'
                elif words[i] == '(sad)': 
                    sadness, anger = sad(sadness, anger) #nilai sadness dan anger akan diperbarui
                    words[i] = '\U0001f622' #'(sad)' akan diubah jadi emoticon sad

                #jika kata adalah '(anger)'
                elif words[i] == '(angry)': 
                    anger, happiness = angry(anger, happiness) #nilai anger dan happiness akan diperbarui
                    words[i] = '\U0001f621' #'(anger)' akan diubah jadi emoticon anger
                kalimat_baru.append(words[i])

                #menambahkan enter (\n) di akhir kalimat
                if i == len(words)-1:
                    kalimat_baru.append('\n')    

        #jika Dek Pepe yang mengirim pesan
        else:
            words = baris.split()
            for i in range(len(words)):
                #jika kata adalah '(smile)'
                if words[i] == '(smile)':
                    words[i] = '\U0001f603' #'(smile)' akan diubah jadi emoticon smile

                #jika kata adalah '(sad)'
                elif words[i] == '(sad)':
                    words[i] = '\U0001f622' #'(sad)' akan diubah jadi emoticon sad

                #jika kata adalah '(anger)'
                elif words[i] == '(angry)':
                    words[i] = '\U0001f621' #'(anger)' akan diubah jadi emoticon anger
                kalimat_baru.append(words[i])

                #menambahkan enter (\n) di akhir kalimat
                if i == len(words)-1:
                    kalimat_baru.append('\n') 
    
    #meng-print semua percakapan Pak Chanek dengan Dek Pepe
    for kata_baru in kalimat_baru:
        if kata_baru == '\n':
            print(kata_baru, end='')
        else:
            print(kata_baru, end=' ')

    #mengecek nilai masing-masing mood dan disesuaikan agar tidak melebihi maksimum atau kurang dari minimum
    happiness = checker(happiness)
    sadness = checker(sadness)
    anger = checker(anger)

    print()
    print("Mengukur suasana hati....")
    print()
    print("##### Hasil Pengukuran #####")
    print(f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}")
    print()
    print("##### Kesimpulan #####")

    #beberapa kondisi untuk menentukan kesimpulan
    if (happiness > sadness) and (happiness > anger):
        print("Pak Chanek sedang bahagia.")
    elif (sadness > happiness) and(sadness > anger):
        print("Pak Chanek sedang sedih.")
    elif (anger > happiness) and (anger > sadness):
        print("Pak Chanek sedang marah.")
    elif (happiness == sadness) and (happiness == anger):
        print("Kesimpulan tidak ditemukan.")
    elif (happiness == sadness) and (happiness > anger):
        print("Pak Chanek sedang bahagia atau sedih.")
    elif (happiness == anger) and (happiness > sadness):
        print("Pak Chanek sedang bahagia atau marah")
    elif (sadness == anger) and (sadness > happiness):
        print("Pak Chanek sedang sedih atau marah.")

    file_input.close()

#jika file input tidak ada
except FileNotFoundError:
    print("File input tidak ada :(")

#jika file input ada tapi kosong
except ValueError as err:
    print(err)
