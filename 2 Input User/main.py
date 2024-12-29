
#data yg dimasukkan sudah pasti string
data_str = input("masukkan data: ")

print("data : ", data_str, "type =", type(data_str))


#jika ingin dirubah maka cukup di casting
data_int = int(input("masukkan angka: "))

print("data : ", data_int, "type =", type(data_int))


#boolean
data_bool = bool(int(input("masukkan nilai bool: ")))

print("data : ", data_bool, "type =", type(data_bool))