import os
try:
    class temp():
        selection = 0
        new_dir0 = ''
        py_selection = 0
        language = ''
        multilang = ''
    class translate():
        main_banner_1 = ''
        main_banner_2 = ''
        main_banner_3 = ''
        main_banner_4 = ''
        main_banner_5 = ''
        main_banner_6 = ''
        main_banner_7 = ''

    def language():
        multilang = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'settings/multilang.ini')
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
                if '[main_banner_1]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_1 = '\t\t|\t'+line.split('=')[1].strip() + '\t\t\t   |'
                if '[main_banner_2]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_2 ='\t\t|'+line.split('=')[1].strip() + '|'
                if '[main_banner_3]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_3 ='\t\t|'+line.split('=')[1].strip() + '|'
                if '[main_banner_4]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_4 ='\t\t|'+line.split('=')[1].strip() + '|'
                if '[main_banner_5]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_5 ='\t\t|'+line.split('=')[1].strip() + '|'
                if '[main_banner_6]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_6 ='\t\t|'+line.split('=')[1].strip() + '|'
                if '[main_banner_7]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_7 ='\t\t|'+line.split('=')[1].strip() + '|'
        banner()

    def banner():
        with open(temp.multilang, 'r') as file:
            for line in file:
                if '[main_banner_1]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_1 = '\t\t|\t'+line.split('=')[1].strip() + '\t\t\t   |'
                if '[main_banner_2]' in line and '[' + temp.language + ']' in line:
                    translate.main_banner_2 ='\t\t|'+line.split('=')[1].strip() + '|'
        print "\t\t------------------------------------------"
        print translate.main_banner_1
        print translate.main_banner_2
        print "\t\t------------------------------------------"
        change()

    def start_module():
        new_dir1 = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], 'modules/' + os.listdir(temp.new_dir0)[int(temp.selection)-1])
        # os.system("xterm -geometry 150x30 -e python " +  new_dir1)
        os.system("gnome-terminal --geometry 100x20 -e 'python " +  new_dir1 + "'")

    def selection_check():
        new_dir1 = ''
        try:
            temp.selection = raw_input('\t' + translate.main_banner_3)
            print "Wait..."     
            start_module()
        except ValueError:
            print translate.main_banner_4
            selection_check()
        except IndexError:
            print translate.main_banner_5
        except KeyboardInterrupt:
            print '\nOK!'
            exit()
            

    def change():
        temp.py_selection = 0
        new_dir1 = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1], 'modules')
        temp.new_dir0 = new_dir1
        # print new_dir1
        for i in range(len(os.listdir(new_dir1))):
            if '.py' in os.listdir(new_dir1)[i]:
                temp.py_selection +=1
        print '\t' + translate.main_banner_6 + ' - ' + str(temp.py_selection)
        for i in range(len(os.listdir(new_dir1))):
            if '.py' in os.listdir(new_dir1)[i]:
                print  '\t\t' + str([i+1]) + str(os.listdir(new_dir1)[i].replace('.py', '').replace(os.listdir(new_dir1)[i][0], os.listdir(new_dir1)[i][0].upper()))
            else:
                pass
        # print "Please input number of module"
        selection_check()
    while True:
        language()

    language()
# except Exception as e:
#     print e.message, e.args
except KeyboardInterrupt:
    print '\n' + translate.main_banner_6