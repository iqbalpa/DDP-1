import random

print("Halo, selamat datang di Mathbot")
kondisi_awal = True
while kondisi_awal:
    kondisi_mode = True
    print("Pilih Mode: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Campur")
    print("4. Akhiri program")
    print()
    mode = int(input("Masukkan perintah: "))
    if mode == 1:
        print("Baik, pilih mode penjumlahan ya, sekarang pilih kuis jenis apa?")
        while kondisi_mode: 
            kondisi_kuis = True
            print("Pilih kuis: ")
            print("1. Kuis Lepas")
            print("2. Kuis 5")
            print("3. Ganti mode")
            print("4. Akhiri program")
            print()
            jenis_kuis = int(input("Masukkan jenis kuis: "))
            print()
            if jenis_kuis == 1:
                while kondisi_kuis:
                    a = random.randint(0,10)
                    b = random.randint(0,10)
                    print("Berapa " + str(a) + " + " + str(b) +"?")
                    jawaban = input("Jawab: ")
                    if jawaban == "akhiri kuis":
                        kondisi_kuis = False
                        print()
                    elif jawaban.isnumeric() == False:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a+b:
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a+b:
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                        print()
            elif jenis_kuis == 2:
                score = 0
                for i in range(0, 5):
                    a = random.randint(0,10)
                    b = random.randint(0,10)
                    print("Pertanyaan " + str(i+1) + ": ", end="")
                    print("Berapa " + str(a) + " + " + str(b) +"?")
                    jawaban = input("Jawab: ")
                    if jawaban.isnumeric() == False:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a+b:
                        score += 20
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a+b:
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                        print()
                print("Score kamu: " + str(score))
                print()           
            elif jenis_kuis == 3:
                kondisi_mode = False
                print()
                break
            elif jenis_kuis == 4:
                kondisi_awal = False
                break
            else:
                print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
                print()
    elif mode == 2:
        print("Baik, pilih mode pengurangan ya, sekarang pilih kuis jenis apa?")
        while kondisi_mode: 
            kondisi_kuis = True
            print("Pilih kuis: ")
            print("1. Kuis Lepas")
            print("2. Kuis 5")
            print("3. Ganti mode")
            print("4. Akhiri program")
            print()
            jenis_kuis = int(input("Masukkan jenis kuis: "))
            print()
            if jenis_kuis == 1:
                while kondisi_kuis:
                    a = random.randint(0,10)
                    b = random.randint(0,10)
                    while a < b:
                        a = random.randint(0,10)
                        b = random.randint(0,10)
                    print("Berapa " + str(a) + " - " + str(b) +"?")
                    jawaban = input("Jawab: ")                   
                    if jawaban == "akhiri kuis":
                        kondisi_kuis = False
                        print()
                    elif jawaban.isnumeric() == False:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a-b:
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a-b:
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                        print()           
            elif jenis_kuis == 2:
                score = 0
                for i in range(0, 5):
                    a = random.randint(0,10)
                    b = random.randint(0,10)
                    while a < b:
                        a = random.randint(0,10)
                        b = random.randint(0,10)
                    print("Pertanyaan " + str(i+1) + ": ", end="")
                    print("Berapa " + str(a) + " - " + str(b) +"?")
                    jawaban = input("Jawab: ")
                    if jawaban.isnumeric() == False:
                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                        print()
                    elif int(jawaban) == a-b:
                        score += 20
                        print("Hore benar!")
                        print()
                    elif int(jawaban) != a-b:
                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                        print()
                print("Score kamu: " + str(score))
                print()           
            elif jenis_kuis == 3:
                kondisi_mode = False
                print()
                break
            elif jenis_kuis == 4:
                kondisi_awal = False
                break
            else:
                print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
                print()
    elif mode == 3:
        print("Baik, pilih mode campur ya, sekarang pilih kuis jenis apa?")
        while kondisi_mode: 
            kondisi_kuis = True
            print("Pilih kuis: ")
            print("1. Kuis Lepas")
            print("2. Kuis 5")
            print("3. Ganti mode")
            print("4. Akhiri program")
            print()
            jenis_kuis = int(input("Masukkan jenis kuis: "))
            print()
            if jenis_kuis == 1:
                while kondisi_kuis:
                    a = random.randint(0,10)
                    b = random.randint(0,10)
                    c = random.randint(0,1)
                    tanda = 0
                    if c==0:
                        tanda =  " - "
                        while a < b:
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban == "akhiri kuis":
                            kondisi_kuis = False
                            print()
                        elif jawaban.isnumeric() == False:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a-b:
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a-b:
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                            print()
                    else:
                        tanda = " + "
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban == "akhiri kuis":
                            kondisi_kuis = False
                            print()
                        elif jawaban.isnumeric() == False:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a+b:
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a+b:
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                            print()
            elif jenis_kuis == 2:
                score = 0
                for i in range(0, 5):
                    a = random.randint(0,10)
                    b = random.randint(0,10)
                    c = random.randint(0,1)
                    tanda = 0
                    print("Pertanyaan " + str(i+1) + ": ", end="")
                    if c==0:
                        tanda = " - "
                        while a < b:
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban.isnumeric() == False:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a-b:
                            score += 20
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a-b:
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a-b))
                            print()
                    else:
                        tanda = " + "
                        print("Berapa " + str(a) + tanda + str(b) +"?")
                        jawaban = input("Jawab: ")
                        if jawaban.isnumeric() == False:
                            print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()
                        elif int(jawaban) == a+b:
                            score += 20
                            print("Hore benar!")
                            print()
                        elif int(jawaban) != a+b:
                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(a+b))
                            print()    
                print("Score kamu: " + str(score))
                print()        
            elif jenis_kuis == 3:
                kondisi_mode = False
                print()
                break
            elif jenis_kuis == 4:
                kondisi_awal = False
                break
            else:
                print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
                print()
    elif mode == 4:
        kondisi_awal = False
        break
    else:
        print("Program tidak mengenali perintah yang dimasukkan. Silahkan memilih dari perintah yang tersedia.")
        print()
print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
