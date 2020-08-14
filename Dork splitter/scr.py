import os
import time
print("><")

def chose():
    # print("\t1)Splitter URL\n\t2)Dork maker")
    choose = 1
    if choose == 1:
        splitter()
    elif choose == 2:
        maker()

def splitter():
    terry = []
    count = 0
    print("Input file name")
    file_name0 = raw_input()
    file_name0 = file_name0.replace("'", '').replace("'", "").replace(' ', '')
    time0 = str(time.time())
    folder = os.system('mkdir ' + time0)
    open('./' + time0 + '/first_' + str(time.time()) + ".txt", 'w')
    open('./' + time0 +'/second_' + str(time.time()) + ".txt", 'w')
    open('./' + time0 + '/third_' + str(time.time()) + ".txt", 'w')
    with open(file_name0, 'rb') as file:
        for line in file:
            try:
                if "." and "?" and "=" in line:
                    url = line.split("/")[-1].split("=")[0] + "="
                    if url in terry:
                        pass
                    else:
                        terry.append(url)
                        new_url1 = url.split('.')[0]
                        new_url2 = url.split('.')[1].split('?')[0]
                        new_url3 = url.split('?')[1].split('=')[0]
                        open('./' + time0 + '/first_' + str(time.time()) + ".txt", 'a+').write(new_url1 + "\n")
                        open('./' + time0 +'/second_' + str(time.time()) + ".txt", 'a+').write(new_url2 + "\n")
                        open('./' + time0 + '/third_' + str(time.time()) + ".txt", 'a+').write(new_url3 + "\n")
                else:
                    # print("Error: govno ssil")
                    pass      
            except IndexError:
                pass 
    print("All ready [" + str(count) + "]")
    chose()

if __name__ == "__main__":
    chose()