import os
import requests
import time

class temp():
    language = ''
    multilang = ''

class translate():
    admin_finder_1 = ''
    admin_finder_2 = ''
    admin_finder_3 = ''
    admin_finder_4 = ''
    admin_finder_5 = ''
    admin_finder_6 = ''

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
            if '[admin_finder_1]' in line and '[' + temp.language + ']' in line:
                translate.admin_finder_1 ='\t\t|\t'+line.split('=')[1].strip() + '\t    |'
            if '[admin_finder_2]' in line and '[' + temp.language + ']' in line:
                translate.admin_finder_2 =line.split('=')[1].strip()
            if '[admin_finder_3]' in line and '[' + temp.language + ']' in line:
                translate.admin_finder_3 =line.split('=')[1].strip()
            if '[admin_finder_4]' in line and '[' + temp.language + ']' in line:
                translate.admin_finder_4 =line.split('=')[1].strip()
            if '[admin_finder_5]' in line and '[' + temp.language + ']' in line:
                translate.admin_finder_5 =line.split('=')[1].strip()
            if '[admin_finder_6]' in line and '[' + temp.language + ']' in line:
                translate.admin_finder_6 =line.split('=')[1].strip()


try:
    language()
    print "\t\t|===========================================|"
    print "\t\t|                                           |"
    print translate.admin_finder_1 
    print "\t\t|                                           |"
    print "\t\t|===========================================|"
    admin_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-2], 'settings').replace(os.path.abspath(__file__).split('/')[-1], 'admin.ini')

    print translate.admin_finder_2
    site = raw_input()

    headers = {
        'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15 Epiphany/605.1.15'
    }

    print requests.get(site, headers=headers).status_code
    print requests.get(site + 'admin.php', headers=headers).status_code

    try:
        with open(admin_dir, 'r') as file:
            for line in file:
                page = []
                counter = 0
                req0 = requests.get(site.replace('\n', '') + line.replace('\r\n', ''), headers=headers).text.encode('utf-8')
                if 'method=' in req0 and 'post' in req0 and 'login' in req0 and 'pass' in req0:
                    page.append(req0.split(' '))
                    for i in range(len(page[0])):
                        if 'input' in page[0][i]:
                            counter += 1
                            if counter > 2:
                                print translate.admin_finder_3 + str(site) + str(line).strip()
                                exit()
                else:
                    print translate.admin_finder_4 + site.replace('\n', '') +  line.strip()
    except KeyboardInterrupt:
        print translate.admin_finder_5
        exit()
        
    print translate.admin_finder_6
    raw_input()
# except Exception as e:
#     print e.message, e.args
except KeyboardInterrupt:
    pass