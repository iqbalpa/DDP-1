#============================ MAIN PROGRAM =========================
import html_functions as html
import string
from operator import itemgetter

print("""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
""")

try:
    nama_file = input("Silakan masukan nama file: ")
    print()
    file_input = open(nama_file, "r")
    file_stop_words = open("stopwords.txt", "r")
    print(f"{nama_file} : ")
    print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)")

    #mendapatkan semua baris di file stop words
    list_stop_word = file_stop_words.readlines() 
    stop_words = []
    list_kata = []

    #menghapus semua '\n' di akhir stop words dan menambahkannya ke list stop_words
    for stop_word in list_stop_word:
        stop_word = stop_word.replace('\n', '')
        stop_words.append(stop_word)

    #mendapatkan setiap baris di file input
    for baris in file_input:
        for kata in baris.split(): #mendapatkan setiap kata per baris
            #mengahpus tanda baca di akhir kata
            if kata[-1] in string.punctuation: 
                kata = kata.replace(kata[-1], '')

            #menghapus tanda baca di awal kata
            if len(kata) != 0:
                if kata[0] in string.punctuation:
                    kata = kata.replace(kata[0], '')

            #apabila kata adalah string kosong maka ia tidak dimasukkan ke dalam list kata
            if kata == '': 
                continue

            #jika kata adalah string dan diawali huruf kapital
            if kata[0].isupper():
                kata = kata.lower() #kata dibuat menjadi lowercase semua

            #jika kata ada di list stop_words, maka tidak akan dimasukkan ke list_kata
            if kata not in stop_words:
                list_kata.append(kata)

    #mengecek ulang apakah kata sudah tidak diawali dan tidak diakhiri oleh tanda baca
    #kemudian di tambahkan ke list_kata_baru
    list_kata_baru = []
    for kata in list_kata:
        if kata[-1] in string.punctuation:
                kata = kata.replace(kata[-1], '')
        if len(kata) != 0:
            if kata[0] in string.punctuation:
                kata = kata.replace(kata[0], '')
        if kata not in stop_words:
            list_kata_baru.append(kata)

    #membuat dictionaries kata dengan value jumlah kemunculannya
    dict_kata = {}
    for kata in list_kata_baru: 
        #jika kata sudah ada di dictionaries, maka value nya ditambah 1
        if kata in dict_kata: 
            dict_kata.update({kata: dict_kata[kata] + 1}) 

        #jika kata belum ada di dicionaries, maka kata akan ditambahkan dan value nya di set 1
        else:
            dict_kata[kata] = 1

    #mengurutkan kata yang ada di dictionaries menjadi alfabetis terbalik ( z - a )
    kata_alfabetis = dict(sorted(dict_kata.items(), reverse=True))

    #mengurutkan kata yang ada di dicitonaries berdasarkan jumlah kemunculannya
    sorted_kata = dict(sorted(kata_alfabetis.items(), key=itemgetter(1), reverse=True))

    #daftar kata setelah diurutkan
    list_kata2 = list(sorted_kata.keys())

    #daftar value dari kata
    list_jumlah_kata2 = list(sorted_kata.values())

    #mencetak 56 kata dengan jumlah kemunculan terbanyak
    for i in range(0, 54, 4):
        print(f"{list_jumlah_kata2[i]:>4d}:{list_kata2[i]:<14s}  {list_jumlah_kata2[i+1]:>4d}:{list_kata2[i+1]:<14s}  {list_jumlah_kata2[i+2]:>4d}:{list_kata2[i+2]:<14s}  {list_jumlah_kata2[i+3]:>4d}:{list_kata2[i+3]:<14s}")

    #membuat dictionaries baru yang berisi 56 kata dengan jumlah kemunculan terbanyak
    words = {}
    for i in range(0, 56):
        words.update({list_kata2[i]: list_jumlah_kata2[i]})

    #mengurutkan kata yang ada di dictionaries baru menjadi alfabetis
    new_words = dict(sorted(words.items()))

    #list kata yang baru setelah diurutkan
    alphabetical_words = list(new_words.keys())

    #list value dari kata yang baru
    sum_of_words = list(new_words.values())

    #================================== HTML FUNCTIONS ================================
    def main():
        high_count = list_jumlah_kata2[0]
        low_count = list_jumlah_kata2[55]
        body = ''
        for i in range(0, 56):
            body = body + " " + html.make_HTML_word(alphabetical_words[i], sum_of_words[i], high_count, low_count)
        box = html.make_HTML_box(body)  # creates HTML in a box
        # writes HTML to file name 'testFile.html'
        html.print_HTML_file(box, f'A Word Cloud of {nama_file}')
    main()

    print()
    print("Tekan Enter untuk keluar ...", end="")
    input()
    file_stop_words.close()
    file_input.close()

# jika input file tidak ada
except FileNotFoundError:
    print("File tidak ada")
