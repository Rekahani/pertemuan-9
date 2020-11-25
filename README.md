# TUGAS PERTEMUAN 9 DAN PENJELASAN

## LIST, TUPLE, DAN DICTIONARY

**Nama : Reka Hani Latifah Nurhasanah

**Nim : 312010343

**Kelas : TI.20.A2

**Matkul : Bahasa Pemrograman



## TUGAS LATIHAN PADA PRAKTIKUM 4

#### SOAL

![5.png](/gambar/5.png)

### SYNTAX

berikut merupakan syntax untuk menampilkan program diatas

'''python

print(90*"=")

angka = [1, 5, 10, 15, 20]

print("Tampilkan semua elemen : ", angka) #print semua elemen

print("Tampilkan elemen 3 : ", angka[2]) #print elemen 3

print("Tampilkan elemen 2 sampai eleman 4 : ", angka[1:4]) #print elemen 2 sampai elemen 4

print("Tampilkan elemen terkahir : ", angka[4]) #print elemen terkahir/elemen ke 5

angka[3] = 12
print("Ubah elemen ke 4 : ", angka) #ubah elemen ke 4 dengan nilai lain

angka[3:5] = [20, 25]
print("Ubah elemen ke 4 sampai elemen terkahir : ", angka) #ubah elemen ke 4 sampai terkahir

print(90*"=")

listA = [2, 4, 6, 8, 10] #buat 2 variabel, list A dan list B
listB = [3, 5, 7, 9, 11] 

print("List A : ", listA)
print("List B : ", listB) #Tampilkan semua list

listB.extend(listA[0:2])
print("ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B) : ", listB) #ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)

listB.append("reka")
print("tambah list B dengan nilai string : ", listB) #tambah list B dengan nilai string

listB.extend([15, 17, 19])
print("tambah list B dengan 3 nilai : ", listB) #tambah list B dengan 3 nilai

listC = listA + listB
print("Gabungan list A dan list B : ", listC) #gabungkan list B dengan list A

print(90*"=")

#### OUTPUT

Dibawah ini merupakan hasil output dari syntax diatas

![4.png](/gambar/4.png)

## TUGAS PRAKTIKUM 4

### soal

![7.png](/gambar/7.png)

![6.png](/gambar/6.png)

#### SYNTAX

berikut merupakan syntax untuk menampilkan program diatas

'''python

x = 0
names = []
nim = []
tgs = []
uts = []
uas = []
akhir = []

while True :
    nama = input ("nama : ")
    names.append(nama)
    Nim = input ("nim : ")
    nim.append(Nim)
    tugas = input ("tugas : ")
    tgs.append(tugas)
    UTS = input ("UTS : ")
    uts.append(UTS)
    UAS = input ("UAS : ")
    uas.append(UAS)
    Akhir = (int(tugas)* .30) + (int(UTS)* .35) + (int(UAS)* .35)
    akhir.append(Akhir)
    
    data =''
    while data !='y'and data !='t':
        data = input("Tambah Data (y/t)? ")
        
    x += 1
    if data =='t':
        break

print("======================================================================")
print("| NO |     NAMA      |      NIM      |    UTS    |   UAS    |   AKHIR  |")
print("======================================================================")

for n in range(x):
    print("|",n+1,"|",names[n],"|",nim[n],"|",uts[n],"|",uas[n],"|",akhir[n],"|")

#### OUTPUT

Dibawah ini merupakan hasil output dari syntax diatas

![3.png](/gambar/3.png)

## TUGAS PRAKTIKUM 5

#### SOAL

![8.png](/gambar/8.png)

#### SYNTAX

berikut merupakan syntax untuk menampilkan program diatas

#inisialisasi
daftarKontak = {"Nama":"Nomer Telpon"}
kontak       = {'Ari':'081267888', 'Dina' : '087677776'}

#print
print(30*"-")
print("    Nama    |  Nomor Telepon  ") #prinr daftarkontak
print(30*"-")
print("    Ari     | ", kontak['Ari']) #print kontak Ari
print("    Dina    | ", kontak['Dina']) #print kontak Dina
print(90*"-")

#Tampilkan kontaknya Ari
print("Tampilkan kontaknya Ari")
print("    Ari     | ", kontak['Ari']) #print kontak Ari
print(90*"-")

#Tambah kontak baru dengan nama Riko, nomor 087654544
print("Tambah kontak baru dengan nama Riko, nomor 087654544")
kontak['Riko'] = '087654544'
print("    Riko    | ", kontak['Riko'])
print(90*"-")

#Ubah kontak Dina dengan nomor baru 088999776
print("Ubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print("    Dina    | ", kontak['Dina'])
print(90*"-")

#Tampilkan semua Nama
print("Tampilkan semua Nama")
print(kontak.keys())
print(90*"-")

#Tampilkan semua Nomor
print("Tampilkan semua Nomor")
print(kontak.values())
print(90*"-")

#Tampilkan daftar Nama dan nomornya
print("Tampilkan daftar Nama dan nomornya")
print(kontak.items())
print(90*"-")

#Hapus kontak Dina
print("Hapus kontak Dina")
kontak.pop('Dina')
print(kontak.items())
print(90*"-")

#OUTPUT

Dibawah ini merupakan hasil output dari syntax diatas

![9.png](/gambar/9.png)

