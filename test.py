import math
import time
import sys

sys.set_int_max_str_digits(100000)

last_time = time.time_ns()

print(math.factorial(21443))

print(time.time_ns() - last_time)