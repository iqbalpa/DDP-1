#=========================MORE ELEGANT THAN bismillah.py HAHAHAHAH=====================
import string

print("""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.""")

file_input = open("CommencementSpeechByGates2014.txt", "r")
file_stop_words = open("stopwords.txt", "r")
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

dict_kata = {}
for kata in list_kata:
    if kata in dict_kata:
        dict_kata.update({kata: dict_kata[kata] + 1}) #the value is still problematic(?)
    else:
        dict_kata[kata] = 1

sorted_dict_kata = dict(sorted(dict_kata.items(), key=lambda item: item[1], reverse=True))
list_kata = list(sorted_dict_kata.keys())
list_jumlah_kata = list(sorted_dict_kata.values())

for i in range(0, 54, 4):
    print(f"{list_jumlah_kata[i]:>4d}:{list_kata[i]:<14s}  {list_jumlah_kata[i+1]:>4d}:{list_kata[i+1]:<14s}  {list_jumlah_kata[i+2]:>4d}:{list_kata[i+2]:<14s}  {list_jumlah_kata[i+3]:>4d}:{list_kata[i+3]:<14s}")
