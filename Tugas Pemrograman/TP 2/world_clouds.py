#============================ MAIN PROGRAM =========================
from html_functions import *
import string

print("""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
""")

nama_file = input("Silakan masukan nama file: ")
print()
file_input = open(nama_file, "r")
file_stop_words = open("stopwords.txt", "r")
print(f"{nama_file} : ")
print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)")
list_stop_word = file_stop_words.readlines()
stop_words = []
list_kata = []

for stop_word in list_stop_word:
    stop_word = stop_word.replace('\n', '')
    stop_words.append(stop_word)

for baris in file_input:
    for kata in baris.split():
        if kata[-1] in string.punctuation:
            kata = kata.replace(kata[-1], '')
        if len(kata) != 0:
            if kata[0] in string.punctuation:
                kata = kata.replace(kata[0], '')
        if kata == '': #apabila kata adalah string kosong maka ia tidak dimasukkan ke dalam list kata
            continue
        if kata[0].isupper():
            kata = kata.lower()
        if kata not in stop_words:
            list_kata.append(kata)

list_kata_baru = []
for kata in list_kata:
    if kata[-1] in string.punctuation:
            kata = kata.replace(kata[-1], '')
    if len(kata) != 0:
        if kata[0] in string.punctuation:
            kata = kata.replace(kata[0], '')
    if kata not in stop_words:
        list_kata_baru.append(kata)

dict_kata = {}
for kata in list_kata_baru:
    if kata in dict_kata:
        dict_kata.update({kata: dict_kata[kata] + 1}) #the value is still problematic(?)
    else:
        dict_kata[kata] = 1

kata_alfabetis = dict(sorted(dict_kata.items(), reverse=True))
sorted_kata = dict(sorted(kata_alfabetis.items(), key=lambda item: item[1], reverse=True))
list_kata2 = list(sorted_kata.keys())
list_jumlah_kata2 = list(sorted_kata.values())

for i in range(0, 54, 4):
    print(f"{list_jumlah_kata2[i]:>4d}:{list_kata2[i]:<14s}  {list_jumlah_kata2[i+1]:>4d}:{list_kata2[i+1]:<14s}  {list_jumlah_kata2[i+2]:>4d}:{list_kata2[i+2]:<14s}  {list_jumlah_kata2[i+3]:>4d}:{list_kata2[i+3]:<14s}")

words = {}
for i in range(0, 56):
    words.update({list_kata2[i]: list_jumlah_kata2[i]})
new_words = dict(sorted(words.items()))
alphabetical_words = list(new_words.keys())
sum_of_words = list(new_words.values())

#======================================== FUNCTIONS CALL =================================
def main():
    high_count = list_jumlah_kata2[0]
    low_count = list_jumlah_kata2[55]
    body = ''
    for i in range(0, 56):
        body = body + " " + make_HTML_word(alphabetical_words[i], sum_of_words[i], high_count, low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    # writes HTML to file name 'testFile.html'
    print_HTML_file(box, f'A Word Cloud of {nama_file}')
main()

print()
print("Tekan Enter untuk keluar ...", end="")
input()
file_stop_words.close()
file_input.close()
