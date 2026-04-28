Program Sistem Kehadiran Mahasiswa

Deskripsi Singkat

Program ini merupakan program sistem pencatatan kehadiran mahasiswa sederhana berbasis menu, yang dapat digunakan untuk mengisi, menampilkan, mereset, dan melihat status kehadiran masing-masing mahasiswa. Program menggunakan struktur data list sebagai tempat penyimpanan status kehadiran, dan dictionary sebagai pemetaan kode status ke keterangan. List dipilih karena mendukung pengaksesan elemen berdasarkan index secara langsung, sehingga setiap slot dapat diidentifikasi melalui id() untuk melihat address memorinya.
<img width="862" height="52" alt="Cuplikan layar 2026-04-28 183633" src="https://github.com/user-attachments/assets/4c492a70-a0f2-4d1b-8813-34ccf3cedec8" />
Pada baris 1, dibuat list NAMA_MAHASISWA yang menyimpan nama-nama 5 mahasiswa secara berurutan. Pada baris 2, dibuat dictionary STATUS yang memetakan angka 0–4 ke keterangan status kehadiran, di mana 0 berarti belum diisi, 1 hadir, 2 sakit, 3 izin, dan 4 alpha.
<img width="713" height="174" alt="image" src="https://github.com/user-attachments/assets/e212af06-c646-456c-8337-881d2f8abb8b" />
Pada baris 5 didefinisikan fungsi menu() yang berfungsi menampilkan pilihan menu kepada pengguna. Baris 6–11 menampilkan 6 opsi menu, yaitu: melihat address list kehadiran, melihat address tiap slot, mengisi kehadiran semua mahasiswa, mereset kehadiran, melihat kehadiran mahasiswa tertentu, dan keluar dari program.
<img width="856" height="145" alt="image" src="https://github.com/user-attachments/assets/cd004722-a1d1-4563-a4b0-64b8f1e2e322" />
Pada baris 14 didefinisikan fungsi tampilkan_kehadiran(kehadiran) yang menerima parameter list kehadiran. Baris 15–16 menampilkan header tabel. Baris 17–19 melakukan perulangan untuk menampilkan nomor index, nama mahasiswa, dan status kehadirannya menggunakan format string yang rapi.
<img width="397" height="148" alt="image" src="https://github.com/user-attachments/assets/45a60df1-8f2a-4370-bce8-2c1ffd4cb677" />
Pada baris 22 didefinisikan fungsi main() sebagai fungsi utama program. Baris 23 menginisialisasi list kehadiran berisi 5 elemen bernilai 0, artinya semua mahasiswa awalnya berstatus "Belum diisi". Baris 24 menetapkan variabel running = True untuk menjaga perulangan tetap berjalan. Baris 26 memanggil fungsi menu() setiap iterasi agar pilihan selalu ditampilkan.
<img width="764" height="220" alt="image" src="https://github.com/user-attachments/assets/4e15e1c9-8240-489c-ac40-df601f77af91" />
Pilihan 1 menampilkan address memori dari list kehadiran secara keseluruhan menggunakan fungsi id(). Pilihan 2 menampilkan address memori dari setiap elemen (slot) dalam list satu per satu, disertai label nama mahasiswanya. Ini berguna untuk memahami bagaimana Python menyimpan data di memori.
<img width="781" height="289" alt="image" src="https://github.com/user-attachments/assets/7886b5fd-1be3-425d-94a8-74639a9248fc" />
Pilihan 3 menggunakan perulangan for untuk mengiterasi semua mahasiswa. Di dalamnya terdapat perulangan while True untuk memvalidasi input. Jika input tidak berada dalam rentang 1–4, program meminta input ulang. Jika valid, nilai disimpan ke kehadiran[i] dan perulangan dihentikan dengan break. Setelah semua selesai, tampilkan_kehadiran() dipanggil untuk menampilkan hasilnya.
<img width="737" height="111" alt="image" src="https://github.com/user-attachments/assets/cdb2c3c6-4fc2-4b40-9763-d5ac33a4edd4" />
Pilihan 4 mereset semua data kehadiran dengan membuat ulang list kehadiran berisi 5 elemen bernilai 0. Setelah direset, fungsi tampilkan_kehadiran() dipanggil untuk memperlihatkan bahwa semua status kembali menjadi "Belum diisi".
<img width="1083" height="267" alt="image" src="https://github.com/user-attachments/assets/f32c5c9e-6ec1-408a-88ed-f77212827040" />
Pilihan 5 meminta input index mahasiswa (0–4). Jika index valid, program menampilkan nama dan status kehadiran mahasiswa tersebut. Jika tidak valid, program meminta input ulang menggunakan while True. Ini memungkinkan pengguna melihat kehadiran satu mahasiswa secara spesifik tanpa harus menampilkan semua data.
<img width="716" height="155" alt="image" src="https://github.com/user-attachments/assets/30176d9f-6875-441c-a1e9-6b50cd29bf5a" />
Pilihan 6 mengubah nilai running menjadi False, sehingga perulangan while berhenti dan program berakhir.
<img width="513" height="228" alt="image" src="https://github.com/user-attachments/assets/6d994c9e-08db-413e-abfa-88b2a648ac81" />
Address List Kehadiran
Program menampilkan address memori dari objek list kehadiran secara keseluruhan
<img width="516" height="161" alt="image" src="https://github.com/user-attachments/assets/fb0a7895-0636-4396-b376-65c7d5a24b06" />
Address Tiap Slot
Program menampilkan address dari masing-masing elemen list. 
<img width="331" height="166" alt="image" src="https://github.com/user-attachments/assets/232554a1-0ded-40c1-a1b5-d84601310ab9" />
 Isi Kehadiran
User diminta mengisi status untuk Satria, Jaki, Dzakya, Riandra, dan Riva satu per satu. Setelah semua terisi, tabel kehadiran lengkap ditampilkan.
<img width="388" height="166" alt="image" src="https://github.com/user-attachments/assets/5a63c6fe-2018-4c75-a5f7-334f59e3c189" />
Reset Kehadiran
Setelah direset, semua mahasiswa kembali berstatus "Belum diisi" dan tabel ditampilkan ulang.
<img width="542" height="124" alt="image" src="https://github.com/user-attachments/assets/795f5982-bfcf-4d17-96df-c416614fd25d" />
Kehadiran Tertentu
User memasukkan index, misalnya 2, maka program menampilkan nama Dzakya beserta statusnya saja.

link youtube : https://youtu.be/_vtHVMWRqJA
