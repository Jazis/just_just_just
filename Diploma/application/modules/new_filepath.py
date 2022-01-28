import os
import requests
import time

class temp():
    language = ''
    multilang = ''

class translate():
    index_of_1 = ''
    index_of_2 = ''
    index_of_3 = ''

def language():
    multilang = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-2], 'settings').replace(os.path.abspath(__file__).split('/')[-1], 'multilang.ini')
    temp.multilang = multilang
    with open(temp.multilang, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if '[language]' in lines[i]:
                lang = lines[i].split('=')[1].replace(' ', '').strip()
                temp.language = lang
            # if '[menu_banner]' in lines[i] and '[' + lang + ']' in lines[i]:
                # print lines[i]
    with open(temp.multilang, 'r') as file:
        for line in file:
            if '[index_of_1]' in line and '[' + temp.language + ']' in line:
                translate.index_of_1 =line.split('=')[1].strip()
            if '[index_of_2]' in line and '[' + temp.language + ']' in line:
                translate.index_of_2 =line.split('=')[1].strip()
            if '[index_of_3]' in line and '[' + temp.language + ']' in line:
                translate.index_of_3 =line.split('=')[1].strip()

try:
    language()
    print"\t\t|===========================================|"
    print"\t\t|                                           |"
    print"\t\t|   " + translate.index_of_1 +"     |"
    print"\t\t|                                           |"
    print"\t\t|===========================================|"


    temp1_save = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt'

    index_of_save = open('Index-of_' + str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())) + '.txt', 'w+')

    no_dub = []
    count = 0

    with open(temp1_save, 'r') as file:
        for line in file:
            try:
                headers = {
                    'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15 Epiphany/605.1.15'
                }
                count += 1
                
                try:
                    req0 = requests.get(line.replace('\n', ''), headers=headers).text.encode('utf-8')
                    if 'Directory' in req0 and 'Parent' in req0 and 'Directory Listing' in req0 and 'Index of /' in req0:
                        print str([count]) + '[+] Index of ' + str(line)
                        index_of_save = open('Index-of_' + str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())) + '.txt', 'a+')
                        index_of_save.write(str(line))
                    else:
                        print str([count]) + translate.index_of_3
                        pass
                except requests.exceptions.SSLError:
                    pass
                except requests.exceptions.InvalidSchema:
                    pass
                except requests.exceptions.ConnectionError:
                    pass
            except IndexError:
                pass
# except Exception as e:
#     print e.message, e.args
except KeyboardInterrupt:
    exit()
