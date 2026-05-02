def tukar(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Jumlah makanan: "))
    except ValueError:
        print("Input tidak valid!")
        return

    makanan = []
    for i in range(n):
        nama = input(f"Nama makanan ke-{i+1}: ")
        while True:
            try:
                lemak = float(input(f"Kandungan lemak {nama} (gram): "))
                break
            except ValueError:
                print("Masukkan angka!")
        makanan.append((nama, lemak))

    print("\nSebelum diurutkan:")
    for m in makanan:
        print(f"  {m[0]}: {m[1]}g")

    bubble_sort(makanan, n)

    print("\nSetelah diurutkan (lemak terkecil → terbesar):")
    for i, m in enumerate(makanan, 1):
        print(f"  {i}. {m[0]}: {m[1]}g")


if __name__ == "__main__":
    main()