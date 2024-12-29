# latihan konversi satuan temperature

#celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE")
7
celcius=float(input('masukkan suhu dalam celcius : '))
print("suhu adalah", celcius, "Celcius")

#reamur
reamur = (4/5) *celcius
print("suhu dalam reamur adalah ", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) *celcius) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, "Kelvin")


#PR
#Fahrenheit ke Kelvin
fahrenheitInput = float(input("masukkan suhu dalam fahrenheit : "))
convertCelcius = (5/9) * (fahrenheitInput - 32)
convertKelvin = convertCelcius + 273.15
print("suhu fahrenheit adalah ",fahrenheitInput,"  dan dalam satuan kelvin adalah ", convertKelvin, "Kelvin")