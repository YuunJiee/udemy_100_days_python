# Subscripting
print("Hello"[0])
print("Hello"[-1])


# String
print("123" + "456")

# Integer = Whole number
print(123 + 456)

# Large Integer
print(123_456_789)

# Float
print(3.14159)

# Boolean
print(True)
print(False)

#----------

len("Hello")
print(type(123))
print(type("Hello"))
print(type("123.456"))
print(type(True))

#----------

int("123") # String to Integer
print(int("123") + int("456"))

#-----------

print("My age: " + str(24))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3) # 取整數
print(2 ** 2) # 次方

# PEMDAS 優先級
# ()
# **
# * OR /
# + OR -
print(3 * (3 + 3) / 3 - 3)

#-----------
score = 0

score += 1 
print(score)

#f-string
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

