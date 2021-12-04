import tkinter as ttk
import tkinter.messagebox as tkmsg

L_CODE = ("0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011")
G_CODE = ("0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111")
R_CODE = ("1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100")

# ================= BARCODE =================
class Barcode:
    def __init__(self, number):
        self.number = number
        self.first_digit = int(number[0]) #integer
        self.first_group = number[1:7] #string
        self.second_group = number[7:] + self.check_digit() #string

        self.first_pattern = self.make_first() #list of sequence
        self.second_pattern = self.make_second() #list of sequence
    
    def check_digit(self):
        checksum = 0
        number = self.number
        for i in range(len(number)):
            if (i+1)%2 == 0:
                checksum += int(number[i]) * 3
            else:
                checksum += int(number[i])
        x = checksum % 10
        check_digit = x
        if x != 0:
            check_digit = 10 - x
        return str(check_digit)
    
    def make_second(self):
        second_pattern = []
        for angka in self.second_group:
            second_pattern.append(R_CODE[int(angka)])
        return second_pattern

    def make_first(self):
        first_pattern = []
        panjang = len(self.first_group)

        if self.first_digit == 0: #LLLLLL
            for angka in self.first_group:
                first_pattern.append(L_CODE[int(angka)])

        elif self.first_digit == 1: #LLGLGG
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==1) or (i==3):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 2: #LLGGLG
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==1) or (i==4):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 3: #LLGGGL
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==1) or (i==5):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 4: #LGLLGG
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==2) or (i==3):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 5: #LGGLLG
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==3) or (i==4):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 6: #LGGGLL
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==4) or (i==5):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 7: #LGLGLG
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==2) or (i==4):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        elif self.first_digit == 8: #LGLGGL
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==2) or (i==5):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])

        else: #LGGLGL
            for i in range(panjang):
                angka = int(self.first_group[i])
                if (i==0) or (i==3) or (i==5):
                    first_pattern.append(L_CODE[angka])
                else:
                    first_pattern.append(G_CODE[angka])
        return first_pattern
    
    def make_barcode(self, param, lst1, lst2):
        param.canvas.create_text(155, 80, text="EAN-13 Barcode:", fill="black", font="Helvetica 15 bold")

        # barcode
        lebar = 300
        tinggi = 350
        kiri = lebar/2 - 90
        param.canvas.create_line(kiri,tinggi/2 - 60, kiri, tinggi/2 + 68, width=2, fill="blue")
        param.canvas.create_line(kiri+2,tinggi/2 - 60, kiri+2, tinggi/2 + 68, width=2, fill="")
        param.canvas.create_line(kiri+4,tinggi/2 - 60, kiri+4, tinggi/2 + 68, width=2, fill="blue")
        kiri += 6
        for sublst in lst1:
            for elem in sublst:
                if elem == "1":
                    param.canvas.create_line(kiri, tinggi/2 - 60, kiri, tinggi/2 + 60, width=2, fill="green")
                else:
                    param.canvas.create_line(kiri, tinggi/2 - 60, kiri, tinggi/2 + 60, width=2, fill="")
                kiri += 2
        param.canvas.create_line(kiri,tinggi/2 - 60, kiri, tinggi/2 + 68, width=2, fill="")
        param.canvas.create_line(kiri+2,tinggi/2 - 60, kiri+2, tinggi/2 + 68, width=2, fill="blue")
        param.canvas.create_line(kiri+4,tinggi/2 - 60, kiri+4, tinggi/2 + 68, width=2, fill="")
        param.canvas.create_line(kiri+6,tinggi/2 - 60, kiri+6, tinggi/2 + 68, width=2, fill="blue")
        param.canvas.create_line(kiri+8,tinggi/2 - 60, kiri+8, tinggi/2 + 68, width=2, fill="")
        kiri += 10
        for sublst in lst2:
            for elem in sublst:
                if elem == "1":
                    param.canvas.create_line(kiri, tinggi/2 - 60, kiri, tinggi/2 + 60, width=2, fill="green")
                else:
                    param.canvas.create_line(kiri, tinggi/2 - 60, kiri, tinggi/2 + 60, width=2, fill="")
                kiri += 2
        param.canvas.create_line(kiri,tinggi/2 - 60, kiri, tinggi/2 + 68, width=2, fill="blue")
        param.canvas.create_line(kiri+2,tinggi/2 - 60, kiri+2, tinggi/2 + 68, width=2, fill="")
        param.canvas.create_line(kiri+4,tinggi/2 - 60, kiri+4, tinggi/2 + 68, width=2, fill="blue")
        
        # angka di bawah barcode
        param.canvas.create_text(50, 250, text=self.first_digit, font="Helvetica 14 bold")
        kiri = 75
        for angka in self.first_group:
            param.canvas.create_text(kiri, 250, text=angka, font="Helvetica 14 bold")
            kiri += 13
        kiri = 165
        for angka in self.second_group:
            param.canvas.create_text(kiri, 250, text=angka, font="Helvetica 14 bold")
            kiri += 13
        
        # check digit
        param.canvas.create_text(155, 300, text=f"Check Digit: {self.check_digit()}", fill="orange", font="Helvetica 14 bold")


# ================== CONTAINER ====================
class MyApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.number = ttk.StringVar()
        self.name = ttk.StringVar()
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.label_name = ttk.Label(self, text="Save barcode to PS file [eg: EAN13.eps]:", font="Helvetica 12 bold")
        self.entry_name = ttk.Entry(self, textvariable=self.name)
        self.label_code = ttk.Label(self, text="Enter code (first 12 decimal digits):", font="Helvetica 12 bold")
        self.entry_code = ttk.Entry(self, textvariable=self.number)
        self.canvas = ttk.Canvas(self, width=300, height=350, bg="white")
        self.entry_code.bind("<Return>", self.build_barcode)
        self.label_name.grid()
        self.entry_name.grid(pady=4)
        self.label_code.grid()
        self.entry_code.grid(pady=6)
        self.canvas.grid(pady=20)
    
    def get_name(self):
        return self.name.get()
    def get_number(self):
        return self.number.get()

    def build_barcode(self, event):
        if len(self.get_number()) != 12:
            tkmsg.showerror("Wrong input!", "Please enter correct input code.")
            self.name.set("")
            self.number.set("")
        else:
            barcode = Barcode(self.get_number())
            barcode.make_barcode(self, barcode.first_pattern, barcode.second_pattern)
            self.save_file()

    def save_file(self):
        file_name = self.get_name()
        if (len(file_name)>4 and file_name.endswith(".eps")) or (len(file_name)>3 and file_name.endswith(".ps")):
            self.canvas.postscript(file=self.get_name())
        else:
            tkmsg.showerror("Wrong file name", "Please enter correct file name.")
        

def main():
    app = MyApp()
    app.master.title("EAN-13")
    app.master.geometry("400x500")
    app.master.mainloop()

if __name__ == "__main__":
    main()
