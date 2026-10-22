data_product = {
    1: "Laptop         ",
    2: "Monitor        ",
    3: "Keyboard       ",
    4: "Mouse          ",

    5: "Charger Laptop"
}
daftar_harga = {
    1: 20000000,
    2: 600000,
    3: 300000,
    4: 100000,
    5: 200000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1: "Transfer Bank",
    2: "Virtual Account",
    3: "Cash on Delivery",
    4: "Kartu Kredit"
}
print("==========List Product==========")
for i in data_product:
    print("Id Product : ",i, "\t Nama Product : ",data_product[i], "\t Harga Product : ",daftar_harga[i])
pilih_id = int(input("Pilih Id Product: "))
if pilih_id in data_product :
    pilih_beli = input("Ingin Beli ? (Y/N)")
    if pilih_beli == "y" or pilih_beli == "Y" :
        nama_penerima     = input ("Nama Penerima    : ")
        alamat_penerima   = input ("Alamat Penerima  : ")
        telepon           = input ("No HP            : ")
        kurir_pengiriman = input ("Kurir Pengiriman : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "No Hp":telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "product_id":data_product
        }
    else:
        pass
    if len (dict_trx) > 0 :
        ("========== Metode Pembayaran ==========")
    for i in daftar_metode_pembayaran:
        print("Id : ", i, "\t Metode Pembayaran : ",daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih ID Metode Pembayaran :"))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : ", dict_trx["nama penerima"])
        print("Alamat Penerima : ", dict_trx["alamat penerima"])
        print("No Hp : ", dict_trx["No Hp"])
        print("Kurir Pengiriman : ", dict_trx["Kurir Pengiriman"])
        print("Product : ", data_product[pilih_id])
        print("Harga : ", daftar_harga[pilih_id])
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah anda yakin ingin melakukan pembayarab ? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y" :
            print("Anda sudah berhasi melakukan pembayaran")
        else:
            pass
    else:
        print("Id metode pembayaran tidak tersedia")
else:
    print("Id Product tidak tersedia")

        



