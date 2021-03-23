import requests
import time
import threading
import socket
import os
import re

try:
    class selections():
        def selection_0():
            selection = input("\tCan i correct url? [y/n] -> ")
            if selection == 'y':
                correction_url()
            elif selection == 'n':
                exit()
            else:
                selections.selection_0()
        def selection_1():
            selection = input("\tDo you want to collect emails?[y/n]")
            if selection == 'y':
                information.email_parsing = True
            elif selection == 'n':
                information.email_parsing = False
            else:
                selections.selection_1()
        def selection_settings():
            selection = input("\n\tWhat you wanna do?\n\t[1] Start with default settings\n\t[2] Settings\n===>")
            if selection == '1':
                pass
            elif selection == '2':
                settings()
            else:
                selections.selection_0()

    class information():
        _isworking = False
        email_parsing = False
        encoding_working = False

        full_url = ''
        certificate = ''
        url = ''
        other = ''
        charset = ''

        threads = []

        headers = {
            "User-agent" : "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.75 Mobile DuckDuckGo/5 Safari/537.36"
        }

    def settings():
        os.system("clear")
        banner()
        print ("""
        \tAnd what you wanna do?
        \t[1] Email parsing = {0}
        \t[2] Something else = True""".format(information.email_parsing))
        changing = input("\t\tex: 1=true\n\t===>")
        changing = changing.replace(" ", "")
        if changing.split("=")[0] == "1":
            information.email_parsing = changing.split("=")[1]
        if changing.split("=")[0] == "2":
            test = changing.split("=")[1]
            print (test)
    def error(error0):
        print(f"\tYou have an error -> {error0[0]} - {error0[1]}")

    def banner():
                print("\n\t███████╗██████╗ ██╗██████╗ ███████╗██████╗") 
                print("\t██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗")
                print("\t███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝")
                print("\t╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗")
                print("\t███████║██║     ██║██████╔╝███████╗██║  ██║")
                print("\t╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")


    def correction_url():
        if '/' in information.full_url:
            pass
        else:
            information.full_url = "https://" + information.full_url + "/" 
            information.certificate = "https"
        print("\t[+]Currect url = " + information.full_url)

    def input_infos():
        information.full_url = input("\n\tInput url ->")
        try:
            for i in range(len(information.full_url.split('/'))):
                information.certificate = information.full_url.split(':')[0]
                information.url = information.full_url.split('/')[2]
                information.other = information.full_url.split('/')[3]
        except IndexError:
            error0 = ["[IndexError]", "Wrong Url"]
            error(error0)
            
            selections.selection_0()

    def encoding():
        information.encoding_working = True
        request0 = requests.get(information.full_url, headers = information.headers).text.encode("utf-8")
        for i in range(len(str(request0).split('"'))):
            if 'charset=' in str(request0).split('"')[i]:
                information.charset = str(request0).split('"')[i+1]
        if information.charset == None:
            information.charset = "uft-8"
        try:
            request0 = requests.get(information.full_url, headers = information.headers).text.encode(information.charset)
        except LookupError:
            error0 = ["[Charset]", "Set default charset"]
            information.charset = "utf-8"
        while information._isworking == True:
            time.sleep(1)
        else:
            print("\t[+] Charset -> " + information.charset + "\n")
            information.encoding_working = False



    class for_parser():
        links = []
        ready_links = []
        emails = []

    def main_page_parser():
        request0 = requests.get(information.full_url, headers = information.headers).text.encode(information.charset)
        for i in range(len(str(request0).split('"'))):
            if "http://" in str(request0).split('"')[i] or "https://" in str(request0).split('"')[i] and information.url in str(request0).split('"')[i]:
                for_parser.links.append(str(request0).split('"')[i])
        # print("[++++]" + str(len(for_parser.links)))

    # def timer(thread_name):
    #     i = 0
    #     while (i < 5):
    #         i+=1
    #         time.sleep(1)
    #     else:
    #         information.threads.remove(thread_name)
    #         #threading.Thread(name = thread_name).killed = True

    def parsing_page(link, thread_name):
        try:
            # timer0 = threading.Thread(target = timer, args = thread_name).killed = True
            dublicate_end = 0
            if link in for_parser.ready_links:
                information.threads.remove(thread_name)
                #threading.Thread(name = thread_name).killed = True
                dublicate_end += 1
                if dublicate_end > 10:
                    print("I think, this is the end :(")
                    exit()
            else:
                dublicate_end = 0
                for_parser.ready_links.append(link)
                try:
                    request0 = requests.get(link, headers = information.headers).text.encode(information.charset)
                    for i in range(len(str(request0).split('"'))):
                        if "http://" in str(request0).split('"')[i] or "https://" in str(request0).split('"')[i] and information.url in str(request0).split('"')[i]:
                            for_parser.links.append(str(request0).split('"')[i])
                        if information.email_parsing == True:
                            email_find = re.findall('\w{3,}@[A-z0-9].\S[A-z0-9]{2,}', str(request0))
                            for elem in email_find: 
                                if elem in for_parser.emails or "\\" in email_find or '\\x' in email_find: pass
                                else:
                                    for_parser.emails.append(email_find)
                                    open("emails.txr", 'a+').write(elem + "\n")
                                    #sprint(email_find)
                            if "@" in str(request0).split('"')[i] and "." in str(request0).split('"')[i]:
                                for_parser.emails.append(str(request0).split('"')[i])
                    # print("[++++]" + str(len(for_parser.links)))
                    information.threads.remove(thread_name)
                except requests.exceptions.InvalidSchema:
                    information.threads.remove(thread_name)
                    pass
        except socket.gaierror:
            information.threads.remove(thread_name)
            #threading.Thread(name = thread_name).killed = True
            pass
            

    def manager():
        i = 0
        while i < len(for_parser.links):
            print("[Work] {} | [Emails] {} | Threads -> {}".format(str(len(for_parser.links)), str(len(for_parser.emails)), str(len(information.threads))))
            while len(information.threads) >= 50:
                time.sleep(0.5)
            else:
                time.sleep(0.5)
                thread_name = f"thread_{str(i)}"
                information.threads.append(thread_name)
                thread0 = threading.Thread(name = f"thread_{str(i)}",target = parsing_page, args = (for_parser.links[i], thread_name))
                thread0.start()
                i += 1
        else:
            time.sleep(1)
            
        

    if __name__ == "__main__":
        banner()
        selections.selection_settings()
        input_infos()
        print("\t[+] Getting information")
        print("\t[+] The definition of the encoding")
        thread0 = threading.Thread(target = encoding)
        thread0.start()
        information._isworking = True
        print(
            "\t[+] URL -> " + information.full_url + "\n",
            "\t[+] Cert -> " + information.certificate + "\n")

        open("emails.txr", 'w')

        selections.selection_1() 
        information._isworking = False
        while information.encoding_working == True:
            time.sleep(1)
        else:
            pass
        print("\t[+] Starting crawl main page")
        main_page_parser()
        page_parsing0 = threading.Thread(target = manager)
        page_parsing0.start()

except KeyboardInterrupt:
    exit()