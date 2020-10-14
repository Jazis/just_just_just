import os
import requests
import time
import threading

class temp():
    file_name = 'file_test.txt'

def check(line):
    print('123')
    print('123')
    print('123')
    print('123')
    open(temp.file_name, 'a+').write("working")

base = input("Site list -> ")
base = base.replace('"', '').replace("'", "").replace(' ', '')
open(temp.file_name, 'w')
with open(base, 'r') as file:
    for line in file:
        ne_thread = threading.Thread(target = check, args = (line, ))
        ne_thread.start()
        time.sleep(5)