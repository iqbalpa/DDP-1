import random #import modul random
print("Halo, selamat datang di Mathbot")
kondisi_awal = True #set kondisi_awal bernilai True
while kondisi_awal:
    kondisi_mode = True #set kondisi_mode bernilai True
    print("Pilih Mode: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Campur")
    print("4. Akhiri program")
    print()
    mode = int(input("Masukkan perintah: "))
    
    #jika user memilih mode penjumlahan
    if mode == 1: 
        print("Baik, pilih mode penjumlahan ya, sekarang pilih kuis jenis apa?")
        while kondisi_mode: 
            kondisi_kuis = True #set kondisi_kuis bernilai True
            print("Pilih kuis: ")
            print("1. Kuis Lepas")
            print("2. Kuis 5")
            print("3. Ganti mode")
            print("4. Akhiri program")
            print()
            jenis_kuis = int(input("Masukkan jenis kuis: "))
            print()
            #jika user memilih kuis lepas
            if jenis_kuis == 1:
                while kondisi_kuis:
                    a = random.randint(0,10) #mendapatkan angka random
                    b = random.randint(0,10)
                    print("Berapa " + str(a) + " + " + str(b) +"?")
                    jawaban = input("Jawab: ")
                    if jawaban == "akhiri kuis": #jika user memberi input "akhiri kuis"
                        kondisi_kuis = False #kondisi_kuis akan False dan keluar dari loop kondisi_kuis
                        print()
                    elif jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a+b: #jika jawaban benar
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a+b: #jika jawabannya angka tetapi salah
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                        print()
            #jika user memilih kuis 5
            elif jenis_kuis == 2:
                score = 0 #score awal
                for i in range(0, 5):
                    a = random.randint(0,10) #mendapatkan angka random
                    b = random.randint(0,10)
                    print("Pertanyaan " + str(i+1) + ": ", end="")
                    print("Berapa " + str(a) + " + " + str(b) +"?")
                    jawaban = input("Jawab: ")
                    if jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a+b: #jika jawaban benar
                        score += 20 #score bertambah 20 
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a+b: #jika jawabannya angka tetapi salah
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                        print()
                print("Score kamu: " + str(score))
                print()  
            #jika user memilih ganti mode         
            elif jenis_kuis == 3:
                kondisi_mode = False #kondisi_mode akan False dan keluar dari loop kondisi_mode
                print()
            #jika user memilih akhiri program
            elif jenis_kuis == 4:
                kondisi_mode = False #kondisi_mode akan False dan keluar dari loop kondisi_mode
                kondisi_awal = False #kondisi_awal akan False dan keluar dari loop kondisi_awal
            #jika input dari user tidak ada di pilihan
            else:
                print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
                print()
    
    #jika user memilih mode pengurangan
    elif mode == 2:
        print("Baik, pilih mode pengurangan ya, sekarang pilih kuis jenis apa?")
        while kondisi_mode: 
            kondisi_kuis = True #set kondisi_kuis bernilai True
            print("Pilih kuis: ")
            print("1. Kuis Lepas")
            print("2. Kuis 5")
            print("3. Ganti mode")
            print("4. Akhiri program")
            print()
            jenis_kuis = int(input("Masukkan jenis kuis: "))
            print()
            #jika user memilih kuis lepas
            if jenis_kuis == 1:
                while kondisi_kuis:
                    a = random.randint(0,10) #mendapatkan angka random
                    b = random.randint(0,10)
                    while a < b: #jika a<b maka akan terjadi looping hingga didapat a>b
                        a = random.randint(0,10)
                        b = random.randint(0,10)
                    print("Berapa " + str(a) + " - " + str(b) +"?")
                    jawaban = input("Jawab: ")                   
                    if jawaban == "akhiri kuis": #jika user memberi input "akhiri kuis"
                        kondisi_kuis = False #kondisi_kuis akan False dan keluar dari loop kondisi_kuis
                        print()
                    elif jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a-b: #jika jawabannya benar
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a-b: #jika jawabannya angka tetapi salah
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                        print() 
            #jika user memiliih kuis 5          
            elif jenis_kuis == 2:
                score = 0
                for i in range(0, 5):
                    a = random.randint(0,10) #mendapatkan angka random
                    b = random.randint(0,10)
                    while a < b: #jika a<b maka akan terjadi looping hingga didapat a>b
                        a = random.randint(0,10)
                        b = random.randint(0,10)
                    print("Pertanyaan " + str(i+1) + ": ", end="")
                    print("Berapa " + str(a) + " - " + str(b) +"?")
                    jawaban = input("Jawab: ")
                    if jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a-b: #jika jawabannya benar
                        score += 20 #score bertambah 20 
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a-b: #jika jawabannya angka tetapi salah
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                        print()
                print("Score kamu: " + str(score))
                print() 
            #jika user memilih ganti mode          
            elif jenis_kuis == 3:
                kondisi_mode = False #kondisi_mode akan False dan keluar dari loop kondisi_mode
                print()
            #jika user memilih akiri program
            elif jenis_kuis == 4:
                kondisi_mode = False #kondisi_mode akan False dan keluar dari loop kondisi_mode
                kondisi_awal = False #kondisi_awal akan False dan keluar dari loop kondisi_awal
            #jika input dari user tidak ada di pilihan
            else:
                print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
                print()

    #jika user memilih mode campur
    elif mode == 3:
        print("Baik, pilih mode campur ya, sekarang pilih kuis jenis apa?")
        while kondisi_mode: 
            kondisi_kuis = True #set kondisi_kuis bernilai True
            print("Pilih kuis: ")
            print("1. Kuis Lepas")
            print("2. Kuis 5")
            print("3. Ganti mode")
            print("4. Akhiri program")
            print()
            jenis_kuis = int(input("Masukkan jenis kuis: "))
            print()
            #jika user memilih kuis lepas
            if jenis_kuis == 1:
                while kondisi_kuis:
                    a = random.randint(0,10) #mendapatkan angka random
                    b = random.randint(0,10)
                    c = random.randint(0,1) #mendapatkan angka random antara 1 dan 0
                    tanda = 0
                    if c==0: #jika c=0, maka akan terpilih operasi pengurangan
                        tanda =  " - "
                        while a < b: #jika a<b maka akan terjadi looping hingga didapat a>b
                            a = random.randint(0,10) 
                            b = random.randint(0,10)
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban == "akhiri kuis": #jika user memberi input "akhiri kuis"
                            kondisi_kuis = False #kondisi_kuis akan False dan keluar dari loop kondisi_kuis
                            print()
                        elif jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a-b: #jika jawabannya benar
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a-b: #jika jawabannya angka tetapi salah
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                            print()
                    else: #jika c=1, maka akan terpilih operasi penjumlahan
                        tanda = " + "
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban == "akhiri kuis": #jika user memberi input "akhiri kuis"
                            kondisi_kuis = False #kondisi_kuis akan False dan keluar dari loop kondisi_kuis
                            print()
                        elif jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a+b: #jika jawabannya benar
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a+b: #jika jawabannya angka tetapi salah
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                            print()
            #jika user memilih kuis 5
            elif jenis_kuis == 2:
                score = 0 #score awal
                for i in range(0, 5):
                    a = random.randint(0,10) #mendapatkan angka random
                    b = random.randint(0,10)
                    c = random.randint(0,1) #mendapatkan angka random antara 1 dan 0
                    tanda = 0
                    print("Pertanyaan " + str(i+1) + ": ", end="")
                    if c==0: #jika c=0, maka akan terpilih operasi pengurangan
                        tanda = " - "
                        while a < b: #jika a<b maka akan terjadi looping hingga didapat a>b
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a-b: #jika jawabannya benar
                            score += 20 #score bertambah 20 
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a-b: #jika jawabannya angka tetapi salah
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                            print()
                    else: #jika c=1, maka akan terpilih operasi penjumlahan
                        tanda = " + "
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban.isnumeric() == False: #jika jawaban bukan sebuah angka
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a+b: #jika jawabannya benar
                            score += 20 #score bertambah 20 
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a+b: #jika jawabannya angka tetapi salah
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                            print()    
                print("Score kamu: " + str(score))
                print()   
            #jika user memilih ganti mode     
            elif jenis_kuis == 3:
                kondisi_mode = False #kondisi_mode akan False dan keluar dari loop kondisi_mode
                print()
            #jika user memilih akiri program
            elif jenis_kuis == 4:
                kondisi_mode = False #kondisi_mode akan False dan keluar dari loop kondisi_mode
                kondisi_awal = False #kondisi_awal akan False dan keluar dari loop kondisi_awal
            #jika input dari user tidak ada di pilihan
            else:
                print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
                print()
    
    #jika user memilih akiri program
    elif mode == 4:
        kondisi_awal = False #kondisi_awal akan False dan keluar dari loop kondisi_awal
    #jika input dari user tidak ada di pilihan
    else:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print()
print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
