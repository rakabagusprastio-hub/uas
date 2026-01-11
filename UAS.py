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
    print("No   Nama Barang        Satuan   Kuantum   Harga Satuan     Jumlah")
    print("------------------------------------------------------------------------------------------")

    sub_total = 0
    for i in range(ulang):
        print(f"{i+1:<4} {nama_barang[i]:<18} {satuan[i]:<8} {kuantum[i]:<9} {harga_satuan[i]:<15} {jumlah[i]}")
        sub_total += jumlah[i]

    print("------------------------------------------------------------------------------------------")

    ppn = sub_total * 0.10
    grand_total = sub_total + ppn

    print(f"{'Sub Total':<80} {sub_total}")
    print(f"{'Discount':<80} 0")
    print(f"{'Total':<80} {sub_total}")
    print(f"{'PPN 10%':<80} {int(ppn)}")
    print(f"{'Grand Total':<80} {int(grand_total)}")

    print("------------------------------------------------------------------------------------------")
    print("Pembayaran mohon ditransfer ke rekening:")
    print("Bank BCA Cab. Sudirman")
    print("No. Rekening : 035-0123456")
    print("Atas Nama    : PT Krishand Indonesia\n")

    print("Hormat kami,")
    print("\n\n( Vonny Kusuma )")
    print("Manager Accounting")
    print("------------------------------------------------------------------------------------------")
print("No   Nama Barang        Satuan   Kuantum   Harga Satuan     Jumlah")
print("------------------------------------------------------------------------------------------")
# ================== CETAK ISI TABEL ==================
sub_total = 0
for i in range(ulang):
    print(f"{i+1:<4} {nama_barang[i]:<18} {satuan[i]:<8} {kuantum[i]:<9} {harga_satuan[i]:<15} {jumlah[i]}")
    sub_total += jumlah[i]

print("------------------------------------------------------------------------------------------")

# ================== HITUNG TOTAL ==================
ppn = sub_total * 0.10
grand_total = sub_total + ppn

print(f"{'Sub Total':<80} {sub_total}")
print(f"{'Discount':<80} 0")
print(f"{'Total':<80} {sub_total}")
print(f"{'PPN 10%':<80} {int(ppn)}")
print(f"{'Grand Total':<80} {int(grand_total)}")

print("------------------------------------------------------------------------------------------")
print("Pembayaran mohon ditransfer ke rekening:")
print("Bank BCA Cab. Sudirman")
print("No. Rekening : 035-0123456")
print("Atas Nama    : PT Krishand Indonesia\n")

print("Hormat kami,")
print("\n\n( Vonny Kusuma )")
print("Manager Accounting")
print("------------------------------------------------------------------------------------------")
header_invoice()
data = input_data()
output_data(*data)