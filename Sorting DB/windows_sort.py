import os, sys
import threading
import time

class temp_0():
    counter = 0
    summary = 0 

def func(qwe, file, file_size):
    temp_0.counter = temp_0.counter + 1
    if temp_0.counter == 10000:
        temp_0.summary = 0
        for i in range(len(os.listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'sorting/')))):
            file =  os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'sorting/') + os.listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'sorting/'))[i]
            temp_0.summary = temp_0.summary + os.path.getsize(file)
        p = float(temp_0.summary)/float(file_size)*100
        sys.stdout.write('\r' + '|-> ' + str(int(p)) + '%')
        temp_0.counter = 0
    try:
        bkv = qwe[0] + qwe[1]
        bkv = bkv.lower()
        open( 'sorting/' + bkv + '.txt', 'a+').write(qwe)
    except IndexError:
        pass
    except OSError:
        pass 

try:
    os.system('mkdir sorting/')
except OSError:
    pass
counter0 = 0
counter1 = 0
while True:
    base = input('BSE PLZ RETARD FR SRT ->')
    threads1 = []
    threads0 = []
    base = base.replace('"', '').replace("'", "").replace(' ', '')
    file_size = os.path.getsize(base)
    with open(base, 'r') as file:
        try:
            for line in file:
                line = line.replace('\r', '')
                try:
                    if len(threads0) >= 500:
                        # sys.stdout.write("\n")   
                        time.sleep(0.1)
                        threads0 = []
                        threads1.append(line)
                        thread2 = threading.Thread(target=func, args=(line, file, file_size))
                        thread2.start()
                    else:
                        try:
                            threads1 = []
                            threads0.append(line)
                            thread1 = threading.Thread(target=func, args=(line, file, file_size))
                            thread1.start()
                        except RuntimeError:
                            pass
                except RuntimeError:
                    pass
        except UnicodeDecodeError:
            pass