makanan = input('masukan nama makan') # "sushi"

makanan_tersedia = ["pizza", "sushi", "burger"]

print(f"makanan yang dimasukan {makanan}")
if makanan in makanan_tersedia:
    print("tersedia")
else:
    print("tidak ada di menu")

