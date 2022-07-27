import queue


import queue
import time
import threading
import random

def myworkers(myqueue):
    while True:
        x = myqueue.get()
        print(f"thread {threading.current_thread().name} : is sleeping for {x} seconds")
        time.sleep(x)
        print(f"thread {threading.current_thread().name} : is awake after sleeping {x} seconds")

def main():
    NUM_THREAD=5
    myqueue=queue.Queue(maxsize=5)
    for i in range(NUM_THREAD):
        t = threading.Thread(target=myworkers , args=(myqueue,) , daemon=True)
        t.start()
    while True:
        myqueue.put(random.randint(1,5))

if __name__ == '__main__':
    main()

'''class Mylist(list):
    def get(self, idx, default=None):
        try:
            return self[idx]
        except IndexError:
            return default
            
>>> list1 = Mylist((1, 2, 3))           
>>> list1.get(0 , "mydefault")
1
>>> list1.get(1 , "mydefault")
2
>>> list1.get(2 , "mydefault")
3
>>> list1.get(3 , "mydefault")
'mydefault'
            
'''