import itertools
import string
import time


chars = string.printable
password = "123"
max_length = 10
start_time = time.time()

# Try all possible combinations of characters up to max_length
for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        
        candidate = "".join(combination)
        print("Trying password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("Password found:", candidate)
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            
            raise SystemExit