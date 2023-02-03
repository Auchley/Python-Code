

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

Celcius     = float(input("Masukan suhu dalam celcius degree"))
print("Suhu gunung everest adalah :",Celcius,"Celcius")

Fahreinheit = float(input("Masukan suhu dalam Fahreinheit degree"))
print("Suhu gunung everest adalah :",Fahreinheit,"Fahreinheit")

Reamur      = float(input("Masukan suhu dalam Reamur degree"))
print("Suhu gunung everest adalah :",Reamur,"Reamur")

Kelvin      = float(input("Masukan suhu dalam Kelvin degree"))
print("Suhu gunung everest adalah :",Kelvin,"Kelvin")

##Operasi dan Manipulasi String

# isalpha()   = Untuk mengecek semua huruf
# isalnum()   = Huruf dan Angka 
# isdecimal() = Angka saja
# isspace()   = Spasi, tab, newline \n
# istitle()  = Semua kata di mulai huruf besar (Proper)

judul = "The Truth Of Devil Side"
cek_judul = judul.istitle()
print(judul + " merupakan jenis film = " + str(cek_judul))


## Mengecek komponen Startswith + Endswith

## Penggabungan Komponen Join() Split()

pisah = ['aku','suka','kamu','hyunsuk']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = 'huhu'.join(pisah)
print(gabungan)

gabungan = 'akuhuhusukahuhukamuhuhuhyunsuk'
print(gabungan.split('huhu'))

## Alokasi Karakter = rjust(), ljust(), center()

kanan = "kanan".rjust(20,"=")
print("'"+kanan+"'")

kiri = "kiri".ljust(20,"=")
print("'"+kiri+"'")

tengah = "tengah".center(20,"=")
print("'"+tengah+"'")

# Kebalikannya = Strip()

kanan = kanan.strip("=")
print("'"+kanan+"'")

# Format String 

# String
nama = "Auchley"
format_str = f"Hai Cantik {nama}"
print(format_str)

# Boolean 
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka  = 1444.4
format_str = f"angka = {angka}"
print(format_str)

# Bilangan bulat 
angka = 20.5
format_str = f"bilangan bulat = {angka}"
print(format_str)

# Bilangan dengan ordo Ribuan
angka = 2000000000
format_str = f"Berapa jumlah angka dalam juta? {angka:,}"
print(format_str)

# Bilangan Decimal
angka = 2005.123456789
format_str = f"Berapa jumlah angka dalam decimal? {angka:.3f}"
print(format_str)

# Bilangan Decimal
angka = 2005.123456789
format_str = f"Berapa jumlah angka dalam decimal? {angka:.3f}"
print(format_str)

# Menampilkan Leading Zero
angka = 2005.123456789
format_str = f"Berapa jumlah angka dalam decimal? {angka:010.3f}"
print(format_str)

# Menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.12345
format_minus = f"Berapa jumlah angka dalam minus? {angka_minus:+d}"
format_plus = f"Berapa jumlah angka dalam plus? {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# Memformat Persen 
persentase = 0.085
format_persen = f"format persen nominal penjulan ini = {persentase:.1%}"
print(format_persen)

# Melakukan Operasi Aritmatika dalam kurung kurawal {}
harga = 500000
jumlah = 50
format_string = f"Jumlah total harga yang harus di bayar Auchley ialah {jumlah*harga:,}"
print(format_string)


# Format Angka Lain (Binary, Octal, Hexadecimal)

angka = 2008

format_binary      = f"binary = {bin(angka)}"
format_octal       = f"oct = {oct(angka)}"
format_hexadecimal = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)



























