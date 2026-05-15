class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TumpukanSepatu:
    def __init__(self):
        self.paling_atas = None

    def kosong(self):
        return self.paling_atas is None

    def tumpuk(self, sepatu):
        node_baru = Node(sepatu)
        node_baru.next = self.paling_atas
        self.paling_atas = node_baru
        print(f" Sepatu '{sepatu}' berhasil ditumpuk di atas!")

    def ambil(self):
        if self.kosong():
            print("  Tumpukan sepatu kosong, tidak ada yang bisa diambil!")
            return
        sepatu_dipakai = self.paling_atas.data
        self.paling_atas = self.paling_atas.next
        print(f" Sepatu '{sepatu_dipakai}' diambil dan siap digunakan!")

    def lihat_teratas(self):
        if self.kosong():
            print("  Tumpukan sepatu kosong!")
            return
        print(f" Sepatu paling atas (yang akan digunakan): '{self.paling_atas.data}'")

    def tampilkan(self):
        if self.kosong():
            print("  Tumpukan sepatu kosong!")
            return
        print("Tumpukan Sepatu (atas → bawah):")
        current = self.paling_atas
        urutan = 1
        while current is not None:
            label = " ← akan digunakan" if urutan == 1 else ""
            print(f"  {urutan}. {current.data}{label}")
            current = current.next
            urutan += 1


def main():
    rak = TumpukanSepatu()
    pilih = 0

    while pilih != 5:
        print("\n=== MENU ===")
        print("1. Tumpuk sepatu baru")
        print("2. Ambil sepatu teratas (untuk dipakai)")
        print("3. Lihat sepatu yang akan dipakai")
        print("4. Tampilkan semua tumpukan")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print(" Input tidak valid! Masukkan angka 1-5.")
            continue

        if pilih == 1:
            nama = input("Nama/jenis sepatu: ").strip()
            if nama:
                rak.tumpuk(nama)
            else:
                print(" Nama sepatu tidak boleh kosong!")
        elif pilih == 2:
            rak.ambil()
        elif pilih == 3:
            rak.lihat_teratas()
        elif pilih == 4:
            rak.tampilkan()
        elif pilih == 5:
            print("\nMembereskan rak sepatu...")
            while not rak.kosong():
                rak.ambil()
            print(" Semua sepatu telah dirapikan. Program selesai!")
        else:
            print(" Pilihan tidak valid! Masukkan angka 1-5.")


if __name__ == "__main__":
    main()