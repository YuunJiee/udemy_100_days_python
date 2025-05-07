import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!#$%&()*+"
numbers = "0123456789"


print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# easy
password_list = []
for l in range(0, num_letters):
    password_list.append(random.choice(letters))
for s in range(0, num_symbols):
    password_list.append(random.choice(symbols))
for n in range(0, num_numbers):
    password_list.append(random.choice(numbers))

password = ""
for p in password_list:
    password += p
print(f"(Easy) Here is your password: {password}")

# hard -> 執行時間 O(n^2)
password_list2 = password_list.copy()
password_hard = ""
for num in range(0, len(password)):
    p = random.choice(password_list2) # 隨機取一個
    password_hard += p
    password_list2.remove(p) # 移除

print(f"(Hard) Here is your password: {password_hard}")


# teacher method hard -> 執行時間 O(n)
password_list3 = password_list.copy()
password_teacher = ""
random.shuffle(password_list3) # !!! 把陣列打亂
for p in password_list3:
    password_teacher += p
print(f"(Teacher) Here is your password: {password_teacher}")

