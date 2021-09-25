import math

r = float(input("Masukkan radius ingkaran: ")) 

# rumus luas untuk tiap bentuk
segitiga = r*r
lingkaran = math.pi*r**2
persegi = 4*r*r

print("Luas daerah cat merah:", format(persegi-lingkaran, '.2f'))
print("Luas daerah cat kuning:", format(lingkaran-segitiga, '.2f'))
print("Luas daerah cat ungu:", format(segitiga, '.2f'))
