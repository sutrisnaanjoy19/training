import json
import logging
#logging.basicConfig(filename='train.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def main(): 
    def DEL():
        try:
            key2 = input("Enter Key : ")
            del json_data[key2]
        except:
            print("key is not present")

    def GET():
        try:
            key1 = input("Enter key : ")
            value_for_specific_key = json_data[key1]
            print(value_for_specific_key)
        except:
            print("key is not present")

    def PUT():                                    
        key = input ("Enter key : ")
        value = input ("Enter value : ")
        json_data[key] = value

    ##################################################################################################
    json_data = json.load(open("/home/sutrisna/Desktop/pypy/file.json", 'r'))

    print(json_data)
    while True:
        string = input("what do you want to do GET/PUT/DEL : ")
        if string == "GET":
            GET()
        elif string == "PUT":
            PUT()
        elif string == "DEL":
            DEL()
        else:
            break

    print(json_data)

    with open("/home/sutrisna/Desktop/pypy/file.json", "w") as outfile:
        json.dump(json_data, outfile)

if __name__ == "__main__":
    main()

