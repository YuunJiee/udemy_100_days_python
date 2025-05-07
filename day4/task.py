import random
import my_module

# random
random_integer = random.randint(0, 9)
print(random_integer)

# 不包含10
random_number = random.random() * 10
print(random_number)

# 包含10
random_float = random.uniform(1, 10)
print(random_float)

# module
print(my_module.my_number)


