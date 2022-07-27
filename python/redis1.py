import redis
import pickle
 
'''def main():
    redis_client = redis.Redis(host='localhost',port=6379)
    redis_client.set('foo','bar')
    print(redis_client.get('foo'))'''

'''def main():
    redis_client = redis.Redis(host='localhost',port=6379)
    key = 'https://docs.google.com/document/d/1xdnIHqwS8RlwAWtQCM2y_k1jFkl-m-1kpGd3DLVLTas/edit'
    redis_client.set(key,'soma data')
    print(redis_client.get(key))'''

class Person:
    def __init__(self, name) -> None:#init must only return none
        self.name = name

def main():
    redis_client = redis.Redis(host='localhost',port=6479)
    data = Person(name = 'soma')
    redis_client.set('name',pickle.dumps(data))
    print(pickle.loads(redis_client.get('name')))

    pipeline = redis_client.pipeline()
    pipeline.set("foo" ,"bar")
    pipeline.get("foo")
    pipeline.set("clumatized" ,"iam")
    pipeline.delete("clumatized")
    pipeline.execute() #to execute all commands


    '''
    r = redis.Redis(host = 'localhost' , port = 6379) #pub/sub
    ps = r.pubsub()
    r.publish("channel1" , "soma data")
    ps.subscribe("channel1")
    ps.get_message()
    #my handler'''
    '''
    def my_handler(message):
         print("MY_CHANNEL_HANDLER : ", message['data'])
    ps.subscribe(**{'channel3' : my_handler})
    ps.get_message()
    r.publish("channel3", 'awosome data')
    message = ps.get_message() # only print out the data part of the message
    ps.unsubscribe("channel1")
    p = r.pubsub(ignore_subscribe_messages=True)

    '''



main()