"""tes ketiga"""

import string

# MAIN PROGRAM
print("""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
""")
file_input = open("CommencementSpeechByGates2014.txt", "r")
file_stop_words = open("stopwords.txt", "r")
print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)")
list_stop_word = file_stop_words.readlines()
list2_stop_word = []
for i in list_stop_word:
    i = i.replace('\n', '')
    list2_stop_word.append(i)
list_kata = []

#mengambil tiap kata di file input dan di tambahkan ke list_kata
for baris in file_input:
    for kata in baris.split():
        if kata[-1] in string.punctuation:
            kata = kata.replace(kata[-1], '')
        if kata == '': #apabila kata adalah string kosong maka ia tidak dimasukkan ke dalam list kata
            continue
        list_kata.append(kata)
print(f"panjang list sblm di remove: {len(list_kata)}")
# print(list_kata)

""""why is this doesn't even work"""
#menghapus stop_words yang ada di list_kata
print(list2_stop_word)
def is_in(kata, arr):
    if kata in arr:
        return True
    else:
        return False

removed_kata = []

for kata in list_kata:
    for stop_word in list2_stop_word:
        if kata.lower() == stop_word and not is_in(kata, removed_kata):
            removed_kata.append(kata)
            list_kata.remove(kata)
print(removed_kata)
print(f"panjang list setelah di remove: {len(list_kata)}")

#menghitung jumlah kemunculan kata dan disimpan ke dictionaries (dict_kata)
dict_kata = {}
for kata in list_kata:
    if kata in dict_kata:
        dict_kata.update({kata: dict_kata[kata] + 1}) #the value is still problematic(?)
    else:
        dict_kata[kata] = 1

#mengurutkan kata berdasarkan jumlah kemunculan (dari yg terbesar)
sorted_dict_kata = dict(sorted(dict_kata.items(), key=lambda item: item[1], reverse=True))

#ubah dictionaries menjadi dua list (list keys dan list value)
list_kata = list(sorted_dict_kata.keys())
list_jumlah_kata = list(sorted_dict_kata.values())

#mendapatkan 56 kata dengan jumlah kemunculan paling banyak
for i in range(0, 54, 4):
    print(f"{list_jumlah_kata[i]:>4d}:{list_kata[i]:<14s}  {list_jumlah_kata[i+1]:>4d}:{list_kata[i+1]:<14s}  {list_jumlah_kata[i+2]:>4d}:{list_kata[i+2]:<14s}  {list_jumlah_kata[i+3]:>4d}:{list_kata[i+3]:<14s}")
input()

file_stop_words.close()
file_input.close()