from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3))
hunians.append(Rumah("Sekar MK", 5, 5))
hunians.append(Indekos("Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", 2, 4))
hunians.append(Indekos("Bp. Yogi", "Ananda Myzza"))

# Halaman daftar hunian akan tersembunyi sampai tombol di landing page ditekan.
root = Tk()
root.title("Latihan 9 DPBO 2023")
root.withdraw()

def open_main_page():
    root.deiconify()  # Menampilkan halaman daftar hunian.
    landing_page.destroy()  # Menghancurkan/destroy landing page.

# Membuat halaman landing page.
landing_page = Toplevel() # Menggunakan Toplevel() karena ingin menampilkan halaman yang independen dari root window (Halaman daftar hunian).
landing_page.title("Landing Page DPBO")

# Menambahkan foto pada landing page, tidak menggunakan library PIL karena gagal install librarynya.
image = PhotoImage(file="a-letter-logo-png-6.png")
image_label = Label(landing_page, image=image)
image_label.pack()

# Menambahkan tombol navigasi untuk pergi ke halaman daftar hunian.
button = Button(landing_page, text="Masuk ke Halaman Daftar Residen", command=open_main_page)
button.pack(padx=10, pady=10)

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Summary Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    d_summary = Label(d_frame, text=hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)


frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
