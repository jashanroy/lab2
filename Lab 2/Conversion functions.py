#Conversion functions
x = 10.5
print(type(x))
print("x =", x)
x = int(x)
print("x =", x)
x = "Hello"
y= 14
z = 12.5
print(type(x))
print(type(y))
print(type(z))
result = y + z
print(result)
print(type(result))
result = y + int(z)
print(result)
print(type(result))
result = z + float(y)
print(result)
print(type(result))
print(type(str(z)))
result = x + str(y) + str(z)
print(result)
result = x + str(y)
print(result)