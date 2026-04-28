NAMA_MAHASISWA = ["Satria", "Jaki", "Dzakya", "Riandra", "Riva"]
STATUS = {0: "Belum diisi", 1: "Hadir", 2: "Sakit", 3: "Izin", 4: "Alpha"}


def menu():
    print("SISTEM KEHADIRAN MAHASISWA")
    print("1. Tampilkan address daftar kehadiran")
    print("2. Tampilkan address dari semua slot kehadiran")
    print("3. Isi kehadiran semua MAHASISWA")
    print("4. Reset semua kehadiran")
    print("5. Lihat kehadiran MAHASISWA tertentu")
    print("6. Keluar")


def tampilkan_kehadiran(kehadiran):
    print("\nDaftar Kehadiran")
    print(f"{'No':<5} {'Nama':<12} {'Status'}")
    for i in range(5):
        print(f"{i:<5} {NAMA_MAHASISWA[i]:<12} {STATUS[kehadiran[i]]}")


def main():
    kehadiran = [0] * 5
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print(f"\nAddress daftar kehadiran: {id(kehadiran)}")

        elif choice == 2:
            print("\nAddress setiap slot kehadiran:")
            print(f"{'Slot':<30} {'Address'}")
            for i in range(5):
                label = f"kehadiran[{i}] ({NAMA_MAHASISWA[i]})"
                print(f"{label:<30} {id(kehadiran[i])}")

        elif choice == 3:
            print("\n Isi kehadiran untuk semua mahasiswa:")
            print("Status: 1=Hadir  2=Sakit  3=Izin  4=Alpha")
            for i in range(5):
                while True:
                    try:
                        print(f"\nMahasiswa: {NAMA_MAHASISWA[i]}")
                        nilai = int(input("Status (1/2/3/4): "))
                        if nilai in (1, 2, 3, 4):
                            kehadiran[i] = nilai
                            print(f" Tercatat: {STATUS[nilai]}")
                            break
                        else:
                            print("Status tidak valid! Masukkan angka 1-4.")
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka!")

            print("\nKehadiran berhasil diisi!")
            tampilkan_kehadiran(kehadiran)

        elif choice == 4:
            kehadiran = [0] * 5
            print("\nSemua kehadiran mahasiswa telah direset.")
            tampilkan_kehadiran(kehadiran)

        
        elif choice == 5:
            print("\nDaftar mahasiswa:")
            for i in range(5):
                print(f"  {i} = {NAMA_MAHASISWA[i]}")
            while True:
                try:
                    index = int(input("\nMasukkan index mahasiswa yang ingin dilihat (0-4): "))
                    if 0 <= index < 5:
                        print(f"\n--- Hasil ---")
                        print(f"Mahasiswa  : {NAMA_MAHASISWA[index]}")
                        print(f"Status : {STATUS[kehadiran[index]]}")
                        break
                    else:
                        print("Index tidak valid, silakan masukkan index antara 0-4.")
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")

        elif choice == 6:
            print("\nProgram selesai. Sampai jumpa!")
            running = False

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()