# Example of a multi-threaded application using start() and join()
import threading

chunks = ['abcdefghij', 'klmnopqrs', 'tuvwxyz']
threads = []

def writer(chunk):
    with open('alphabet.txt', 'a') as f:
        f.write(chunk)

if __name__ == '__main__':
    print('Main thread starting')
    for chunk in chunks:
        t = threading.Thread(target=writer, args=[chunk])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    with open('alphabet.txt') as f:
        print(f.read())
    print('Main thread ending')