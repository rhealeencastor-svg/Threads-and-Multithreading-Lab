import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter

    for i in range(100000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter:", counter)
