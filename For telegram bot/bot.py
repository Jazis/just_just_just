# coding=utf-8
import telebot
import requests
import pymysql
import pymysql.cursors
import threading
import time

class trash():
    telegram_key = '360479486:AAEdl-X7rFZkwEuoqkIIYCNrCPP1F5Fsbm0'
    admin_id = '169682005'
    mysql_host = 'localhost'
    mysql_port = 3306
    mysql_uname = 'root'
    mysql_upass = ''
    mysql_charset = 'utf8mb4'

class db_user():
    db_name = ''
    def conn(**self):
        connection = pymysql.connect(host=trash.mysql_host, port = trash.mysql_port,
                                    user=trash.mysql_uname,
                                    password=trash.mysql_upass,
                                    db=db_user.db_name,
                                    charset=trash.mysql_charset,
                                    cursorclass=pymysql.cursors.DictCursor)
        return connection

class temp():
    big_bases = []
    dbases = []
    fname = []
    lname = []
    email = []
    fio = []
    phone = []
    command = ''
    def banner(**self):
        ban = """
        Привет! Доступных баз -> {0}
        Крупных баз -> {5}
        Доступные команды:
        /fname <arg> ({1})
        /lname <arg> ({2})
        /phone <arg> ({3})
        /email <arg> ({4})
        /fio <arg> ({6})
        """.format(len(temp.dbases), len(temp.fname), len(temp.lname), len(temp.phone), len(temp.email), len(temp.big_bases), len(temp.lname) + len(temp.fname))
        return ban

def phone(bot, text, uid):
    command = str(text).split(' ')[0].replace('/', '')
    text = str(text).replace("/" + command + " ", '')
    for i in range(len(temp.phone)):
        db_user.db_name = str(temp.phone[i][0])
        connection = db_user.conn()
        print("Thread '{0}', '{1}', '{2}'".format(str(command), str(text), str(uid)))
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `{0}`.`{1}` WHERE `{2}` LIKE '%{3}%'".format(str(temp.phone[i][0]), str(temp.phone[i][1]), command, text)
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                print (rows)
                for row in rows:
                    bot.send_message(uid, str(row))
                connection.commit()
                time.sleep(0.1)
        except pymysql.err.OperationalError:
            pass
        except pymysql.err.ProgrammingError:
            pass
    bot.send_message(uid, "--------------------")        
    print("End")

def email(bot, text, uid):
    command = str(text).split(' ')[0].replace('/', '')
    text = str(text).replace("/" + command + " ", '')
    for i in range(len(temp.email)):
        db_user.db_name = str(temp.email[i][0])
        connection = db_user.conn()
        print("Thread '{0}', '{1}', '{2}'".format(str(command), str(text), str(uid)))
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `{0}`.`{1}` WHERE `{2}` LIKE '%{3}%'".format(str(temp.email[i][0]), str(temp.email[i][1]), command, text)
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                print (rows)
                for row in rows:
                    bot.send_message(uid, str(row))
                connection.commit()
                time.sleep(0.1)
        except pymysql.err.OperationalError:
            pass
        except pymysql.err.ProgrammingError:
            pass
    bot.send_message(uid, "--------------------")
    print("End")

def FIO(bot, text, uid):
    command = str(text).split(' ')[0].replace('/', '')
    text = str(text).replace("/" + command + " ", '')
    for i in range(len(temp.fio)):
        db_user.db_name = str(temp.fio[i][0])
        connection = db_user.conn()
        print("Thread '{0}', '{1}', '{2}'".format(str(command), str(text), str(uid)))
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `{0}`.`{1}` WHERE `{2}` LIKE '%{3}%'".format(str(temp.fio[i][0]), str(temp.fio[i][1]), command, text)
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                print (rows)
                for row in rows:
                    bot.send_message(uid, str(row))
                connection.commit()
                time.sleep(0.1)
        except pymysql.err.OperationalError:
            pass
        except pymysql.err.ProgrammingError:
            pass
    bot.send_message(uid, "--------------------")
    print("End")

def lname(bot, text, uid):
    command = str(text).split(' ')[0].replace('/', '')
    text = str(text).replace("/" + command + " ", '')
    for i in range(len(temp.lname)):
        db_user.db_name = str(temp.lname[i][0])
        connection = db_user.conn()
        print("Thread '{0}', '{1}', '{2}'".format(str(command), str(text), str(uid)))
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `{0}`.`{1}` WHERE `{2}` LIKE '%{3}%'".format(str(temp.lname[i][0]), str(temp.lname[i][1]), command, text)
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                print (rows)
                for row in rows:
                    bot.send_message(uid, str(row))
                connection.commit()
                time.sleep(0.1)
        except pymysql.err.OperationalError:
            pass
        except pymysql.err.ProgrammingError:
            pass
    bot.send_message(uid, "--------------------")        
    print("End")

def fname(bot, text, uid):
    command = str(text).split(' ')[0].replace('/', '')
    text = str(text).replace("/" + command + " ", '')
    for i in range(len(temp.fname)):
        db_user.db_name = str(temp.fname[i][0])
        connection = db_user.conn()
        print("Thread '{0}', '{1}', '{2}'".format(str(command), str(text), str(uid)))
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `{0}`.`{1}` WHERE `{2}` LIKE '%{3}%'".format(str(temp.fname[i][0]), str(temp.fname[i][1]), command, text)
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                print (rows)
                for row in rows:
                    bot.send_message(uid, str(row))
                connection.commit()
                time.sleep(0.1)
        except pymysql.err.OperationalError:
            pass
        except pymysql.err.ProgrammingError:
            pass
    bot.send_message(uid, "--------------------")
    print("End")

def db_check():
    connection = db_user.conn()
    db_row = 0
    try:
        with connection.cursor() as cursor:
            sql = "SHOW DATABASES LIKE '%_db'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            # print (rows)
            for row in rows:
                temp.dbases.append(str(row).split('\'')[3])
            connection.commit()
            time.sleep(0.1)
            for i in range(len(temp.dbases)):
                db_row = 0
                sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='{0}'".format(temp.dbases[i])
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    db_row += 1
                    if db_row > 50:
                        if temp.dbases[i] not in temp.big_bases:
                            temp.big_bases.append(temp.dbases[i])
            for i in range(len(temp.dbases)):
                sql = "select * from information_schema.columns where table_schema = '{0}'".format(temp.dbases[i])
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    # print (str(row))
                    for j in range(len(str(row).split('\''))):
                        if 'COLUMN_NAME' in str(row).split('\'')[j]:
                            #  string example -> DBname, TABLEname, Value
                            if 'FIO' in str(row).split('\'')[j+2]:
                                if str(row).split('\'')[j+2] in temp.fname: pass
                                else:
                                    temp.fname.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                                if str(row).split('\'')[j+2] in temp.lname: pass
                                else:
                                    temp.lname.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                                if str(row).split('\'')[j+2] in temp.fio: pass
                                else:
                                    temp.fio.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                            if 'fname' in str(row).split('\'')[j+2]:
                                if str(row).split('\'')[j+2] in temp.fname: pass
                                else:
                                    temp.fname.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                            if 'lname' in str(row).split('\'')[j+2]:
                                if str(row).split('\'')[j+2] in temp.lname: pass
                                else:
                                    temp.lname.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                            if 'email' in str(row).split('\'')[j+2]:
                                if str(row).split('\'')[j+2] in temp.email: pass
                                else:
                                    temp.email.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                            if 'phone' in str(row).split('\'')[j+2]:
                                if str(row).split('\'')[j+2] in temp.phone: pass
                                else:
                                    temp.phone.append([temp.dbases[i], str(row).split('\'')[j-2], str(row).split('\'')[j+2]])
                connection.commit()
    except pymysql.err.OperationalError:
        pass
    except pymysql.err.ProgrammingError:
        pass
    
    

def booting():
    # try:
    bot = telebot.TeleBot(trash.telegram_key)
    # https://hidemy.name/ru/proxy-list/
    bot.send_message(trash.admin_id, 'Work')
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, temp.banner)
    @bot.message_handler(commands=['help'])
    def start_message(message):
        ban = temp.banner()
        bot.send_message(message.chat.id, ban)

    @bot.message_handler(commands=['phone'])
    def start_message(message):
        print(message.text)
        thread0 = threading.Thread(target = phone, args =(bot, message.text, message.chat.id))
        thread0.start()
    @bot.message_handler(commands=['fio'])
    def start_message(message):
        print(message.text)
        thread0 = threading.Thread(target = FIO, args =(bot, message.text, message.chat.id))
        thread0.start()
    @bot.message_handler(commands=['email'])
    def start_message(message):
        print(message.text)
        thread0 = threading.Thread(target = email, args =(bot, message.text, message.chat.id))
        thread0.start()
    @bot.message_handler(commands=['lname'])
    def start_message(message):
        print(message.text)
        thread0 = threading.Thread(target = lame, args =(bot, message.text, message.chat.id))
        thread0.start()
    @bot.message_handler(commands=['fname'])
    def start_message(message):
        print(message.text)
        thread0 = threading.Thread(target = fname, args =(bot, message.text, message.chat.id))
        thread0.start()
    @bot.message_handler(commands=['test'])
    def start_message(message):
        print(message.text)
        thread0 = threading.Thread(target = test, args =(bot, message.text, message.chat.id))
        thread0.start()
    @bot.message_handler(commands=['check'])
    def start_message(message):
        thread0 = threading.Thread(target = db_check, args =(message.chat.id, bot))
        thread0.start()
    bot.polling()
    # except requests.exceptions.SSLError:
    #     pass
    # # except requests.exceptions.ConnectionError:
    # #     booting()
    # except NameError:
    #     booting()
        
if __name__ == "__main__":
    db_check()
    booting()
