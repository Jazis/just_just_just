#coding = utf-8
import os
from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException
import threading
from selenium.webdriver.common.keys import Keys
import random

class login_date():
    login = '###########'
    paswd = '###########'

class temp():
    page = ''
    msg = ''
    fri = ''
    folder = ''
    audio_page = ''
    page_id = ''
    wayfarer = False
    timer = 250
    status_msg = ""  

class counters():
    counter_timer = 0

def music(driver):
    open(temp.folder + '/music.txt', 'w')
    driver.get('https://vk.com' + temp.audio_page)
    page = []
    changed = []
    combbo = []
    audios_count = 0
    if 'audios' in driver.current_url:
        page.append(driver.page_source.split('"'))
        for i in range(len(page[0])):
            try:
                audios_count += 1
                if 'audio_page_player_title_song_title' in page[0][i]:
                    # changed.append('[00]')
                    name = page[0][i+1].replace('\n', '').replace('</span>              <span class=', '').replace('</a></div>          </div>        </div>      </div>      <div class=', '')
                if 'audio_page_player_title_performer' in page[0][i]:
                    user = page[0][i+7].replace('\n', '').replace('</span>              <span class=', '').replace('</a></div>          </div>        </div>      </div>      <div class=', '')
                upper = '[00] ' + unicode(name.replace('>', '')) + ' | ' + unicode(user.replace('>', ''))
                if changed != upper:
                    changed.append(upper)
                else:
                    pass
            except UnboundLocalError:
                pass
        i = 0
        j = 0
        for i in range(len(page[0])):
            if 'audio_row__title_inner _audio_row__title_inner' in page[0][i]:
                if '%' in page[0][i]:
                    pass
                else:
                    name = page[0][i+1].replace('\n', '').split('<\/span>')[0].replace('>', '').split('</span')[0]
                    users = page[0][i-5].replace('\n', '').split('</a>')[0].replace('>', '')
                    combos = name + ' | ' + users
                    if 'performers' in combos:
                        pass
                    else:
                        j += 1
                        # print '[' + str(j) + '] ' + combos
                        if combos  not in combbo:
                            combbo.append(combos)
                            # print '[' + str(j) + '] ' + combos
                            open(temp.folder + '/music.txt', 'a+').write('[' + str(j) + '] ' + combos.encode('utf-8') + '\n')


def possible_friends(driver):
    print("[Working]")
    friends_id = []
    friends_name = []
    friends_common = []

    page = []
    driver.get('https://vk.com/friends?act=find')
    page.append(driver.page_source.split('"'))
    open(temp.folder + '/possible_friends.txt', 'w')
    for i in range(len(page[0])):
        if 'friends_find_user_name' in page[0][i]:
            friends_id.append(page[0][i+2])
            friends_name.append(page[0][i+3].split('</a>')[0].replace('>', ''))
            friends_common.append(page[0][i+7].split('</a>')[0].replace('>', '').replace('&nbsp;', ' '))
    print('[+]First step - Done')
    for j in range(len(friends_id)):
        open(temp.folder + '/possible_friends.txt', 'a+').write(friends_id[j].encode('utf-8') + ' | ' + friends_name[j].encode('utf-8') + ' | ' + friends_common[j].encode('utf-8') + '\n')
    print('[+]Second step - Done')

def timer():
    temp.timer = input("Input timer in sec (250)-> ") 
    online_timer(driver)

def friends_online(driver):
    open(temp.folder + '/friends_online.txt', 'w')
    friends_id = []
    friends_name = []
    page = []
    driver.get('https://vk.com/friends?section=online')
    page.append(driver.page_source)
    for i in range(len(page[0])):
        if 'friends_user_info' in page[0][i]:
            friends_id.append(page[0][i+4])
            friends_name.append(page[0][i+7].split('</a>')[0].replace('>', ''))
    for j in range(len(friends_id)):
        open(temp.folder + '/friends_online.txt', 'a+').write(friends_id[j].encode('utf-8') + ' | ' + friends_name[j].encode('utf-8'))

def message_check(driver):
    friends_name = []
    friends_msg = []
    open(temp.folder + '/friends_messages.txt', 'w')
    page = []
    driver.get('https://vk.com/im')
    page.append(driver.page_source.split('"'))
    for i in range(len(page[0])):
        if 'nim-dialog--name' in page[0][i]:
            name = page[0][i+7]
            friends_name.append(name.split('<img')[0])
        if 'nim-dialog--text-preview' in page[0][i]: #15
            if '<span' in page[0][i+5].split('</span>')[0]:
                msg = page[0][i+15]
                friends_msg.append(msg.split('</span>')[0].replace('>', ''))
            else:
                msg = page[0][i+5]
                friends_msg.append(msg.split('</span>')[0].replace('>', ''))
            msg = page[0][i+5]
            friends_msg.append(msg.split('</span>')[0].replace('>', ''))
    for j in range(len(friends_name)):
        try:
            if 'class=' in friends_name[j] or 'class=' in friends_msg[j] or 'src=' in friends_name[j] or 'src=' in friends_msg[j]:
                pass
            else:
                open(temp.folder + '/friends_messages.txt', 'a+').write(str(friends_name[j]).replace('>', '').encode('utf-8') + ' | ' + str(friends_msg[j]).encode('utf-8') + '\n')
        except IndexError:
            pass

def stat_check(driver):
    driver.get('https://vk.com/stats?act=visitors&mid=' + temp.page_id)
    driver.save_screenshot(temp.folder + '/statistic.png')

def wayfarer(driver):
    if temp.Wayfarer == True:
        temp.Wayfarer == False
        print("[-] Wayfarer mod - OFF")
    else:
        driver.get('https://vk.com/id' + temp.page_id)
        temp.Wayfarer == True
        while temp.Wayfarer == True:
            page = []
            human = []
            page.append(driver.page_source.split('"'))
            for i in range(len(page[0])):
                if 'people_cell_name' in page[0][i]:
                    human.append(page[0][i+2])
            # print len(human)
            time.sleep(1)
            for j in range(len(human)):
                try:
                    sel = human[random.randint(0, len(human))]
                    driver.get('https://vk.com' + sel)
                except IndexError:
                    pass
                wayfarer(driver)
    

def status(driver):
    driver.get(temp.page)
    driver.find_element_by_id("current_info").click()
    time.sleep(0.5)
    driver.find_element_by_id("currinfo_input").send_keys(temp.status_msg + " | headless mode")
    time.sleep(0.5)
    driver.find_element_by_id("currinfo_save").click()


def actions(driver):
    # os.system('clear')
    print('[+] Im on this page - ' + temp.page + ' | ID:' + temp.page_id + ' | Wayfarer mode: ' + str(temp.wayfarer))
    print('[+] Your messages - ' + temp.msg)
    print('[+] Your new friends - ' + temp.fri)
    print("\t\tWhat do you want?")
    print("\t[1]Checking possible friends")
    print("\t[2]Check your music")
    print("\t[3]Friends online")
    print("\t[4]Recheck main page")
    print("\t[5]Messages check")
    print("\t[6]Stat checker")
    print("\t[7]Wayfarer")
    print("\t[8]Status set")
    print("\t[99]Timer set")

    selection = int(input('->'))
    if selection == 1:
        possible_friends(driver)
    if selection == 2:
        music(driver)
    if selection == 3:
        friends_online(driver)
    if selection == 4:
        page_checking(driver)
    if selection == 5:
        message_check(driver)
    if selection == 6:
        stat_check(driver)
    if selection == 7:
        thread = threading.Thread(target = wayfarer, args = [driver])
        thread.start()
    if selection == 8:
        # thread = threading.Thread(target = status, args = driver)
        # thread.start()
        status(driver)
    if selection == 99:
        timer()
    actions(driver)

def page_checking(driver):
    trash0 = []
    trash1 = []
    trash2 = []
    trash3 = []
    trash4 = []
    page = []
    driver.get('https://vk.com/feed')
    page.append(driver.page_source.split('"'))
    for i in range(len(page[0])):
        if 'l_ph' in page[0][i]:
            trash4.append(page[0][i+4])
        if 'l_pr' in page[0][i]:
            # print page[0][i+4]
            trash0.append(page[0][i+4])
        if 'l_msg' in page[0][i]:
            # print page[0][i+12]
            trash1.append(page[0][i+12])
        if 'l_fr' in page[0][i]:
            # print page[0][i+21]
            trash2.append(page[0][i+21].split('<')[0].replace('>', ''))
        if 'l_aud' in page[0][i]:
            trash3.append(page[0][i+4])
    try:
        os.mkdir(str(trash0[0]).replace('/', ''))
    except OSError:
        pass

    temp.page = 'https://vk.com' + trash0[0]
    if 'left_count_wrap' in trash1[0]:
        temp.msg = '0'
    else:
        temp.msg = trash1[0]
    temp.fri = trash2[0]
    temp.audio_page = str(trash3[1])
    temp.page_id = str(trash4[0]).split('albums')[1]

    temp.folder = str(trash0[0]).replace('/', '')
    
    open(str(trash0[0]).replace('/', '') + '/log', 'w')
    open(str(trash0[0]).replace('/', '') + '/log', 'a+').write('[+] Im on this page - https://vk.com' + trash0[0] + '\n')
    open(str(trash0[0]).replace('/', '') + '/log', 'a+').write('[+] Your messages - ' + trash1[0] + '\n')
    open(str(trash0[0]).replace('/', '') + '/log', 'a+').write('[+] Your new friends - ' + trash2[0] + '\n')


def online_timer(driver):
    while True:
        counters.counter_timer += 1
        time.sleep(temp.timer)
        driver.get('https://vk.com/feed')
        temp.status_msg = "Yea -> " + str(counters.counter_timer)
        status(driver)
        

def login(driver):
    print('[+] Auth')
    driver.find_element_by_id('index_email').send_keys(str(login_date.login))
    driver.find_element_by_id('index_pass').send_keys(str(login_date.paswd))
    driver.find_element_by_id('index_login_button').click()
    while True:
        if driver.current_url == 'https://vk.com/feed':
            print('[+] Auth Success')
            break
    thread = threading.Thread(target= online_timer, args = [driver])
    thread.start()
    pass




if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument('headless')
    # chrome_path = '/home/jazisett/Documents/projects/music/chromedriver'
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://vk.com/')
    login(driver)
    page_checking(driver)
    actions(driver)
