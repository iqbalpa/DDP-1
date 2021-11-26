# list untuk menampung nama product yang ada
products_name = []

def urutkan_produk(produk):
    return produk.get_name()

class User() :
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.__user_name = user_name
        self.__tipe = tipe

    # method untuk mendapatkan user_name
    def get_name(self) : 
        return self.__user_name

    # method untuk mendapatkan tipe
    def get_tipe(self) : 
        return self.__tipe


class Seller(User) : 
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class Seller
        """
        super().__init__(user_name, tipe)
        self.pemasukan = 0
        self.list_barang_jual = []
        self.products = []

    # method untuk mendapatkan pemasukan SELLER
    def get_pemasukan(self) : 
        return self.pemasukan

    # method untuk menambah jumlah pemasukan sesuai dengan harga barang yang dibeli BUYER
    def set_pemasukan(self, produk) : 
        self.pemasukan += produk.get_harga()

    # method untuk menambahkan produk
    def tambah_product(self, produk_baru) :
        produk_baru = produk_baru.split()
        nama = produk_baru[0]
        harga = int(produk_baru[1])
        stok = int(produk_baru[2])

        # jika nama barang sudah pernah ditambahkan oleh SELLER
        if nama in self.products:
            print("Produk sudah pernah terdaftar")

        # jika barang belum pernah ditambahkan oleh SELLER
        else:

            # produk akan ditambahkan ke list_barang_jual milik SELLER,
            # self.products, dan products_name
            produk = Product(nama, harga, stok, self.get_name())
            self.list_barang_jual.append(produk)
            list_product.append(produk)
            self.products.append(nama)
            products_name.append(nama)

    # method untuk melihat produk yang dijual
    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")

        # mengurutkan self.list_barang_jual berdasarkan nama produk
        self.list_barang_jual.sort(key=urutkan_produk)

        for produk in self.list_barang_jual : 
            print(f"{produk.get_name():<16s}|{produk.get_harga():<11d}|{produk.stok:<7d}")
        print("-------------------------------------\n")

    # method menu untuk SELLER
    def menu(self) : 
        print(f"Anda telah masuk dalam akun {self.get_name()} sebagai SELLER")
        print()
        print(f"Selamat datang {self.get_name()}")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")
        print()

        cond = True
        while cond:
            print(f"Pemasukan anda {self.get_pemasukan()},")
            perintah = input("Apa yang ingin anda lakukan? ")

            # jika perintah adalah TAMBAHKAN_PRODUK
            if perintah == "1":
                data_produk = input("Masukkan data produk : ")
                self.tambah_product(data_produk)

            # jika perintah adalah LIHAT_DAFTAR_PRODUK_SAYA
            elif perintah == "2":
                self.lihat_produk_jualan_saya()

            # jika perintah adalah LOG_OUT
            elif perintah == "3":
                print(f"Anda telah keluar dari akun {self.get_name()}")

                # maka cond di set menjadi False dan akan keluar dari loop
                cond = False
            print()
            


class Buyer(User) : 
    def __init__(self, user_name, tipe, saldo):
        super().__init__(user_name, tipe)
        self.saldo = saldo
        self.list_barang_beli = []

    # method untuk melihat semua porduk yang ada di Dekdepedia
    def lihat_semua_produk(self):
        print("Berikut merupakan daftar produk di Dekdepedia")
        print("-----------------------------------------------")
        print("  Nama Produk   |   Harga   | Stock |  Penjual")
        print("-----------------------------------------------")

        # mengurutkan list_product berdasarkan nama produk
        list_product.sort(key=urutkan_produk)

        for produk in list_product:
            print(f"{produk.get_name():<16s}|{produk.get_harga():<11d}|{produk.stok:<7d}|{produk.get_seller():<9s}")
        print("-----------------------------------------------")
    
    # mrthod untuk membeli produk
    def beli_produk(self):
        nama_barang = input("Masukkan barang yang ingin dibeli : ")

        # jika produk yang diinginkan BUYER tidak ada
        if nama_barang not in products_name:
            print(f"Barang dengan nama {nama_barang} tidak ditemukan dalam Dekdepedia.")

        # jika produk yang diinginkan BUYER ada
        else:
            for produk in list_product:
                if nama_barang == produk.get_name():

                    # jika saldo BUYER >= harga produk dan stok produk masih ada
                    if (self.saldo >= produk.get_harga()) and (produk.stok >= 1):
                        print(f"Berhasil membeli {produk.get_name()} dari {produk.get_seller()}")

                        # produk akan ditambahkan ke list_barang_beli milik BUYER
                        self.list_barang_beli.append(produk)

                        # saldo BUYER akan berkurang sebesar harga produk
                        self.saldo -= produk.get_harga()

                        # stok produk akan berkurang 1
                        produk.stok -= 1

                        # pemasukan SELLER yang menjual barang tsb akan bertambah sebesar harga produk
                        for user in list_user:
                            if user.get_name() == produk.get_seller():
                                user.set_pemasukan(produk)

                    # jika stok produk tidak tersedia
                    elif produk.stok < 1:
                        print("Maaf, stok produk telah habis.")

                    # jika saldo BUYER < harga produk
                    elif self.saldo < produk.get_harga():
                        print(f"Maaf, saldo Anda tidak cukup untuk membeli {produk.get_name()}")
                    
    # method untuk melihat riwayat pembelian
    def riwayat_pembelian(self):
        print("Berikut merupakan barang yang saya beli")
        print("----------------------------------------")
        print("  Nama Produk   |   Harga   | Penjual")
        print("----------------------------------------")

        # mengurutkan self.list_barang_beli berdasarkan nama produk
        self.list_barang_beli.sort(key=urutkan_produk)

        for produk in self.list_barang_beli:
            print(f"{produk.get_name():<16s}|{produk.get_harga():<11d}|{produk.get_seller():<9s}")
        print("----------------------------------------")

    # method menu untuk BUYER
    def menu(self):
        print(f"Anda telah masuk dalam akun {self.get_name()} sebagai BUYER")
        print()
        print(f"Selamat datang {self.get_name()}")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")
        print()

        cond = True
        while cond:
            print(f"Saldo anda {self.saldo},")
            perintah = input("Apa yang ingin anda lakukan? ")

            # jika perintah adalah LIHAT_SEMUA_PRODUK
            if perintah == "1":
                self.lihat_semua_produk()

            # jika perintah adalah BELI_PRODUK
            elif perintah == "2":
                self.beli_produk()

            # jika perintah adalah RIWAYAT_PEMBELIAN_SAYA
            elif perintah == "3":
                self.riwayat_pembelian()

            # jika perintah adalah LOG_OUT
            elif perintah == "4":
                print(f"Anda telah keluar dari akun {self.get_name()}")

                # maka cond di set menjadi False dan akan keluar dari loop
                cond = False
            print()
        

class Product() : 
    def __init__(self, nama, harga, stok, seller):
        self.__nama = nama
        self.__harga = harga
        self.stok = stok
        self.__seller = seller
    
    # method untuk mendapatkan nama produk
    def get_name(self):
        return self.__nama
    
    # method untuk mendapatkan harga produk
    def get_harga(self):
        return self.__harga

    # method untuk mendapatkan nama penjual produk
    def get_seller(self):
        return self.__seller



# method get_user dan get_product tidak perlu diubah, 
# silakan manfaatkan method ini untuk mendapatkan user dan produk yang dibutuhkan
def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None


list_user = []
list_product = []


def main():
    cond = True
    while cond:
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        pilih = input("Pilihan Anda: ")

        # jika pilihan adalah Sign Up
        if (pilih == "1") : 
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))

            print("Data akun: ")
            for i in range (banyak_user) : 
                data_user = input(str(i+1)+". ")
                template_uname = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
                flag = True

                data_user = data_user.split()
                tipe = data_user[0]

                # jika tipe user adalah SELLER
                if tipe == "SELLER":
                    uname = data_user[1]

                    # jika input user sesuai format (2 kata)
                    if len(data_user) == 2:

                        # untuk mengecek apakah username sudah sesuai dengan ketentuan karakter
                        for elem in uname:
                            if elem not in template_uname:
                                flag = False
                        
                        # jika username sesuai dengan ketentuan karakter
                        if flag:
                            pengguna = Seller(uname, tipe)
                            list_user.append(pengguna)

                        # jika username tidak sesuai dengan ketentuan karakter
                        else:
                            print("Akun tidak valid")

                    # jika input user tidak sesuai format (tidak 2 kata)
                    else:
                        print("Akun tidak valid")

                # jika tipe user adalah BUYER
                elif tipe == "BUYER":

                    # jika input user sesuai format (3 kata)
                    if len(data_user) == 3:
                        uname = data_user[1]
                        saldo = int(data_user[2])

                        # untuk mengecek apakah username sudah sesuai dengan ketentuan karakter
                        for elem in uname:
                            if elem not in template_uname:
                                flag = False

                        # jika username sudah sesuai dengan ketentuan karakter
                        if flag:

                            # jika saldo bukan bilangan bulat positif
                            if (type(saldo) != int) or (saldo <= 0):
                                print("Akun tidak valid")

                            # jika saldo bilangan bulat positif
                            else:
                                pengguna = Buyer(uname, tipe, saldo)
                                list_user.append(pengguna)
                        
                        # jika username tidak sesuai dengan ketentuan karakter
                        else:
                            print("Akun tidak valid")

                    # jika input user tidak sesuai format (tidak 3 kata)
                    else:
                        print("Akun tidak valid")

                # jika tipe selain SELLER dan BUYER
                else:
                    print("Akun tidak valid")
    
        # jika pilihan adalah log In
        elif (pilih == "2") : 
            user_name_login = input("user_name : ")
            user_logged_in = get_user(user_name_login, list_user)
            
            # jika input username ada di list_user
            try:
                if user_name_login == user_logged_in.get_name():
                    user_logged_in.menu()

            # jika input username tidak ada di list_user
            except:
                print(f"Akun dengan user_name {user_name_login} tidak ditemukan")

        # jika pilihan adalah Exit
        elif (pilih == "3") : 
            print("Terima kasih telah menggunakan Dekdepedia!")

            # maka cond di set menjadi False dan akan keluar dari loop
            cond = False
        print()

if __name__ == "__main__":
    main()
