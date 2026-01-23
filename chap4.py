# Type casting means converting a value from one data type to another.

# .in simple definition 
# When you change the type of data (like number → string, string → number), that is called type casting.

# Why do we need type casting?
# To perform correct calculations
# To compare values properly
# To store data in the required format
# To avoid errors


# String → Integer
x = "10"
y = int(x)

print(y)
print(type(y))   # <class 'int'>



# Integer → String
x = 100
y = str(x)

print(y)
print(type(y))   # <class 'str'>


# Integer → Float
x = 5
y = float(x)

print(y)         # 5.0


# Float → Integer
x = 9.8
y = int(x)

print(y)         # 9 (decimal part removed)


# String → Float
x = "12.5"
y = float(x)

print(y)

# Boolean Casting
print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool("Hello")) # True
