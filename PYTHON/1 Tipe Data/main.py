#tipe data integer = angka satuan
data_integer = 1
print("data :", data_integer, "bertipe data :", type(data_integer))

#tipe data desimal/float = angka dengan koma
data_float = 6.5
print("data :", data_float, "bertipe data :", type(data_float))

#tipe data string = "karakter"
name = "ucup"
print("Nama :", name, "bertipe data :", type(name))

#tipe data boolean = true false
data_bool = True
print("data :", data_bool, "bertipe data :", type(data_bool))

##tipe data khusus

# bilangan kompleks
data_complex = complex(5.6)
print("data :", data_complex, "bertipe data :", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char, c_long #dll

data_c_double = c_double(10.5)
print("data :", data_c_double, "bertipe data :", type(data_c_double))
