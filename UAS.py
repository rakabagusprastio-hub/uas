# UAS.py
def header_invoice():
    print("\n" + "=" * 90)
    print("KRISHAND INDONESIA".center(90))
    print("Jakarta Selatan - Indonesia".center(90))
    print("=" * 90)
    print("I N V O I C E".center(90))
    print("=" * 90)

def input_data():
    global nama_barang, satuan, kuantum, harga_satuan, jumlah, ulang

    nama_barang = []
    satuan = []
    kuantum = []
    harga_satuan = []
    jumlah = []

    ulang = int(input("Masukkan jumlah jenis barang : "))

    for i in range(ulang):
        print(f"\nBarang ke-{i+1}")
        nama = input("Nama barang   : ")
        sat = input("Satuan        : ")
        qty = int(input("Kuantum       : "))
        harga = int(input("Harga satuan  : "))

        total = qty * harga

        nama_barang.append(nama)
        satuan.append(sat)
        kuantum.append(qty)
        harga_satuan.append(harga)
        jumlah.append(total)


def output_data():
    print("\nNo  Nama Barang        Satuan  Qty   Harga      Jumlah")
    print("-" * 90)

    sub_total = 0
    for i in range(ulang):
        print(f"{i+1:<3} {nama_barang[i]:<18} {satuan[i]:<7} {kuantum[i]:<5} {harga_satuan[i]:<10} {jumlah[i]}")
        sub_total += jumlah[i]

    print("-" * 90)

    ppn = sub_total * 0.10
    grand_total = sub_total + ppn

    print(f"Sub Total   : {sub_total}")
    print(f"PPN 10%     : {int(ppn)}")
    print(f"Grand Total : {int(grand_total)}")
    print("-" * 90)


while True:
    header_invoice()
    input_data()
    output_data()

    ulangi = input("\nBuat invoice lagi? (Y/T) : ").lower()
    if ulangi != "y":
        print("\nTerima kasih, program selesai.")
        break
