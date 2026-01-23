# Arithmetic Operators

# Used for mathematical calculations.
# +	Addition	a + b
# -	Subtraction	a - b
# *	Multiplication	a * b
# /	Division	a / b
# %	Modulus (remainder)	a % b
# **	Exponent (power)	a ** b
# //	Floor division	a // b
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3





# Assignment Operators

# Used to assign values.

# Operator	Example	Same As
# =	a = 5	assign
# +=	a += 2	a = a + 2
# -=	a -= 2	a = a - 2
# *=	a *= 2	a = a * 2
# /=	a /= 2	a = a / 2
# %=	a %= 2	a = a % 2
# **=	a **= 2	a = a ** 2
# //=	a //= 2	a = a // 2
a = 10
a += 5
print(a)  # 15




# Comparison (Relational) Operators

# Used to compare values → result is True or False.

# Operator	Meaning
# ==	Equal
# !=	Not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal
# <=	Less than or equal
# a = 10
# b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False


# Logical Operators

# Used with conditions.

# Operator	Meaning
# and	Both true
# or	Any one true
# not	Reverse result
a = 10
b = 5

print(a > 5 and b < 10)  # True
print(a > 15 or b < 10) # True
print(not(a > 5))       # False











# Bitwise Operators



# Operator	Name
# &	AND
# `	`
# ^	XOR
# ~	NOT
# <<	Left shift
# >>	Right shift
a = 5   # 0101
b = 3   # 0011

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
print(~a)     # -6
print(a << 1) # 10
print(a >> 1) # 2

#  Membership Operators

# Check if a value exists in a sequence.

# Operator	Meaning
# in	Exists
# not in	Does not exist
list1 = [1, 2, 3, 4]

print(2 in list1)      # True
print(5 not in list1) # True

#  Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a == c)      # True

# 8 Ternary (Conditional) Operator

# One-line if-else.

a = 10
b = 20

result = a if a > b else b
print(result)  # 20

# 9️ Operator Precedence (Short Example)
result = 10 + 3 * 2 ** 2
print(result)  # 22