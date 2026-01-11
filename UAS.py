def header_invoice():
    print("KRISHAND INDONESIA")
    print("Jakarta Selatan - Indonesia")
    print("------------------------------------------------------------------------------------------")
    print("                                 I N V O I C E                                            ")
    print("Kepada Yth.                                               No.             :FT./003/01/2008 ")
    print("PT ISM BOGOSARI FLOUR JAKARTA                             Tanggal         :30/01/2008      ")
    print("Jl. Raya Cilincing, Tanjung Priok                         Mata uang       :IDR             ")
    print("Jakarta Utara - 14110                                     No. PO          :PO-0001/01/2008 ")
    print("                                                          Tgl.PO          :25/01/2008      ")
    print("                                                          Tgl Jatuh Tempo :13/02/2008      ")
    print("------------------------------------------------------------------------------------------")

def input_data():
    global nama_barang, satuan, kuantum, harga_satuan, jumlah, ulang

    # LIST DATA
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