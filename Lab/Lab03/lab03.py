a = input("Masukkan input himpunan A: ")
b = input("Masukkan input himpunan B: ")

himpunan_a = a.split(',') # daftar elemen himpunan A
himpunan_b = b.split(',') # daftar elemen himpunan B

print("{", end = "")
for i in himpunan_a:
    for j in himpunan_b:
        # kondisi untuk cartesian product terakhir => tidak perlu mem-print ',' setelah ')'
        if (i == himpunan_a[-1]) and (j == himpunan_b[-1]):
            print("(" + str(i) + "," + str(j) + ")", end = "")
        # jika bukan cartesian product terakhir => maka perlu mem-print ',' setelah ')'
        else: 
            print("(" + str(i) + "," + str(j) + ")" + ",", end = " ")
print("}")
