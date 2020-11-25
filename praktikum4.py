# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:47:21 2020

@author: LENOVO i5
"""

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

