<img width="1179" height="891" alt="Cuplikan layar 2026-05-15 112018" src="https://github.com/user-attachments/assets/ca235816-d021-4211-9a12-6bb78c997177" />

<img width="927" height="815" alt="Cuplikan layar 2026-05-15 112038" src="https://github.com/user-attachments/assets/379d782a-a447-47eb-8a3b-755d4f601bb8" />

<img width="788" height="415" alt="Cuplikan layar 2026-05-15 112050" src="https://github.com/user-attachments/assets/6a65d050-6a36-44d3-af53-14cdfb909265" />

Line 1-3 mendefinisikan class `Node` beserta konstruktornya yang menerima satu parameter yaitu `data`. Setiap node memiliki dua atribut, yaitu `self.data` untuk menyimpan nilai sepatu dan `self.next` yang diinisialisasi `None` sebagai penunjuk ke node berikutnya di bawahnya.


Line 6-8 mendefinisikan class `TumpukanSepatu` beserta konstruktornya. Atribut `self.paling_atas` diinisialisasi `None` yang berarti tumpukan masih kosong saat pertama kali dibuat.


Line 10-11 mendefinisikan fungsi `kosong` yang mengembalikan nilai `True` jika `paling_atas` bernilai `None`, artinya tidak ada satu pun sepatu dalam tumpukan, dan `False` jika sebaliknya.


Line 13-17 mendefinisikan fungsi `tumpuk` yang menerima parameter `sepatu`. Fungsi ini membuat node baru, lalu menyambungkan `node_baru.next` ke node yang sebelumnya berada di paling atas, kemudian memindahkan `paling_atas` ke node baru tersebut sehingga sepatu terbaru selalu berada di posisi teratas tumpukan.


Line 19-25 mendefinisikan fungsi `ambil` yang mengambil sepatu dari posisi teratas. Jika tumpukan kosong maka fungsi mencetak peringatan dan berhenti. Jika tidak kosong, nama sepatu teratas disimpan sementara ke variabel `sepatu_dipakai`, lalu `paling_atas` digeser ke node di bawahnya sehingga sepatu teratas tadi terlepas dari tumpukan.


Line 27-31 mendefinisikan fungsi `lihat_teratas` yang hanya menampilkan nama sepatu di posisi paling atas tanpa mengambilnya. Jika tumpukan kosong maka fungsi mencetak peringatan dan berhenti lebih awal.


Line 33-41 mendefinisikan fungsi `tampilkan` yang menelusuri seluruh node dari atas ke bawah menggunakan variabel `current`. Setiap sepatu dicetak beserta nomornya, dan khusus untuk sepatu di urutan pertama ditambahkan label `← akan digunakan` sebagai penanda bahwa itulah sepatu yang akan dipakai.


Line 44-46 adalah awal fungsi `main` yang membuat objek `TumpukanSepatu` bernama `rak` dan menginisialisasi variabel `pilih` dengan nilai `0` sebagai nilai awal sebelum loop menu dimulai.


Line 48-57 menampilkan menu pilihan dan meminta input dari pengguna menggunakan `try-except`. Jika pengguna memasukkan bukan angka maka `ValueError` ditangkap, program mencetak pesan error dan langsung kembali ke awal loop dengan `continue`.


Line 59-72 adalah blok kondisi yang menjalankan fungsi sesuai pilihan pengguna. Pilihan 1 meminta nama sepatu lalu memanggil `tumpuk`, pilihan 2 memanggil `ambil`, pilihan 3 memanggil `lihat_teratas`, dan pilihan 4 memanggil `tampilkan`. Pilihan 5 mengosongkan seluruh tumpukan satu per satu menggunakan loop `while` sebelum program berhenti.


**Line 74-75** adalah blok yang memastikan fungsi `main` hanya berjalan jika file ini dijalankan langsung, bukan ketika diimpor sebagai modul di program lain.

Link yt : https://youtu.be/9-RrNeOAOiU
