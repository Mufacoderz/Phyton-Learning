print("===INTEGER===")
data_int = 9
print("data :", data_int, "bertipe data :", type(data_int))
      
data_float = float(data_int) #casting data int jadi float
data_str = str(data_int) 
data_bool = bool(data_int) 

print("data :", data_float, "bertipe data :", type(data_float))
print("data :", data_str, "bertipe data :", type(data_str))
print("data :", data_bool, "bertipe data :", type(data_bool))



print("===FLOAT===")
data_float = 9.8
print("data :", data_float, "bertipe data :", type(data_float))
      
data_int = int(data_float) #float ke int maka akan dibulatkan kebawah ex: 9.8 menjadi 9
data_str = str(data_float) 
data_bool = bool(data_float) #akan false jika floatnya 0

print("data :", data_int, "bertipe data :", type(data_int))
print("data :", data_str, "bertipe data :", type(data_str))
print("data :", data_bool, "bertipe data :", type(data_bool))