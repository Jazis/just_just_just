# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import requests
import random
import string
import zipfile
import os
from requests_toolbelt import MultipartEncoder
import time
from os import listdir

class temp():
    unique_number = ''

def main_window():
    open(temp.unique_number + '_index.html', 'w')
    open(temp.unique_number + '_index.html', 'a+').write("""
    <html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>"""+ str(temp.unique_number) + """</title>
 </head>
 <!-- cols="300,*" -->
 <frameset>
  <frame src=""" + str(temp.unique_number) + '_index2.html' +""" name="MENU">
  <!-- <frame src="index3.html" name="CONTENT"> -->
 </frameset>
</html>""")
# open(temp.unique_number + '_index.html').close()

def main_menu():
    open(temp.unique_number + '_index2.html', 'w')
    open(temp.unique_number + '_index2.html', 'a+').write("""
        <!DOCTYPE HTML>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Логи</title>
    </head>
    <body>
    <table border="1">
    <caption>Весь список файлов</caption>
    <tr>
        <th>Наименование файлов</th>
    </tr>
    """)
    # print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/'
    for folder, subfolders, files in os.walk(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/'):
        # print files
        for file in files:
            # print "add"
            if file.endswith('.txt'):
                file_name_withot_dot = str(file).replace('.txt', '')
                # print file_name_withot_dot
                open(temp.unique_number + '_index2.html', 'a+').write("""
                <tr><td><a href='""" + temp.unique_number + '_' + str(file.strip().split('.')[0]) + """_index3.html' onclick="parent.frames[´CONTENT´].document.location=´index.html´">""" + str(file.strip()) +"""</td></tr>
                """)
    open(temp.unique_number + '_index2.html', 'a+').write("""
            </table>
        </body>
    </html>""")

def other_pages():
    for folder, subfolders, files in os.walk(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/'):
        for i in range(len(files)):
            file_name = str(files[i]).split('.')[0].replace('.txt', '')
            open(temp.unique_number + '_' +  file_name + '_index3.html', 'w')
            open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write("""
            <!DOCTYPE HTML>
            <html>
            <head>
            <meta charset="utf-8">
            <title>Логи</title>
            <style>
                .block-left{width:20%;height:800px;overflow:auto;float:left;}
                .block-right{width:80%;height:800px;overflow:auto;}
            </style>
            </head>
            <body>
            <div class="block-left">
                <table border="1">
                <caption>Весь список файлов</caption>
                <tr>
                <th>Наименование файлов</th>
                </tr>
            """)
            for folder, subfolders, files in os.walk(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/'):
                for file in files:
                    # print files
                    if file.endswith('.txt'):
                        open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write("""
                        <tr><td><a href='""" + temp.unique_number + '_' + str(file.strip().split('.')[0]) + """_index3.html' onclick="parent.frames[´CONTENT´].document.location=´index.html´">""" + str(file.strip()) +"""</td></tr>
                        """)
            open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write("""
            </table>
            </div>
            <div class="block-right">
            <table border="1">
            <tr>
                <th>""" + file_name + """</th>""")
            # print "1"
            # print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/' + files[i]
            with open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '')+ 'output/' + files[i], 'r') as file1:
                for line in file1:
                    open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write('<tr><td>' + str(line) + '</td></tr>')
                open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write("""
                </table>
                </table>
                </div>
                </body>
                </html>
                """)

try:
    status = requests.get('http://localhost/').status_code
    print """
    \t\t|===========================================|
    \t\t|                                           |
    \t\t|               UPLOAD MODULE               |
    \t\t|                                           |
    \t\t|===========================================|
    """
    print """
    \t\t|===========================================|
    \t\t|                                           |
    \t\t|            PLEASE INPUT                   |
    \t\t|           YOUR NICKNAME                   |
    \t\t|                                           |
    \t\t|===========================================|
    """
    NICKNAME = raw_input('========>>>> ')

    print """
    \t\t|===========================================|
    \t\t|                                           |
    \t\t|            Log Uploader                   |
    \t\t|                                           |
    \t\t|     Status code -> """ + str(status) + """ \t\t    |
    \t\t|                                           |
    \t\t|===========================================|
    """

    name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    temp.unique_number = name
    link = name + '.zip'
    folders = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '')+ 'logs/' + name + '.zip'
    # print folders
    open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'logs/' + name + '.zip', 'w')
    fantasy_zip = zipfile.ZipFile(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'logs/' + name + '.zip', 'w')
    
    for folder, subfolders, files in os.walk(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/'):
    
        for file in files:
            if file.endswith('.txt'):
                fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output/'), compress_type = zipfile.ZIP_DEFLATED)
    
    fantasy_zip.close()
    print """
    \t\t|===========================================|
    \t\t|                                           |
    \t\t|                                           |
    \t\t|             File compressed               |
    \t\t|                                           |
    \t\t|                                           |
    \t\t|===========================================|
    """
    url = 'http://localhost/upload.php'
    qwe = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'logs/' + name + '.zip'
    # print qwe
    unique_id = qwe.split('/')[-1].split('.')[0]
    with open(qwe, 'rb') as fd:
        files = {'path' : (qwe,  fd.read() ) }
        requests.post(url, files=files)
    time.sleep(3)

    print """
    \t\t|===========================================|
    \t\t|                                           |
    \t\t|                                           |
    \t\t|           Creating pages                  |
    \t\t|                                           |
    \t\t|                                           |
    \t\t|===========================================|
    """
    main_window()
    main_menu()
    other_pages()
    print """
    \t\t|===========================================|
    \t\t|                                           |
    \t\t|                                           |
    \t\t|                Created                    |
    \t\t|                                           |
    \t\t|                                           |
    \t\t|===========================================|
    """
    print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '')
    listok = listdir(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], ''))
    for i in range(len(listok)):
        if '.html' in listok[i]:
            with open(listok[i], 'rb') as fd:
                files_fr = {'path' : (listok[i],  fd.read() ) }
                requests.post(url, files=files_fr)
    
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='db_diplom',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
            
    try:
        with connection.cursor() as cursor:
            # Create a new record
            # sql = "INSERT INTO output_infos VALUES(''"+ str(unique_id) +"', '" + str(NICKNAME) + "', 'http://192.168.1.2/uploads/" + str(link) + "');"
            sql = "INSERT INTO output_infos (unique_id, User) VALUES ('{0}', '{1}');".format(unique_id, NICKNAME)
            cursor.execute(sql)
            result = cursor.fetchone()
            # print(result)
        connection.commit()
    finally:
        connection.close()
# except Exception as e:
#     print e.message, e.args
except KeyboardInterrupt:
    exit()