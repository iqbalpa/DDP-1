"""PERCOBAAN PERTAMA (5 september 2021, 21.00)"""

import string

# MAIN PROGRAM
print("""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
""")
nama_file = input("Silakan masukan nama file: ")
file_input = open(nama_file, "r")
file_stop_words = open("stopwords.txt", "r")
print()
print()
print(f"{nama_file} :")
print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)")
list_kata = []

#mengambil tiap kata di file input dan di tambahkan ke list_kata
for baris in file_input:
    for kata in baris.split():
        if kata[-1] in string.punctuation:
            kata = kata[:len(kata)-1]
        if kata not in list_kata:
            list_kata.append(kata)

#menghapus stop_words yg ada di list_kata
for kata in list_kata:
    for stop_word in file_stop_words:
        stop_word = stop_word.strip()
        if kata == stop_word:
            list_kata.remove(kata)

#menghitung jumlah kemunculan kata dan disimpan ke dictionaries (dict_kata)
dict_kata = {}
for kata in list_kata:
    if kata in dict_kata:
        dict_kata.update({kata: dict_kata[kata] + 1}) #the value is still problematic(?)
    else:
        dict_kata[kata] = 1
print(dict_kata)
#mengurutkan kata berdasarkan jumlah kemunculan (dari yg terbesar)
sorted_dict_kata = dict(sorted(dict_kata.items(), key=lambda item: item[1], reverse=True))

#ubah dictionaries menjadi dua list (list keys dan list value)
list_kata = list(sorted_dict_kata.keys())
list_jumlah_kata = list(sorted_dict_kata.values())
# print(list_kata)
# print(list_jumlah_kata)

#mendapatkan 56 kata dengan jumlah kemunculan paling banyak
for i in range(0, 54, 4):
    print(f"{list_jumlah_kata[i]:>4d}:{list_kata[i]:<14s}  {list_jumlah_kata[i+1]:>4d}:{list_kata[i+1]:<14s}  {list_jumlah_kata[i+2]:>4d}:{list_kata[i+2]:<14s}  {list_jumlah_kata[i+3]:>4d}:{list_kata[i+3]:<14s}")
input()

file_stop_words.close()
file_input.close()