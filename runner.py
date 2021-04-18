import os, threading

def start_server():
    os.system('python webapi.py')

def start_click_listener():
    os.system('python clicker.py')


server = threading.Thread(target=start_server)
clicker = threading.Thread(target=start_click_listener)

server.start()
clicker.start()
