from utils import random_gen


user = "Alex"
print(f"Hello {user}!")
rand_count = 10
min_num = 0
max_num = 100
rand_seq = random_gen.get_rand_int_seq(min_num, max_num, rand_count)
print(f"This is random sequence: {rand_seq}")
