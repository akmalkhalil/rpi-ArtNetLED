# This is a file created so I can test the multithreading functionality on Windows without the pi stuff or the artnet node

from time import sleep

running = True

def main():
    global running
    running = True
    count = 0
    while running:
        print("Thread counter " + str(count))
        sleep(1)
        count +=1
        if count == 30:
            break
    return 0

def stop():
    global running
    running = False


# Ok that seems to work
# I'll set up artnetLEDController like this for now, but it should be encapsulated in a class tbh
