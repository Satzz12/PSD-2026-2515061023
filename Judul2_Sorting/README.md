<img width="1001" height="902" alt="Cuplikan layar 2026-05-02 145004" src="https://github.com/user-attachments/assets/7bf473f2-65fd-456a-9ea1-9007963e8a1a" />
<img width="815" height="222" alt="Cuplikan layar 2026-05-02 145029" src="https://github.com/user-attachments/assets/b6e5f337-15cd-4da6-a17d-af234db48fd5" />

Line 1-3 mendefinisikan fungsi tukar yang bertugas menukar posisi dua elemen dalam list. Fungsi ini menerima tiga parameter yaitu array, indeks i, dan indeks j, lalu menukar nilai pada posisi i dan j secara langsung tanpa variabel sementara.

Line 6-10 mendefinisikan fungsi bubble_sort yang berisi dua loop bersarang. Loop luar mengontrol jumlah putaran sebanyak n-1 kali, sedangkan loop dalam membandingkan dua elemen yang bersebelahan. Jika kandungan lemak elemen kiri lebih besar dari elemen kanan, maka fungsi tukar dipanggil untuk membalik posisi keduanya.

Line 13-17 adalah awal fungsi main yang meminta pengguna memasukkan jumlah makanan. Jika input bukan angka maka akan masuk ke blok except, menampilkan pesan error, dan program langsung berhenti.

Line 19-27 adalah bagian pengumpulan data makanan. Program mengulang sebanyak n kali untuk meminta nama makanan dan kandungan lemaknya. Khusus untuk input lemak digunakan loop while True agar program terus meminta ulang jika pengguna memasukkan bukan angka. Setiap pasangan nama dan lemak kemudian disimpan ke dalam list makanan sebagai tuple.

Line 29-31 menampilkan daftar makanan sebelum diurutkan dengan mengakses m[0] untuk nama dan m[1] untuk kandungan lemak.

Line 33 memanggil fungsi bubble_sort untuk mengurutkan list makanan.

Line 35-37 menampilkan daftar makanan setelah diurutkan dari lemak terkecil ke terbesar, lengkap dengan nomor urut yang dimulai dari angka 1 menggunakan enumerate.

Line 40-41 adalah blok yang memastikan fungsi main hanya berjalan jika file ini dijalankan langsung, bukan ketika diimpor sebagai modul di program lain.

link yt : https://youtu.be/APpknQpRG1Q

