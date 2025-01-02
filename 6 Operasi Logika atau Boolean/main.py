print('===NOT===')
a = True
c = not a
print('data a =', a)
print('---------------NOT')
print('data c =', c)



print('===OR===') #jika salah satu true maka outputnya true
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, " =", c)
a = True
b = False
c = a or b
print(a, " OR", b, "=", c)
a = True
b = True
c = a or b
print(a, " OR", b, " =", c)



print('===AND===') #jika keduanya true baru hasilnya true
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, " =", c)
a = True
b = False
c = a and b
print(a, " AND", b, "=", c)
a = True
b = True
c = a and b
print(a, " AND", b, " =", c)

print('===XOR===') #jika salah satuu true maka hasilnya true
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)
a = True
b = False
c = a ^ b
print(a, " XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, " XOR", b, " =", c)

