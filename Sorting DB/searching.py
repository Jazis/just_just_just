# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import os, sys
import requests
import time
from threading import Thread

try:
    def create_tables():
        counter = 0
        counter0 = 0
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        # open('out.txt', 'w')
        simbols = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9,-,_,.,$,%,^,&,*,+"
        for i in range(len(simbols.split(','))):
            #print(simbols.split(',')[i])
            for x in range(len(simbols.split(','))):
                for l in range(len(simbols.split(','))):
                    # print(simbols.split(',')[i], simbols.split(',')[x], simbols.split(',')[l])
                    symbol = simbols.split(',')[i] + simbols.split(',')[x] + simbols.split(',')[l]
                    try:
                        with connection.cursor() as cursor:
                            # Create a new record
                            # sql = "INSERT INTO output_infos VALUES(''"+ str(unique_id) +"', '" + str(NICKNAME) + "', 'http://192.168.1.2/uploads/" + str(link) + "');"
                            sql =  "CREATE TABLE {0} (combos text);".format(symbol)
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            # print(result)
                            connection.commit()
                            # time.sleep(0.1)
                            counter +=1
                            counter0 += 1
                            if counter0 == 10000:
                                print('[+]PUM PUM PURUM - 10000')
                                counter0 = 0
                    except pymysql.err.OperationalError:
                        pass
                    except pymysql.err.ProgrammingError:
                        pass
        #            finally:
        #               connection.close()
        print('[0]TABLES' + [counter])

    def base_adding():
        counter = 0 
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        base = input('bse plz -> ')
        base = base.replace('"', '').replace("'", "").replace(' ', '')
        with open(base, 'r') as file:
            for line in file:
                if '@' in line and ':' in line and '.' in line:
                    bd_searcher = line[0] + line[1]
                    bd_searcher = bd_searcher.lower()
                    # try:
                    with connection.cursor() as cursor:
    #                   print('12112')
                        #print(str(bd_searcher))
                        sql = "SELECT * FROM `{0}` WHERE `combos` LIKE '{1}'".format(bd_searcher, str(line).replace('\n', ''))
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        #print(len(rows))
                        if len(rows) > 0:
                            pass
                            counter += 1
                            print("[-] ALREADY = ", [counter])
                        else:     
                            sql = "INSERT IGNORE INTO `{0}` (`combos`) VALUES ('{1}')".format(bd_searcher, str(line).replace('\n', ''))
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            # print(result)
                            connection.commit()
                            counter += 1
                            print("[+] COUNTER = ", [counter])
                    # except pymysql.err.OperationalError:
                    #     pass
                    # except pymysql.err.ProgrammingError:
                    #     pass
        print('Ready', [counter])
        connection.close()

    def searching():
        try:
            quer = input('Y0ur query -> ')
            quer_bukv = quer[0] + quer[1]
            quer_bukv = quer_bukv.lower()
            print('------------------------')
            connection = pymysql.connect(host='192.168.1.3',
                                    user='Jazis',
                                    password='1234567890',
                                    db='crew_db',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                #   print('12112')
                    #print(str(bd_searcher))
                    sql = "SELECT * FROM `{0}` WHERE `combos` LIKE '%{1}%'".format(quer_bukv, quer)
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    # print(len(rows))
                    if len(rows) == 0:
                        print('>:(')
                    for row in rows:
                        for i in range(len(str(row).split("'"))):
                            if ':' in str(row).split("'")[i] and '@' in str(row).split("'")[i] and '.' in str(row).split("'")[i]:
                                rr = str(row).split("'")[i]
                                print(rr)
                    connection.commit()
                    time.sleep(0.1)
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass
            print('------------------------')
        except IndexError:
            print("Error. Try again")
            searching()

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

    def sorting_base():
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
            try:
                with open(base, 'r') as file:
                    try:
                        for line in file:
                            line = line.replace('\r', '')
                            try:
                                if len(threads0) >= 400:
                                    # sys.stdout.write("\n")   
                                    time.sleep(0.1)
                                    threads0 = []
                                    threads1.append(line)
                                    thread2 = Thread(target=func, args=(line, file, file_size))
                                    thread2.start()
                                else:
                                    try:
                                        threads1 = []
                                        threads0.append(line)
                                        thread1 = Thread(target=func, args=(line, file, file_size))
                                        thread1.start()
                                    except RuntimeError:
                                        pass
                            except RuntimeError:
                                pass
                    except OSError:
                        pass
            except UnicodeDecodeError:
                pass

    class temp_0_0():
        counter = 0
        summary = 0 

    def func_vk(line, file, file_size):
        for i in range(len(line.split(','))):
            email = line.split(',')[2].replace("'", '').replace(' ', '')
            phone = line.split(',')[4].replace("'", '').replace(' ', '').replace(');', '')
        temp_0_0.counter = temp_0_0.counter + 1
        if temp_0_0.counter == 10000:
            temp_0_0.summary = 0
            for i in range(len(os.listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'sorting_vk/')))):
                file =  os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'sorting_vk/') + os.listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'sorting/'))[i]
                temp_0_0.summary = temp_0_0.summary + os.path.getsize(file)
            p = float(temp_0_0.summary)/float(file_size)*100
            sys.stdout.write('\r' + '|-> ' + str(int(p)) + '%')
            temp_0_0.counter = 0
        try:
            table_name = email[:2] + '$' + phone.replace(phone[-1], '')[-2:]
            # print(table_name)
            open( 'sorting_vk/' + table_name + '.txt', 'a+').write(line)
        except IndexError:
            pass
        except OSError:
            pass   

    def sorting_vk():
            try:
                os.mkdir('sorting_vk')
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
                                if len(threads0) >= 300:
                                    # sys.stdout.write("\n")   
                                    time.sleep(0.1)
                                    threads0 = []
                                    threads1.append(line)
                                    thread2 = Thread(target=func_vk, args=(line, file, file_size))
                                    thread2.start()
                                else:
                                    try:
                                        threads1 = []
                                        threads0.append(line)
                                        thread1 = Thread(target=func_vk, args=(line, file, file_size))
                                        thread1.start()
                                    except RuntimeError:
                                        pass
                            except RuntimeError:
                                pass
                    except UnicodeDecodeError:
                        pass
                    except:
                        pass

    def base_sorting():
        print('\t------------------------|')
        print('\t|[1]Sorting base        |')
        print('\t|[2]Sorting VK          |')
        print('\t------------------------|')
        selection = input('Select -> ')
        if selection == 1:
            sorting_base()
        if selection == 2:
            sorting_vk()
    
    def base_sorting_struct():
        while True:
            base = input('BSE PLZ RETARD FR SRT ->')
            base = base.replace('"', '').replace("'", "").replace(' ', '')
            with open(base, 'r') as file:
                for line in file:
                    bkv = line[0] + line[1]
                    bkv = bkv.lower()
                    open( 'sorting/' + bkv + '_struct.txt', 'a+').write("INSERT INTO `" + bkv + "`(`combos`) VALUES ('" + line.replace('\n', '') + "');\n")

    def struct_adder():
        try:
            connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='crew_db',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            counter = 0
            print('[+] ' + str(os.getcwd()))
            print('[+] ' + str(os.listdir(os.getcwd())))
            for i in range(len(os.listdir(os.getcwd()))):
                if '.' not in os.listdir(os.getcwd())[i]:
                    folder = os.listdir(os.getcwd())[i]
            print('[+] ' + str(folder))
            for i in range(len(str(os.listdir(os.getcwd())) + '/' + str(folder))):
                counter += 1
            print('[+] Counter -> ' + str(counter))
            counter = 0
            #print('[+] ' + str(os.listdir(os.getcwd() + '/' + str(folder))))
            page = str(os.listdir(os.getcwd() + '/' + str(folder)))
            for i in range(len(str(os.listdir(os.getcwd() + '/' + str(folder))))):
                file = str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                # print(file)
                folder_file = os.getcwd() + '/' + folder + '/' + str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                with open(folder_file, 'r') as file:
                    print('[+] ' + str(folder_file))
                    for line in file:
                        try:
                            with connection.cursor() as cursor:
                                sql = line
                                cursor.execute(sql)
                                counter += 1
                                result = cursor.fetchone()
                                # print(result)
                                connection.commit()
                        except pymysql.err.OperationalError:
                            pass
                        except pymysql.err.ProgrammingError:
                            pass    
            print('Ready', [counter])
            connection.close()
        except IndexError:
            pass

    def auto_struct_adder():
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        counter = 0
        print('[+] ' + str(os.getcwd()))
        print('[+] ' + str(os.listdir(os.getcwd())))
        for i in range(len(os.listdir(os.getcwd()))):
            if '.' not in os.listdir(os.getcwd())[i]:
                folder = os.listdir(os.getcwd())[i]
        print('[+] ' + str(folder))
        for i in range(len(str(os.listdir(os.getcwd())) + '/' + str(folder))):
            counter += 1
        print('[+] Counter -> ' + str(counter))
        print('[+] ' + str(os.listdir(os.getcwd() + '/' + str(folder))))
        page = str(os.listdir(os.getcwd() + '/' + str(folder)))
        counter = 0
        for i in range(len(str(os.listdir(os.getcwd() + '/' + str(folder))))):
            try:
                file = str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                # print(file)
                counter += 1
                folder_file = os.getcwd() + '/' + folder + '/' + str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                with open(folder_file, 'r') as file:
                    try:
                        with connection.cursor() as cursor:
                            cursor.execute(file.read())
                            result = cursor.fetchone()
                            connection.commit()
                    except pymysql.err.OperationalError:
                        pass
                    except pymysql.err.ProgrammingError:
                        pass
                    except pymysql.err.InterfaceError:
                        pass
            except IndexError:
                pass
        print('Ready', [counter])
        connection.close()

    def single_auto_struct_adder():
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        base = input('bse plz -> ')
        base = base.replace('"', '').replace("'", "").replace(' ', '')
        with open(base, 'r') as file:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(file.read())
                    result = cursor.fetchone()
                    connection.commit()
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass
        print('Ready')
        connection.close()

    def load_data_infile():
        try:
            connection = pymysql.connect(host='192.168.1.3',
                                            user='Jazis',
                                            password='1234567890',
                                            db='crew_db',
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
            counter = 0
            print('[+] ' + str(os.getcwd()))
            print('[+] ' + str(os.listdir(os.getcwd())))
            for i in range(len(os.listdir(os.getcwd()))):
                if '.' not in os.listdir(os.getcwd())[i]:
                    folder = os.listdir(os.getcwd())[i]
            print('[+] ' + str(folder))
            for i in range(len(str(os.listdir(os.getcwd())) + '/' + str(folder))):
                counter += 1
            print('[+] Counter -> ' + str(counter))
            #print('[+] ' + str(os.listdir(os.getcwd() + '/' + str(folder))))
            page = str(os.listdir(os.getcwd() + '/' + str(folder)))
            for i in range(len(str(os.listdir(os.getcwd() + '/' + str(folder))))):
                file = str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                # print(file)
                quer_bukv = str(file)[0] + str(file)[1]
                quer_bukv = quer_bukv.lower()
                folder_file = os.getcwd() + '/' + folder + '/' + str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                try:
                    with open(folder_file, 'r') as file:
                        with connection.cursor() as cursor:
                            try:
                                sql = "CREATE TABLE {0} (combos text);".format(str(quer_bukv))
                                cursor.execute(sql)
                                result = cursor.fetchone()
                                connection.commit()
                            except pymysql.err.OperationalError:
                                pass
                            except pymysql.err.ProgrammingError:
                                pass
                            except pymysql.err.InternalError:
                                pass
                            try:
                                # print(str(folder_file))
                                sql = "LOAD DATA INFILE '{0}' IGNORE INTO TABLE {1} (combos);".format(str(folder_file), str(quer_bukv))
                                print('[+] DATA LOADED ' + str(folder_file))
                                cursor.execute(sql)
                                result = cursor.fetchone()
                                connection.commit()
                            except pymysql.err.OperationalError:
                                pass
                            except pymysql.err.ProgrammingError:
                                pass
                            except pymysql.err.InternalError:
                                pass
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass
                except pymysql.err.InternalError:
                    pass
        except IndexError:
            pass

    def load_data_infile_once():
        base = '/media/jazis/nya/#2/fullz/base/'
        counter2 = 0
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        counter = 0
        print('[+] ' + str(base))
        print('[+] ' + str(os.listdir(base)))
        for i in range(len(os.listdir(base))):
            if '.' not in os.listdir(base)[i]:
                folder = os.listdir(base)[i]
        print('[+] ' + str(folder))
        for i in range(len(str(os.listdir(base)) + str(folder))):
            counter += 1
        print('[+] Counter -> ' + str(counter))
        try:
            page = str(os.listdir(base + str(folder)))
            counter = 0
            for i in range(len(str(os.listdir(base  + str(folder))))):
                try:
                    file = str(os.listdir(base  + str(folder))[i])
                    # print(file)
                    counter += 1
                    folder_file = base + folder + '/' + str(os.listdir(base + '/' + str(folder))[i])
                    try:
                        with open(folder_file, 'r') as file:
                            with connection.cursor() as cursor:
                                sql = "CREATE TABLE {0} (combos text);".format(str(quer_bukv))
                                cursor.execute(sql)
                                result = cursor.fetchone()
                                connection.commit()
                                sql = "LOAD DATA INFILE '{0}' IGNORE INTO TABLE {1} (combos);".format(str(folder_file), str(quer_bukv))
                                print('[+] DATA LOADED ' + str(folder_file))
                                cursor.execute(sql)
                                result = cursor.fetchone()
                                connection.commit()
                    except pymysql.err.OperationalError:
                        pass
                    except pymysql.err.ProgrammingError:
                        pass
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass 
        except NotADirectoryError:
            pass   

    def fullz_transfer():
        base = '/media/jazis/nya/#2/fullz/base/'
        counter2 = 0
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        counter = 0
        print('[+] ' + str(base))
        print('[+] ' + str(os.listdir(base)))
        for i in range(len(os.listdir(base))):
            if '.' not in os.listdir(base)[i]:
                folder = os.listdir(base)[i]
        print('[+] ' + str(folder))
        for i in range(len(str(os.listdir(base)) + str(folder))):
            counter += 1
        print('[+] Counter -> ' + str(counter))
        try:
            page = str(os.listdir(base + str(folder)))
            counter = 0
            for i in range(len(str(os.listdir(base  + str(folder))))):
                try:
                    file = str(os.listdir(base  + str(folder))[i])
                    # print(file)
                    counter += 1
                    folder_file = base + folder + '/' + str(os.listdir(base + '/' + str(folder))[i])
                    with open(folder_file, 'r') as file:
                        base2 = base2.replace('"', '').replace("'", "").replace(' ', '')
                        with open(base2, 'r') as file:
                            for line in file:
                                bkv = line[0] + line[1] + line[2]
                                bkv = bkv.lower()
                                open( 'sorting/' + bkv + '.txt', 'a+').write(line)
                                counter2 += 1
                                print('[+] COUNT ->' + str([counter2]))
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass 
        except NotADirectoryError:
            pass   

    def base_separator():
        name = ''
        counter = 0
        counter0 = 0
        base = input('bse plz -> ')
        base = base.replace('"', '').replace("'", "").replace(' ', '')
        with open(base, 'r') as file:
            for line in file:
                if counter == 1000000:
                    counter0 += 1
                    counter = 0
                    print("[+] " + str(counter0) + " +1kk")
                    name = str(time.time())
                open('output/base10kk' + str(name) + '.txt', 'a+').write(line)
                counter +=1


        


    def sorting_merge():
        try:
            connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='crew_db',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
            counter = 0
            print('[+] ' + str(os.getcwd()))
            print('[+] ' + str(os.listdir(os.getcwd())))
            for i in range(len(os.listdir(os.getcwd()))):
                if '.' not in os.listdir(os.getcwd())[i]:
                    folder = os.listdir(os.getcwd())[i]
            print('[+] ' + str(folder))
            for i in range(len(str(os.listdir(os.getcwd())) + '/' + str(folder))):
                counter += 1
            print('[+] Counter -> ' + str(counter))
            #print('[+] ' + str(os.listdir(os.getcwd() + '/' + str(folder))))
            page = str(os.listdir(os.getcwd() + '/' + str(folder)))
            for i in range(len(str(os.listdir(os.getcwd() + '/' + str(folder))))):
                file = str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                # print(file)
                folder_file = os.getcwd() + '/' + folder + '/' + str(os.listdir(os.getcwd() + '/' + str(folder))[i])
                with open(folder_file, 'r') as file:
                    for line in file:
                        if '@' in line and ':' in line and '.' in line:
                            bd_searcher = line[0] + line[1]
                            bd_searcher = bd_searcher.lower()
                            try:
                                with connection.cursor() as cursor:
                #                   print('12112')
                                    #print(str(bd_searcher))
                                    sql = "SELECT * FROM `{0}` WHERE `combos` LIKE '{1}'".format(bd_searcher, str(line).replace('\n', ''))
                                    cursor.execute(sql)
                                    rows = cursor.fetchall()
                                    #print(len(rows))
                                    if len(rows) > 0:
                                        pass
                                        counter += 1
                                        print("[-] ALREADY = ", [counter])
                                    else:     
                                        sql = "INSERT IGNORE INTO `{0}` (`combos`) VALUES ('{1}')".format(bd_searcher, str(line).replace('\n', ''))
                                        cursor.execute(sql)
                                        result = cursor.fetchone()
                                        # print(result)
                                        connection.commit()
                                        counter += 1
                                        print("[+] COUNTER = ", [counter])
                            except pymysql.err.OperationalError:
                                pass
                            except pymysql.err.ProgrammingError:
                                pass
            print('Ready', [counter])
            connection.close()
        except IndexError:
            pass

    def main_selection():
        os.system('clear')
        print('\t|\t\t   DataBase utils\t\t       |')
        print('\t|______________________________________________________|')
        print('\t|[1] CREATE TABLE                                      |')
        print('\t|[2] Base adding                                       |')
        print('\t|[3] Searching                                         |')
        print('\t|[4] Base sorting                                      |')
        print('\t|[5] Sorting merge                                     |')
        print('\t|[6] Base sotring (struct)                             |')
        print('\t|[7] Base adding (struct)                              |')
        print('\t|[8] SINGLE AUTO FILE (struct)                         |')
        print('\t|[9] AUTO FILES (struct)                               |')
        print('\t|[10] LOAD DATA INFILE (/SORTING) AUTOMATE | MULTI     |')
        print('\t|[11] LOAD DATA INFILE (/SORTING) AUTOMATE | ONCE      |')
        print('\t|[12] DB SEPARATOR 1kk                                 |')
        print('\t|______________________________________________________|')
        selection = input("Your choice -> ")
        if selection == '1':
            create_tables()
        if selection == '2':
            base_adding()
        if selection == '3':       
            searching()
        if selection == '4':
            base_sorting()
        if selection == '5':
            sorting_merge()
        if selection == '6':
            base_sorting_struct()
        if selection == '7':
            struct_adder()
        if selection == '8':
            single_auto_struct_adder()
        if selection == '9':
            auto_struct_adder()
        if selection == '10':
            load_data_infile()
        if selection == '11':
            load_data_infile_once()
        if selection == '12':
            base_separator()
        if selection == '00':
            fullz_transfer()
        else:
            exit()

    if __name__ == '__main__':
        main_selection()
        

except KeyboardInterrupt:
    main_selection()
