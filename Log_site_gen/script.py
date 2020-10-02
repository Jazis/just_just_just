# coding=utf-8

import os

class temp():
    unique_number = '123qwe'

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
    # print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1], '') + 'output\\'
    for folder, subfolders, files in os.walk(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '') + 'output\\'):
        # print files
        for file in files:
            # print "add"
            if file.endswith('.txt'):
                file_name_withot_dot = str(file).replace('.txt', '')
                print file_name_withot_dot
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
                    print files
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
            print "1"
            print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1], '') + 'output\\' + files[i]
            with open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1], '')+ 'output\\' + files[i], 'r') as file1:
                for line in file1:
                    open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write('<tr><td>' + str(line) + '</td></tr>')
                open(temp.unique_number + '_' +  file_name + '_index3.html', 'a+').write("""
                </table>
                </table>
                </div>
                </body>
                </html>
                """)


if __name__ == '__main__':
    main_window()
    main_menu()
    other_pages()