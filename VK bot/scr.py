#coding = utf-8
import os
from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException
from thread import start_new_thread
from selenium.webdriver.common.keys import Keys

class login_date():
    login = '#############'
    paswd = '#############'

class temp():
    page = ''
    msg = ''
    fri = ''
    folder = ''
    audio_page = ''
    timer = 250

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
    print "[Working]"
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
    print '[+]First step - Done'
    for j in range(len(friends_id)):
        open(temp.folder + '/possible_friends.txt', 'a+').write(friends_id[j].encode('utf-8') + ' | ' + friends_name[j].encode('utf-8') + ' | ' + friends_common[j].encode('utf-8') + '\n')
    print '[+]Second step - Done'

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



def actions(driver):
    os.system('clear')
    print '[+] Im on this page - ' + temp.page
    print '[+] Your messages - ' + temp.msg
    print '[+] Your new friends - ' + temp.fri
    print "\t\tWhat do you want?"
    print "\t[1]Checking possible friends"
    print "\t[2]Check your music"
    print "\t[3]Friends online"
    print "\t[4]Recheck main page"
    print "\t[99]Timer set"


    selection = input('->')
    if selection == 1:
        possible_friends(driver)
    if selection == 2:
        music(driver)
    if selection == 3:
        friends_online(driver)
    if selection == 4:
        page_checking(driver)
    if selection == 99:
        timer()
    actions(driver)

def page_checking(driver):
    trash0 = []
    trash1 = []
    trash2 = []
    trash3 = []
    page = []
    driver.get('https://vk.com/feed')
    page.append(driver.page_source.split('"'))
    for i in range(len(page[0])):
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

    temp.folder = str(trash0[0]).replace('/', '')
    
    open(str(trash0[0]).replace('/', '') + '/log', 'w')
    open(str(trash0[0]).replace('/', '') + '/log', 'a+').write('[+] Im on this page - https://vk.com' + trash0[0] + '\n')
    open(str(trash0[0]).replace('/', '') + '/log', 'a+').write('[+] Your messages - ' + trash1[0] + '\n')
    open(str(trash0[0]).replace('/', '') + '/log', 'a+').write('[+] Your new friends - ' + trash2[0] + '\n')


def online_timer(driver):
    while True:
        time.sleep(temp.timer)
        driver.get('https://vk.com/feed')
        

def login(driver):
    print '[+] Auth'
    driver.find_element_by_id('index_email').send_keys(str(login_date.login))
    driver.find_element_by_id('index_pass').send_keys(str(login_date.paswd))
    driver.find_element_by_id('index_login_button').click()
    while True:
        if driver.current_url == 'https://vk.com/feed':
            print '[+] Auth Success'
            break
    start_new_thread(online_timer, (driver, ))
    pass




if __name__ == '__main__':
    chrome_path = '/home/jazisett/Documents/projects/music/chromedriver'
    driver = webdriver.Chrome(chrome_path)
    driver.get('https://vk.com/')
    login(driver)
    page_checking(driver)
    actions(driver)
