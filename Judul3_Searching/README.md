<img width="1848" height="849" alt="Cuplikan layar 2026-05-08 171741" src="https://github.com/user-attachments/assets/5c476ca2-c5f2-4ec2-aa88-a120d0c71cd0" />

<img width="1817" height="100" alt="Cuplikan layar 2026-05-08 171755" src="https://github.com/user-attachments/assets/259fc80f-88d9-4d27-95b0-9d4161eba207" />


Line 1-3 mendefinisikan fungsi sequential_search_sentinel yang menerima tiga parameter yaitu data berupa list, n sebagai panjang data, dan target sebagai nilai yang ingin dicari. Langkah pertama fungsi ini adalah menambahkan target ke bagian akhir list sebagai sentinel, yaitu sebuah teknik untuk memastikan loop pasti berhenti karena nilai target dijamin ada di dalam list.


Line 4-6 menginisialisasi tiga variabel. Variabel i sebagai penunjuk indeks dimulai dari 0, counter sebagai penghitung kemunculan target dimulai dari 0, dan last_index yang diset ke -1 sebagai penanda bahwa target belum ditemukan.


Line 8-12 adalah loop utama yang berjalan dari indeks 0 hingga n secara inklusif. Di setiap langkah program mengecek apakah elemen pada posisi i sama dengan target. Jika cocok dan posisi i masih dalam batas data asli yaitu kurang dari n, maka counter bertambah satu dan last_index diperbarui ke posisi saat ini. Pengecekan i kurang dari n bertujuan untuk mengabaikan sentinel yang ditambahkan di posisi n.


Line 14-15 menghapus sentinel dari list setelah loop selesai agar data kembali ke kondisi semula, kemudian mengembalikan dua nilai yaitu counter dan last_index.


Line 18-19 adalah awal fungsi main yang mendefinisikan data tinggi badan secara langsung dan menghitung panjangnya menggunakan len.


Line 21-26 meminta input target dari pengguna menggunakan loop while True. Jika pengguna memasukkan bukan angka maka program menangkap ValueError dan meminta input ulang, loop baru berhenti ketika input valid berhasil dimasukkan.


Line 28 memanggil fungsi sequential_search_sentinel dengan data, n, dan target sebagai argumen, lalu menyimpan dua nilai kembaliannya ke dalam counter dan last_index.


Line 30-33 menampilkan hasil pencarian. Jika counter lebih dari 0 maka program menampilkan berapa kali target ditemukan beserta indeks terakhir kemunculannya. Jika counter bernilai 0 maka program menampilkan pesan bahwa target tidak ditemukan.


Line 36-37 adalah blok yang memastikan fungsi main hanya berjalan jika file ini dijalankan langsung, bukan ketika diimpor sebagai modul di program lain.

link yt:https://youtu.be/6JXUMgD0Kxw
