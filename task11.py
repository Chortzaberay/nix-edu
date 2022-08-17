import time
import random

random_number = random.randint(1, 10)

start_time = time.monotonic()
time.sleep(random_number)
end_time = time.monotonic()
print(str(end_time - start_time))

