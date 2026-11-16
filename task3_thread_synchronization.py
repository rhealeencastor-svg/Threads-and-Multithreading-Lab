import threading
import time

def download_file():
    print("Downloading file...")
    time.sleep(3)
    print("Download completed.")

def main():
    t1 = threading.Thread(target=download_file)
    t1.start()

    print("Main program is waiting...")
    t1.join()

    print("Main program continues.")

main()
