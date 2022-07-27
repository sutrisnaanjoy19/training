#count number of request per second
#time taken per request
#total time taken
#how many error it seeing

import time

request_num = 0
total_req_time = 0

def auto_handle_decorator(func):
    def wrapper(*args , **kwargs):
        request_num += 1
        start = time.time
        return_value= func(*args , **kwargs)
        end = time.time
        return return_value
    return wrapper


@auto_handle_decorator
def handle_request():
    request_num += 1
    start = time.time()
    handle_user_stuff()
    call_db()
    r=Response()
    end=time.time()
    total_req_time = end-start
    return r

def handle_user_stuff():
    pass

def call_db():
    pass

class Response():
    pass

'''
class greeter:
    def __enter__(self):
        print("hi")
    def __exit__(self , *args , **kwargs):
        print("bye")



with greeter():
    print("middle")


hi
middle
bye
        '''