import os
import requests
import time
import sys

class templer():
    language = ''
    multilang = ''

class translate():
    spider_module_1 = ''
    spider_module_2 = ''
    spider_module_3 = ''
    spider_module_4 = ''
    spider_module_5 = ''
    spider_module_6 = ''
    spider_module_7 = ''
    spider_module_8 = ''
    spider_module_9 = ''
    spider_module_10 = ''
    spider_module_11 = ''
    spider_module_12 = ''
    spider_module_13 = ''
    spider_module_14 = ''
    spider_module_15 = ''
    spider_module_16 = ''
    spider_module_17 = ''
    spider_module_18 = ''

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
            if '[spider_module_1]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_1 =line.split('=')[1].strip()
            if '[spider_module_2]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_2 =line.split('=')[1].strip()
            if '[spider_module_3]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_3 =line.split('=')[1].strip()
            if '[spider_module_4]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_4 =line.split('=')[1].strip()
            if '[spider_module_5]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_5 =line.split('=')[1].strip()
            if '[spider_module_6]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_6 =line.split('=')[1].strip()
            if '[spider_module_7]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_7 =line.split('=')[1].strip()
            if '[spider_module_8]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_8 =line.split('=')[1].strip()
            if '[spider_module_9]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_9 =line.split('=')[1].strip()
            if '[spider_module_10]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_10 =line.split('=')[1].strip()
            if '[spider_module_11]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_11 =line.split('=')[1].strip()
            if '[spider_module_12]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_12 =line.split('=')[1].strip()
            if '[spider_module_13]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_13 =line.split('=')[1].strip()
            if '[spider_module_14]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_14 =line.split('=')[1].strip()
            if '[spider_module_15]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_15 =line.split('=')[1].strip()
            if '[spider_module_16]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_16 =line.split('=')[1].strip()
            if '[spider_module_17]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_17 =line.split('=')[1].strip()
            if '[spider_module_18]' in line and '[' + templer.language + ']' in line:
                translate.spider_module_18 =line.split('=')[1].strip()


def banner():
    print"\t\t|===========================================|"
    print"\t\t|                                           |"
    print"\t\t|   " + translate.spider_module_1 +"     |"
    print"\t\t|                                           |"
    print"\t\t|===========================================|"
try:
    language()
    banner()
    print translate.spider_module_2
    site = raw_input()

    if '://' in site:
        site = site.replace('https://', '').replace('http://','')
    print site

    class checksum():
        count0 = 0
        count1 = 0
        count2 = 0
        email_count = 0
        site = ''
        charset =''
        token = 0
        app_words =[]

    class select_changer():
        select_yes = ['yes', 'y', 'YES', 'Yes']
        select_no = ['no', 'n', 'NO', 'no']
        email = 0


    def _select_(email):
        if email in select_changer.select_yes:
            select_changer.email = 1
            pass
        elif email in select_changer.select_no:
            select_changer.email = 0
            pass
        elif email == None:
            select_changer.email = 0
            pass
        else:
            select_changer.email = 0
            print translate.spider_module_3

    email = raw_input(translate.spider_module_4)
    if email == None:
        pass
    _select_(email)

    '''
    -_-_-_-_-_-_-_-_-Comment_-_-_-_-_-_-
    sites_score -- All parsed lines
    checksum.count0 -- sites via domain
    checksum.count1 -- sites via sql
    checksum.count2 -- support lines
    '''
    headers = {
        'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15 Epiphany/605.1.15'
    }


    def site_formatten(site):
        if '/' not in site[-1]:
            site = site + '/'
        if '://' not in site[0-4]:
            site = 'http://' + site
            checksum.site = site

    site_formatten(site)
    print checksum.site

    raw_input(translate.spider_module_5)

    print translate.spider_module_6
    time.sleep(1)

    temp0_save = open('temp0', 'w+')
    temp1_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt', 'w+')
    temp2_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'may_sql.txt', 'w+')
    temp3_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'support_lines.txt', 'w+')
    stat = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'/') + 'stat.py'
    email_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'emails.txt', 'w+')

    banner()
    try:
        robots = requests.get(checksum.site + 'robots.txt')
        if robots.status_code == 200 and 'User-agent' in robots.text or 'Disallow' in robots.text or 'Sitemap':
            print '+++++++++++++++++++++++\n+- ' + str(checksum.site) + 'robots.txt\n+++++++++++++++++++++++\n'
            temp3_save.write('+++++++++++++++++++++++\n+- ' + str(checksum.site) + 'robots.txt\n+++++++++++++++++++++++\n')
            checksum.count2 +=1
    except requests.exceptions.ConnectionError:
        print translate.spider_module_7
        exit()
        
    # print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1],'output')

    sites_score = []

    # ///////////// -- The definition of the encoding ---\\\\\\\\\\\

    check_code = requests.get(checksum.site, headers=headers).text.encode('utf-8')
    temp0_save.write(check_code)
    if 'charset' in check_code:
        with open('temp0', 'r') as file:
            for line in file:
                if 'charset' in line:
                    charset = line.split('charset')[1]
                    if '=' in charset:
                        charset = charset.replace('=', '')
                    if '"' in charset:
                        charset = charset.replace('"', '')
                    if '>' in charset or '<' in charset:
                        charset = charset.replace('>', '').replace('<','')
                    if '/' in charset or '\\' in charset:
                        charset = charset.replace('/', '').replace('\\','')
                    charset = charset.split(' ')[0]
                    checksum.charset = charset
    # ---////////////////////---///////////////----///////////////////
    try:
        req0 = requests.get(checksum.site, headers=headers).text.encode(charset)
    except UnicodeEncodeError:
        req0 = requests.get(checksum.site, headers=headers).text.encode(charset = 'UTF-8')
        checksum.charset = 'UTF-8'
    except NameError:
        req0 = requests.get(checksum.site, headers=headers).text
        checksum.charset = 'UTF-8'
    except LookupError:
        req0 = requests.get(checksum.site, headers=headers).text
        checksum.charset = 'UTF-8'
    
    try:
        temp0_save.write(req0)
    except UnicodeEncodeError:
        # req0 = requests.get(checksum.site, headers=headers).text.encode('utf-8')
        # checksum.charset = 'ascii'
        pass

    def email_extractor(email_save):
        email_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'emails.txt', 'a+')
        with open('temp0', 'r') as file:
            for line in file:
                if 'href' in line or 'src' in line:
                    if 'mailto:' in line:
                        new_line0 = line.split('"')
                        for i in range(len(line.split('"'))):
                            if '@' in line.split('"')[i]:
                                try:
                                    new_line1 = line.split('"')[i].split(':')[1].split('>')[0]
                                    if ' ' in new_line1:
                                        pass
                                    else:
                                        if '@' in new_line1 and '.' in new_line1:
                                            if new_line1 in checksum.app_words:
                                                pass
                                            else:
                                                checksum.app_words.append(new_line1)
                                                email_save.write(new_line1 + '\n')
                                except IndexError:
                                    pass
                        # temp2_save.write(line)
                        # print line
                        checksum.email_count += 1

    def stat_start(stat):
        os.system("gnome-terminal --geometry 20x20 -e 'python " +  stat + "'")

    # ________///////////----Support urls finder------Login, reg, adminLogin, sitemap, robots.txt
    def support(new_line2, temp3_save):
        headers = {
            'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15 Epiphany/605.1.15'
        }
        if 'login' in new_line2 or 'auth' in new_line2:
            try:
                req0 = requests.get(new_line2, headers=headers).text.encode(checksum.charset)
                if 'password' in req0 and 'register' in req0 and 'login' in req0:
                    if 'username' in req0 or 'restore':
                        print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_8 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                        temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_8 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                        checksum.count2 +=1
                    if 'password' in req0 and 'register' in req0 and 'login' in req0:
                        if 'username' in req0 and 'password' in req0 and 'confirm' in req0:
                            if 'capcha' in req0 or 'secret'  in req0: 
                                print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_9 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                                temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_9 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                                checksum.count2 +=1
                    if 'login' in req0 and 'passw' in req0 and 'admin' in req0 and 'submit' in req0:
                        print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_10 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                        temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_10 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                        checksum.count2 +=1
                if 'sitemap' in new_line2:
                    print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_11 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                    temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_11 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                    checksum.count2 +=1
                if 'robots.txt' in new_line2:
                    print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_12 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                    temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_12 + ' \n+-' + str(new_line2) + '\n+++++++++++++++++++++++++++++++++\n')
                    checksum.count2 +=1
            except requests.exceptions.InvalidSchema:
                next
            except requests.exceptions.InvalidURL:
                next
            except requests.exceptions.InvalidURL:
                next
        

    def check(temp1_save, sites_score):
        headers = {
            'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15 Epiphany/605.1.15'
        }
        temp1_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt', 'a+')
        temp2_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'may_sql.txt', 'a+')
        temp3_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'support_lines.txt', 'a+')
        try:
            x = 0
            for x in range(len(sites_score)):
                if 'h' in sites_score[x][0]:
                    temp = open('temp0', 'w+')
                    if checksum.site.split('/')[2] in sites_score[x]:
                        if '\/' in sites_score[x]:
                            pass
                        if '.attr' in sites_score[x]:
                            pass
                        else:
                            try:
                                req1 = requests.get(sites_score[x], headers=headers).text.encode(charset)
                                temp.write(req1)
                                req_cookie = requests.get(sites_score[x], headers=headers).cookies
                                if 'token' in req_cookie or 'SESSION' in req_cookie:
                                    if checksum.token == 1:
                                        pass
                                    else:
                                        print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_13 + '\n+-' + str(req_cookie) + '\n+++++++++++++++++++++++++++++++++\n')
                                        temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_13 + '\n+-' + str(req_cookie) + '\n+++++++++++++++++++++++++++++++++\n')
                                pass
                            except LookupError:
                                req1 = requests.get(sites_score[x], headers=headers).text.encode(checksum.charset)
                                temp.write(req1)
                                req_cookie = requests.get(sites_score[x], headers=headers).cookies
                                if 'token' in req_cookie or 'SESSION' in req_cookie:
                                    if checksum.token == 1:
                                        pass
                                    else:
                                        print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_13 + '\n+-' + str(req_cookie) + '\n+++++++++++++++++++++++++++++++++\n')
                                        temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_13 + '\n+-' + str(req_cookie) + '\n+++++++++++++++++++++++++++++++++\n')
                                pass
                            except UnicodeEncodeError:
                                try:
                                    req1 = requests.get(sites_score[x], headers=headers).text.encode('utf-8')
                                    temp.write(req1)
                                    req_cookie = requests.get(sites_score[x], headers=headers).cookies
                                    if 'token' in req_cookie or 'SESSION' in req_cookie:
                                        if checksum.token == 1:
                                            pass
                                        else:
                                            print('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_13 + '\n+-' + str(req_cookie) + '\n+++++++++++++++++++++++++++++++++\n')
                                            temp3_save.write('+++++++++++++++++++++++++++++++++\n' + '++++++ ' + translate.spider_module_13 + '\n+-' + str(req_cookie) + '\n+++++++++++++++++++++++++++++++++\n')
                                    pass
                                except requests.exceptions.ConnectionError:
                                    next
                            except requests.exceptions.InvalidURL:
                                next
                            except requests.exceptions.InvalidSchema:
                                next
                            except requests.exceptions.SSLError:
                                next
                            except requests.exceptions.ConnectionError:
                                next
                            except NameError:
                                print '\n' + translate.spider_module_14
                                cs_char = raw_input(translate.spider_module_15)
                                checksum.charset = cs_char
                                req0 = requests.get(checksum.site, headers=headers).text.encode(checksum.charset)
                        pass
                        if '.' in sites_score[x] and '?' in sites_score[x] and '=' in sites_score[x]:
                            if '.php' in sites_score[x] or '.asp' in sites_score[x] or '.aspx' in sites_score[x] or '.cfm' in sites_score[x] or '.cgi' in sites_score[x] or '.jsp' in sites_score[x]:
                                if '.png' not in sites_score[x] or '.ico' not in sites_score[x] or '.jpg' not in sites_score[x] or '.jpeg' not in sites_score[x] or '.css' not in sites_score[x] or '.js' not in sites_score[x] or '.css' not in sites_score[x]: 
                                    temp2_save.write(sites_score[x].strip() + '\n')
                                    checksum.count1 += 1
                        if select_changer.email == 1:
                            email_extractor(email_save)
                        else:
                            pass
                    else:
                        next        
                    with open('temp0', 'r') as file:
                        for line in file:
                            if 'href' in line or 'src' in line:
                                new_line0 = line.split('"')
                                for i in range(len(new_line0)):
                                    if '/' in new_line0[i] and '<' not in new_line0[i]:
                                        if '/' in new_line0[i][0]:
                                            new_line2 = str(checksum.site) + str(new_line0[i]).replace('/>','')
                                            if 'h' in new_line2[0]:
                                                if new_line2 not in sites_score:
                                                    support(new_line2, temp3_save)
                                                    temp1_save.write(new_line2.strip() + '\n')
                                                    sites_score.append(new_line2)
                                                    if checksum.site.split('/')[2] in new_line2:
                                                        checksum.count0 += 1
                                                if 'robots.txt' in new_line2:
                                                    temp3_save.write(new_line2 + '\n')
                                                    checksum.count2 += 1
                                        elif 'http' in new_line0[i]:
                                            if 'h' in new_line0[i][0]:
                                                if new_line0[i] not in sites_score:
                                                    new_line2 = new_line0[i]
                                                    support(new_line2, temp3_save)
                                                    if '&#58;' in new_line0[i]:
                                                        new_line0[i].replace('&#58;', ':')
                                                        pass
                                                    else:
                                                        sites_score.append(new_line0[i])
                                                        if 'h' in new_line0[i][0] and 't' in new_line0[i][1]:
                                                            temp1_save.write(new_line0[i].strip() + '\n')
                                                            if checksum.site.split('/')[2] in new_line0[i]:
                                                                checksum.count0 += 1
                                                            if 'robots.txt' in new_line0[i]:
                                                                temp3_save.write(new_line0[i] + '\n')
                                                                checksum.count2 += 1
                    # stat_start(stat)
                    # sys.stdout.write('\r' + str(str(len([sites_score]))) + str([checksum.count0]) + str([checksum.count1]) + str([checksum.count2]) + str([checksum.email_count]))
                    # sys.stdout.write("\n")      
                else:
                    next
            check(temp1_save, sites_score)
        except KeyboardInterrupt:
            print '\n' + translate.spider_module_16
            exit()

    with open('temp0', 'r') as file:
        for line in file:
            if 'href' in line or 'src' in line:
                new_line0 = line.split('"')
                for i in range(len(new_line0)):
                    if '/' in new_line0[i] and '<' not in new_line0[i]:
                        if '/' in new_line0[i][0]:
                            new_line2 = str(checksum.site) + str(new_line0[i]).replace('/>','')
                            if new_line2 not in sites_score:
                                temp1_save.write(new_line2.strip() + '\n')
                                sites_score.append(new_line2)
                        elif 'http' in new_line0[i]:
                            if new_line0[i] not in sites_score:
                                if '&#58;' in new_line0[i]:
                                    new_line0[i].replace('&#58;', ':')
                                    pass
                                else:
                                    sites_score.append(new_line0[i])
                                    temp1_save.write(new_line0[i].strip() + '\n')
        stat_start(stat)
        print len(sites_score)
        check(temp1_save, sites_score)

    temp0_save.close()
    temp1_save.close()
    temp2_save.close()

    print translate.spider_module_17
    raw_input()
except KeyboardInterrupt:
    print '\n' + translate.spider_module_18
