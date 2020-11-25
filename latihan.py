# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 06:53:17 2020

@author: LENOVO i5
"""

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