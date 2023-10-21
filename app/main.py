from random import randint


user = "Alex"
print(f"Hello {user}!")
rand_count = 10
min_num = 0
max_num = 100
rand_seq = [randint(min_num, max_num) for i in range(rand_count)]
print(f"This is random sequence: {rand_seq}")
