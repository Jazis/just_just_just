import os
import sys
import time

class templer():
    language = ''
    multilang = ''

class translate():
    stat_1 = ''
    stat_2 = ''
    stat_3 = ''

def language():
    multilang = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-2], 'settings').replace(os.path.abspath(__file__).split('/')[-1], 'multilang.ini')
    templer.multilang = multilang
    with open(templer.multilang, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if '[language]' in lines[i]:
                lang = lines[i].split('=')[1].replace(' ', '').strip()
                templer.language = lang
            # if '[menu_banner]' in lines[i] and '[' + lang + ']' in lines[i]:
                # print lines[i]
    with open(templer.multilang, 'r') as file:
        for line in file:
            if '[stat_1]' in line and '[' + templer.language + ']' in line:
                translate.stat_1 =line.split('=')[1].strip()
            if '[stat_2]' in line and '[' + templer.language + ']' in line:
                translate.stat_2 =line.split('=')[1].strip()
            if '[stat_3]' in line and '[' + templer.language + ']' in line:
                translate.stat_3 =line.split('=')[1].strip()

try:

    temp1_save = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt'
    temp2_save = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'emails.txt'

    print temp1_save
    os.system('clear')

    class temp():
        all_lines = 0
        images = 0
        js = 0
        css = 0
        emails = 0
        docs = 0
        txt = 0
        xls = 0
        sql = 0
        names = 0


    def check(temp1_save, temp2_save):
        with open(temp1_save, 'r') as file:
            for line in file:
                if '.jpg' in line or '.jpeg' in line or '.ico' in line:
                    temp.images += 1
                if '.js' in line:
                    temp.js += 1
                if '.css' in line:
                    temp.css += 1
                if '.doc' in line:
                    temp.docs += 1
                if '.txt' in line:
                    temp.txt += 1
                if '.xls' in line:
                    temp.xls += 1
                if '.' in line and '?' in line and '=' in line:
                    if '.php' in line or '.asp' in line or '.aspx' in line or '.cfm' in line or '.cgi' in line or '.jsp' in line:
                        temp.sql += 1
                if 'name=' in line or 'accountname=' in line or 'login=' in line:
                    temp.names += 1
                temp.all_lines +=1
        with open(temp2_save, 'r') as file:
            for line in file:
                if '@' in line:
                    temp.emails += 1
        print"\t" + translate.stat_1
        print('\n\t[+] ' + translate.stat_2 +' : ' + str(temp.all_lines)
        + '\n\t[+] '+ translate.stat_3 +' : ' + str(temp.images)
        + '\n\t[+] JS : ' + str(temp.js)
        + '\n\t[+] CSS : ' + str(temp.css)
        + '\n\t[+] Emails : ' + str(temp.emails)
        + '\n\t[+] DOCx : ' + str(temp.docs)
        + '\n\t[+] TXT : ' + str(temp.txt)
        + '\n\t[+] XLS : ' + str(temp.xls)
        + '\n\t[+] MSQL : ' + str(temp.sql)
        + '\n\t[+] UserNames : ' + str(temp.names)
        )
        sys.stdout.write('\r\t\\\t\\\t\\')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\r\t|\t|\t|')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\r\t/\t/\t/')
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\r\t-\t-\t-')
        sys.stdout.flush()
        time.sleep(1)
        temp.all_lines = 0
        temp.images = 0
        temp.js = 0
        temp.css = 0
        temp.emails = 0
        temp.docs = 0
        temp.txt = 0
        temp.xls = 0
        temp.sql = 0
        temp.names = 0
        os.system('clear')
        check(temp1_save, temp2_save)


    if __name__ == '__main__':
        language()
        check(temp1_save, temp2_save)
        
except Exception as e:
    print e.message, e.args
except KeyboardInterrupt:
    exit()