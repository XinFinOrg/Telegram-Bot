from twisted.internet import task, reactor
import requests
import json

timeout = 21600.0 # Sixty seconds
token = "552545969:AAHmuCZ8fdjggXtCcOmnLinv1Utfa_N_cEc"
array_size = 0

def send(text):
    params = {'chat_id': '@xinfintalk', 'text': text,"parse_mode":"HTML"}
    sresp = requests.post('https://api.telegram.org/bot552545969:AAHmuCZ8fdjggXtCcOmnLinv1Utfa_N_cEc/sendMessage', params)

def message_picker():
    with open('messages.json') as json_file:
        lMessages = json.load(json_file)
        ldata =lMessages["Messages"]
        length =len(ldata)
        print (ldata[array_size])
        global array_size

        if(array_size< length):
            send(ldata[array_size])
            array_size += 1

        else:
            send(ldata[0])
            array_size +=1

        # sresp = requests.post('https://api.telegram.org/bot609512942:AAHCXKBKWEAhSuMpRWTW7qPne3kIiXJZ-Zo/sendMessage', params)
        pass

def eight_hour_msg():

    with open('eight_hour.json') as json_file:
        lMessages = json.load(json_file)
        ldata =lMessages["Messages"]
        # print (ldata)
        # print("hi\ntesting")
        send(ldata)
        pass

# l = task.LoopingCall(message_picker)
# l.start(timeout) # call every sixty seconds

lnewtask = task.LoopingCall(eight_hour_msg)
lnewtask.start(43200)

reactor.run()
