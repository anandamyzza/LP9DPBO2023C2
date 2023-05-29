## Janji
Saya Ananda Myzza Marhelio NIM 2100702 mengerjakan soal Latihan 9 dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Deskripsi Tugas Latihan 9 DPBO 2023
Latihan Praktikum tidak menggunakan Database, tapi harus mengirim bukti screenshot menjalankan contoh kode yang dikirim.
Spesifikasi:
1. Lengkapi fitur summary
2. Buat landing Page (button yg ngarah ke halaman daftar residen)
3. Tampilin gambar
4. Tambahin 1 metode yang masih relevan untuk setiap kelas

## Desain Program
Terdapat 4 class di program ini, yaitu:
1. **Class Hunian** memiliki 3 atribut yaitu jenis (Jenis Hunian), jml_penghuni, dan jml_kamar.
2. **Class Apartemen** merupakan __child__ dari class **Hunian**. Class ini memiliki 3 atribut yaitu nama_pemilik, jml_penghuni, dan jml_kamar.
3. **Class Rumah** merupakan __child__ dari class **Hunian**. Class ini memiliki 3 atribut yaitu nama_pemilik, jml_penghuni, dan jml_kamar.
4. **Class Indekos** merupakan __child__ dari class **Hunian**. Class ini memiliki 2 atribut yaitu nama_pemilik, dan nama_penghuni.

## Alur Program
1. Pengguna akan dihadapkan dengan landing page saat menjalankan program ini. Pada halaman ini terdapat gambar logo dan tombol yang akan menavigasikan pengguna ke halaman daftar hunian apabila menekannya.
2. Jika pengguna menekan tombol di landing page, maka pengguna akan dihadapkan dengan halaman daftar hunian. Pada halaman ini terdapat data tabel hunian yang ada.
3. Terdapat tombol "Details" pada setiap baris pada kolom hunian, pengguna akan dihadapkan ke halaman detail summary data residen yang dipilih jika pengguna menekan tombol detail.
4. Pada halaman detail, pengguna dapat melihat detail summary tentang hunian yang dipilih, serta ada tombol "Close" untuk menutup window detail tersebut.
5. Kembali kepada halaman daftar hunian, terdapat tombol "Exit" yang akan menutup program ini jika pengguna menekannya.

## Dokumentasi
https://github.com/anandamyzza/LP9DPBO2023C2/assets/100767177/6cc7b2e1-4d84-43de-bb44-b0e40eb9efdb

Screenshots ada pada folder yang sudah disediakan di repositori ini.

### Dokumentasi Mencoba DB
![image](https://cdn.discordapp.com/attachments/771791679165431808/1111950602814107749/image.png)
![image](https://cdn.discordapp.com/attachments/771791679165431808/1111950648678809641/image.png)
![image](https://github.com/anandamyzza/LP9DPBO2023C2/assets/100767177/c71ad94b-43e8-4918-8c6a-f76656ecb39b)
![image](https://github.com/anandamyzza/LP9DPBO2023C2/assets/100767177/e3efe54e-b151-4c46-b8ca-db7cb891a53e)
