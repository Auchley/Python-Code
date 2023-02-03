

#TIPE DATA 
#Data Integer : Angka satuan yang gak ada komanya
Data_integer = 11
print ("data :", Data_integer)
print ("-bertipe :", type (Data_integer))

#Data Float : Angka dengan koma 
Data_float = 1.9
print("data :", Data_float)
print("data :", type (Data_float))

#Data String : Kumpulan Karakter 
Data_string = "Asahi"
print("data :", Data_string)
print("data :", type(Data_string))

#Data Boolean : Biner (True/False)
Data_bool = True
print("data :", Data_bool)
print("data :", type(Data_bool))



#CASTING TYPE DATA : Merubah satu tipe ke tipe yang lainnya
#Gunakan sesuai dengan kebutuhan
data_int = 100;
print("data =", data_int, "type = ", type(data_int))

data_float = float(data_int)
print("data =", data_float, "type = ", type(data_float))

data_str = str(data_int)
print("data =", data_str, "type = ", type(data_str))

data_bool = bool(data_int) # akan false jika nilai int = 0 
print("data =", data_bool, "type = ", type(data_bool))



#MENGAMBIL INPUT DATA DARI USER : Data yang di masukan pasti string
data = input("Masukan code data anda: ")
print("data =", data, "type =", type(data))

data_int = int(input("Masukan kode angka :"))
print("data =", data_int, "type =", type(data_int))

#Mengetahui data boolean maka pindahkan dlu ke data_int = Untuk menemukan True/False
#Data Boolean = Biner 
biner = bool(int(input("Masukan nilai boolean: ")))
print("data =", biner, "type =", type(biner))



#OPERASI ARITMATIKA
a = 10
b = 3
#Operasi Tambah +
hasil = a + b
print(a, "+",b,"=",hasil)

#Operasi Pengurangan -
hasil = a - b
print(a, "-",b,"=",hasil)

#Operasi Perkalian *
hasil = a * b
print(a, "*",b,"=",hasil)

#Operasi Pembagian /
hasil = a / b
print(a, "/",b,"=",hasil)

#Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a, "**",b,"=",hasil)

#Operasi Modulus (Sisa hasil pembagian) %
hasil = a % b
print(a, "%",b,"=",hasil)

#Operasi Floor Division (Pembagian double) // #kebalikan modulus (Hasil di bulatkan ke bawah)
hasil = a // b
print(a, "//",b,"=",hasil)


#Prioritas Operasi, Operational Precedence
#Urutan perhitungan
'''
    1. ()
    2. Exponen **
    3. Perkalian dsb * / ** % //
    4. Pertambahan dan pengurangan + -
'''
x = 9
y = 8
z = 7

hasil = x ** y + z * y // y % x
print (x,"**",y,"+", z,"*", y,"//", y,"%", x,"=",hasil)

#Latihan Perhitungan Program Sederhana

#1. Latihan Konversi Satuan Temperature
#Celcius
#Fahreinheit
#Reamur
#Kelvin

#Program Konversi Celcius ke satuan lain

print ("\n PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius degree"))
print("Suhu gunung everest adalah :",celcius,"celcius")

#Operasi Komparasi (Perbandingan)
#Setiap hasil dari komparasi adalah boolean 








