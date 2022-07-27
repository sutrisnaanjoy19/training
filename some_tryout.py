import time
import redis 

def main():
    r =redis.Redis()
    r.set("foo" ,"bar")
    start = time.time()
    for i in range(100000):
        r.get('foo')
    end =time.time()
    print((end - start))


main()
