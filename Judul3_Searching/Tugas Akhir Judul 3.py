def sequential_search_sentinel(data, n, target):
    data.append(target)
    i = 0
    counter = 0
    last_index = -1

    while i <= n:
        if data[i] == target:
            if i < n:
                counter += 1
                last_index = i
        i += 1

    data.pop()
    return counter, last_index


def main():
    data = [165, 170, 158, 172, 165, 180, 158, 165]
    n = len(data)
    print(f"Data tinggi badan: {data}")
    while True:
        try:
            target = int(input("Masukan tinggi badan yang ingin dicari (cm): "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")

    counter, last_index = sequential_search_sentinel(data, n, target)

    if counter > 0:
        print(f"Tinggi badan {target} cm ditemukan sebanyak {counter} kali, terakhir terlihat pada indeks ke-{last_index}.")
    else:
        print(f"Tinggi badan {target} cm tidak ditemukan.")


if __name__ == "__main__":
    main()