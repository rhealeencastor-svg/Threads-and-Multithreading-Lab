import threading
import time

def display_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

t1 = threading.Thread(target=display_numbers)

t1.start()

t1.join()

print("Program completed.")
