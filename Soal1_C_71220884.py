print("Menu")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
angkaper=int(input("Masukkan angka pertama :"))
angkaked=int(input("Masukkan angka kedua :"))
menu= input("Pilihan anda :")
if menu=="1" :
    Tambah= angkaper+angkaked
    print(Tambah)
elif menu=="2" :
    Kurang= angkaper-angkaked
    print(Kurang)
elif menu=="3" :
    Kali= angkaper*angkaked
    print(Kali)
elif menu=="4" :
    Bagi= angkaper/angkaked
    print(Bagi)
