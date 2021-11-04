#============================ MAIN PROGRAM =========================
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
    import random
    def make_HTML_word(word, cnt, high, low):
        '''
        Make a word with a font size and a random color.
        Font size is scaled between html_big and html_little (to be user set).
        high and low represent the high and low counts in the document.
        cnt is the count of the word. 
        Required -- word (string) to be formatted
                -- cnt (int) count of occurrences of word
                -- high (int) highest word count in the document
                -- low (int) lowest word count in the document
        Return -- a string formatted for HTML that is scaled with respect to cnt
        '''
        html_big = 96
        html_little = 14
        if high != low:
            ratio = (cnt-low)/float(high-low)
        else:
            ratio = 0
        font_size = html_big*ratio + (1-ratio)*html_little
        font_size = int(font_size)
        rgb = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        word_str = '<span style=\"color: rgb{}; font-size:{:s}px;\">{:s}</span>'
        return word_str.format(rgb, str(font_size), word)
    def make_HTML_box(body):
        '''
        Take one long string of words and put them in an HTML box.
        If desired, width, background color & border can be changed in the function
        This function stuffs the "body" string into the the HTML formatting string.

        Required -- body (string), a string of words
        Return -- a string that specifies an HTML box containing the body
        '''
        box_str = """<div style=\"
        width: 560px;
        background-color: rgb(250,250,250);
        border: 1px grey solid;
        text-align: center\" >{:s}</div>
        """
        return box_str.format(body)
    def print_HTML_file(body, title):
        '''
        Create a standard html page (file) with titles, header etc.
        and add the body (an html box) to that page. File created is title+'.html'
        Required -- body (string), a string that specifies an HTML box
        Return -- nothing
        '''
        fd = open(title+'.html', 'w')
        the_str = """
        <html> <head>
        <title>A Word Cloud of """+title+"""</title>
        </head>

        <body>
        <h1>A Word Cloud of """+title+'</h1>'+'\n'+body+'\n'+"""<hr>
        </body> </html>
        """
        fd.write(the_str)
        fd.close()

    def main():
        high_count = list_jumlah_kata2[0]
        low_count = list_jumlah_kata2[55]
        body = ''
        for i in range(0, 56):
            body = body + " " + make_HTML_word(alphabetical_words[i], sum_of_words[i], high_count, low_count)
        box = make_HTML_box(body)  # creates HTML in a box
        # writes HTML to file name 'testFile.html'
        print_HTML_file(box, nama_file)
    main()

    print()
    print("Tekan Enter untuk keluar ...", end="")
    input()
    file_stop_words.close()
    file_input.close()

# jika input file tidak ada
except FileNotFoundError:
    print("File tidak ada")
