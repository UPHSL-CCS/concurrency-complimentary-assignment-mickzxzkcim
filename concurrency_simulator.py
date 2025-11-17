import threading
import time

#Task Simulator for numbers
def print_numbers():
    for i in range(1, 12):
        print(f"Printing number {i}")
        time.sleep(1) # Simulate a delay

#Task simulator for letters
def print_letters():
    for letter in 'CatsareCute':
        print(f"Printing letter {letter}")
        time.sleep(1) # Simulate a delay

#This part creates the two thread objects
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# start of the thread
thread1.start()
thread2.start()

thread1.join()
thread2.join()
