import random
# Functions adapted from ProgrammingHistorian
# http://niche.uwo.ca/programming-historian/index.php/Tag_clouds
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
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()

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

def main():
    high_count = list_jumlah_kata[0]
    low_count = list_jumlah_kata[55]
    body = ''
    for i in range(0, 56):
        body = body + " " + make_HTML_word(list_kata[i], list_jumlah_kata[i], high_count, low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    # writes HTML to file name 'testFile.html'
    print_HTML_file(box, 'testFile')
main()

print()
print()
print("Tekan Enter untuk keluar ...", end="")
input()
file_stop_words.close()
file_input.close()   
