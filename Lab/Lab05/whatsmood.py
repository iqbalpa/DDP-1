def smile(happy, sad):
    return happy + 9, sad - 6
def sad(sad, anger):
    return sad + 10, anger - 8
def angry(anger, happy):
    return anger + 13, happy - 5
def checker(mood):
    if mood > 100:
        mood = 100
    if mood < 0:
        mood = 0
    return mood

happiness = 50
sadness = 50
anger = 50

nama_file = input("Masukkan nama file input: ")
print()
try:
    file_input = open(nama_file, "r")
    kalimat_per_baris = file_input.readlines()
    if len(kalimat_per_baris) == 0:
        raise ValueError ("File input ada tapi kosong :(")
    kalimat_baru = []
    for baris in kalimat_per_baris:
        if 'Pak Chanek:' in baris:
            words = baris.split()
            for i in range(len(words)):
                if words[i] == '(smile)':
                    happiness, sadness = smile(happiness, sadness)
                    words[i] = '\U0001f603'
                elif words[i] == '(sad)':
                    sadness, anger = sad(sadness, anger)
                    words[i] = '\U0001f622'
                elif words[i] == '(angry)':
                    anger, happiness = angry(anger, happiness)
                    words[i] = '\U0001f621'
                kalimat_baru.append(words[i])
                if i == len(words)-1:
                    kalimat_baru.append('\n')         
        else:
            words = baris.split()
            for i in range(len(words)):
                if words[i] == '(smile)':
                    words[i] = '\U0001f603'
                elif words[i] == '(sad)':
                    words[i] = '\U0001f622'
                elif words[i] == '(angry)':
                    words[i] = '\U0001f621'
                kalimat_baru.append(words[i])
                if i == len(words)-1:
                    kalimat_baru.append('\n') 
    
    for kata_baru in kalimat_baru:
        if kata_baru == '\n':
            print(kata_baru, end='')
        else:
            print(kata_baru, end=' ')

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
    if (happiness > sadness) and (happiness > anger):
        print("Pak Chanek sedang bahagia.")
    elif (sadness > happiness) and(sadness > anger):
        print("Pak Chanek sedang sedih.")
    elif (anger > happiness) and (anger > sadness):
        print("Pak Chanek sedang marah.")
    elif (happiness == sadness):
        if happiness > anger:
            print("Pak Chanek sedang bahagia atau sedih.")
        elif happiness == anger:
            print("Kesimpulan tidak ditemukan.")
    elif (happiness == anger) and (happiness > sadness):
        print("Pak Chanek sedang bahagia atau marah")
    elif (sadness == anger) and (sadness > happiness):
        print("Pak Chanek sedang sedih atau marah.")

    file_input.close()

except FileNotFoundError:
    print("File input tidak ada :(")
except ValueError as err:
    print(err)
