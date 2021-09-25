print("Selamat datang di Kalkulator IPK!")
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

#akan terus meminta input jumlah mata kuliah hingga user memasukkan angka non negatif
while jumlah_mata_kuliah < 0: 
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

#jika jumlah mata kuliah yg diambil adalah 0
if jumlah_mata_kuliah == 0: 
    print("Tidak ada mata kuliah yang diambil.")
#jika ada mata kuliah yg diambil (tidak 0)
elif jumlah_mata_kuliah > 0:
    print()
    #inisiasi awal untuk jumlah sks yg lulus, total semua sks, total mutu, total mutu yg lulus
    sks_lulus = 0
    total_sks = 0
    mutu = 0
    mutu_lulus = 0
    for i in range(1, jumlah_mata_kuliah+1):
        mata_kuliah = input("Masukkan nama mata kuliah ke-" + str(i) + ": ")
        sks = int(input("Masukkan jumlah SKS " + mata_kuliah + ": "))
        total_sks += sks #total sks akan bertambah setiap user memberikan input sks

        nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
        #akan terus meminta input nilai hingga user memasukkan angka non negatif
        while nilai < 0: 
            print("Nilai yang kamu masukkan tidak valid")
            nilai = float(input("Masukkan nilai yang kamu dapatkan: "))

        #beberapa kondisi untuk rentang nilai tertentu dengan bobotnya masing-masing,
        #setiap sks akan dikalikan dengan bobotnya dan ditambahkan ke total mutu,
        #setiap sks yg lulus akan dikalikan dengan bobotnya dan ditambahkan ke total mutu yg lulus
        if nilai >= 85: 
            mutu += sks*4.00 
            mutu_lulus += sks*4.00 
        elif 80 <= nilai < 85:       
            mutu += sks*3.70
            mutu_lulus += sks*3.70
        elif 75 <= nilai < 80:
            mutu += sks*3.30
            mutu_lulus += sks*3.30
        elif 70 <= nilai < 75:
            mutu += sks*3.00
            mutu_lulus += sks*3.00
        elif 65 <= nilai < 70:
            mutu += sks*2.70
            mutu_lulus += sks*2.70
        elif 60 <= nilai < 65:
            mutu += sks*2.30
            mutu_lulus += sks*2.30
        elif 55 <= nilai < 60:
            mutu += sks*2.00
            mutu_lulus += sks*2.00
        elif 40 <= nilai < 55:
            mutu += sks*1.00
        #nilai yg kurang dari 40 bisa diabaikan karena tidak mempengaruhi IPK maupun IPT

        #jika nilai lebih dari sama dengan 55, maka sks akan ditambahkan ke jumlah sks yg lulus
        if nilai >= 55:
            sks_lulus += sks
        print()
    
    #rumus untuk menghitung IPT
    ipt = round(mutu/total_sks, 2) 
    #jika ada sks yg lulus
    if sks_lulus > 0: 
        ipk = round(mutu_lulus/sks_lulus, 2) #rumus untuk menghitung IPK 
    #jika tidak ada sks yg lulus, maka IPK = 0
    else: 
        ipk = 0
    print("Jumlah SKS lulus: " + str(sks_lulus) + " / " + str(total_sks))
    print("Jumlah mutu lulus: " + str(format(mutu_lulus, '.2f')) + " / " + str(format(mutu, '.2f')))
    print("Total IPK kamu adalah " + str(format(ipk, '.2f')))
    print("Total IPT kamu adalah " + str(format(ipt, '.2f')))
