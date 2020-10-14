import os
import requests
import time
import threading

class temp():
    language = ''
    multilang = ''
    system = ''

class translate():
    sql_module_1 = ''
    sql_module_2 = ''
    sql_module_3 = ''
    sql_module_4 = ''
    sql_module_5 = ''
    sql_module_6 = ''
    sql_module_7 = ''
    sql_module_8 = ''
    sql_module_9 = ''
    sql_module_10 = ''
    sql_module_11 = ''

def language():
    multilang = os.path.abspath(__file__).replace(os.path.abspath(__file__).split(temp.system)[-2], 'settings').replace(os.path.abspath(__file__).split(temp.system)[-1], 'multilang.ini')
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
            if '[sql_module_1]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_1 =line.split('=')[1].strip()
            if '[sql_module_2]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_2 =line.split('=')[1].strip()
            if '[sql_module_3]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_3 =line.split('=')[1].strip()
            if '[sql_module_4]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_4 =line.split('=')[1].strip()
            if '[sql_module_5]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_5 =line.split('=')[1].strip()
            if '[sql_module_6]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_6 =line.split('=')[1].strip()
            if '[sql_module_7]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_7 =line.split('=')[1].strip()
            if '[sql_module_8]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_8 =line.split('=')[1].strip()
            if '[sql_module_9]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_9 =line.split('=')[1].strip()
            if '[sql_module_10]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_10 =line.split('=')[1].strip()
            if '[sql_module_11]' in line and '[' + temp.language + ']' in line:
                translate.sql_module_11 =line.split('=')[1].strip()

def system_check():
    if '/' in os.path.abspath(__file__):
        print("This is Linux")
        temp.system = '/'
    if '\\' in os.path.abspath(__file__):
        print("This is Windows")
        temp.system = '\\'
    else:
        print("Ya hz chto eto :(\nLets go again\n")
        system_check()

try:
    system_check()
    language()
    sql_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split(temp.system)[-2], 'settings').replace(os.path.abspath(__file__).split(temp.system)[-1], 'sql.ini')
    sql_words_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split(temp.system)[-2], 'settings').replace(os.path.abspath(__file__).split(temp.system)[-1], 'sql_words.ini')
    temp2_save = os.path.abspath(__file__).replace(os.path.abspath(__file__).split(temp.system)[-1],'output' + temp.system) + 'may_sql.txt'
    sites = []
    class checksum():
        count0 = 0 # good tries
        count1 = 0 # All tries
        site = ''
        new_line0 = ''.replace('\n', '')
        new_line1 = ''
        selection = 0
        mode_selection = 0
    # print temp2_save
    # print sql_dir
    # print sql_words_dir

    
    save_file0 = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split(temp.system)[-1],'output' + temp.system) + 'sql_save_' + str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())) + '.txt', 'w')
    
    def not_bad(save_file0, sites):
        if checksum.selection == 1:
            if checksum.new_line0 in checksum.site:
                pass
            else:
                checksum.count0+=1
                print(str([checksum.count0]) + translate.sql_module_1)
                save_file0.write(str(checksum.new_line0.replace('\n', '') + checksum.new_line1))
                sites.append(checksum.new_line0)
        if checksum.selection == 2:
            checksum.count0+=1
            try:
                print(str([checksum.count0]) + translate.sql_module_1)
                save_file0.write(str(checksum.new_line0.replace('\n', '') + checksum.new_line1))
                save_file0.close()
            except ValueError:
                time.sleep(3)
                not_bad(save_file0, sites)
            exit()

    def check_sql(line, new_line1, new_line0, temp_1, temp_0):
        # print(line, new_line1, new_line0)
        req0 = requests.get(new_line0 + new_line1).text.encode('utf-8')
        temp_1.write(str(req0))
        line_0 = line
        checksum.new_line0 = new_line0
        checksum.new_line1 = new_line1
        with open(temp_0, 'r') as file:
            for line in file:
                if 'SQL syntax' in line:
                    not_bad(save_file0, sites)
                if 'MySQL server ' in line:
                    not_bad(save_file0, sites)
                if 'You have an error in your SQL syntax' in line:
                    not_bad(save_file0, sites)
                if 'check the manual that corresponds to your MySQL server version for the right syntax to use near' in line:
                    not_bad(save_file0, sites)
                if 'mysql_fetch_array()' in line:
                    not_bad(save_file0, sites)
                if 'Warning: mysql_fetch_array()' in line:
                    not_bad(save_file0, sites)
                if 'Warning: mysql_' in line:
                    not_bad(save_file0, sites)
                if 'Database error' in line:
                    not_bad(save_file0, sites)
                if 'SELECT * FROM ' in line:
                    not_bad(save_file0, sites)
                if 'MySQL error' in line:
                    not_bad(save_file0, sites)
                if 'MySQL' and ':' and 'Warning' in line:
                    not_bad(save_file0, sites)

    def first_function(new_line0, save_file0):
        new_line1 = ''
        count0 = 0
        temp_0 = 'temp'
        temp_1 = open(temp_0, 'w')
        checksum.count1 += 1
        print(str([checksum.count1]) + translate.sql_module_2 + str([new_line0.replace('\n', '')]))
        req0 = requests.get(new_line0).text.encode('utf-8')
        if 'SQL syntax' in str(req0):
            not_bad(save_file0, sites)
        else:
            count0+=1
        with open(sql_dir, 'r') as file:
            for line in file:
                new_line1 = line 
                with open(sql_words_dir, 'r') as file:
                    for line in file:
                        new_thread = threading.Thread(target=check_sql, args=(line, new_line1, new_line0, temp_1, temp_0))
                        new_thread.start()
                        time.sleep(0.1)
                        # print str([count1]) + '- tries'
                        # print '\t\t' + str([new_line1]) + str([line])
                        
                                    
    def site_formatten(site):
        # if '/' not in site[-1]:
        #     site = site + '/'
        if '://' not in site[0-4]:
            site = 'http://' + site
            checksum.site = site
            print(str(site) + translate.sql_module_3)

    def selection_1():
        checksum.selection = 1
        with open(temp2_save, 'r') as file:
            for line in file:
                site = line
                site_formatten(site)
                new_line0 = site
                new_thread = threading.Thread(target=first_function, args=(new_line0, save_file0))
                new_thread.start()
                time.sleep(1)
                # first_function(new_line0, save_file0)

    def selection_2():
        checksum.selection = 2
        ur_url = input(translate.sql_module_4)
        site = ur_url
        site_formatten(site)
        new_line0 = site
        first_function(new_line0, save_file0)

    def selection():
        try:       
            print("\n\t" + translate.sql_module_5 + " " + str(temp2_save))
            print("\t" + translate.sql_module_6)
            sel = input(translate.sql_module_7)
            if sel == '1':
                selection_1()
            elif sel == '2':
                selection_2()
            else:
                print(translate.sql_module_8)
                selection()
        except KeyboardInterrupt:
            print(translate.sql_module_9)
            exit


    if __name__ =='__main__':
        selection()


    print(translate.sql_module_10)
    save_file0.close()
except KeyboardInterrupt:
    print('\n' +translate.sql_module_11)