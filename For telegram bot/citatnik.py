#coding=utf-8
import os
import requests
import random

def one():
    linc = []
    open('out.txt', 'w')
    page = []
    req0 = requests.get('http://buast.ru/afor5.htm').text.encode("ISO-8859-9", "ignore")
    page.append(req0.split('"'))
    for i in range(len(page[0])):
        if '#669999' in page[0][i] and '>' in page[0][i+1]:
            linc.append(page[0][i+1].replace('\n', '').replace('                                          ', ' '))
            open('out.txt', 'a+').write(page[0][i+1].replace('\n', '').replace('                                          ', ' ').split('<')[0].replace('&nbsp;', '').replace('>', '') + '\n')
            # print page[0][i+1]
    # print linc

def two():
    for i in range(20):
        open('words/lina['+ str(i) +']', 'w')
    with open('good_out.txt', 'r') as file:
        for line in file:
            lona = []
            lona.append(line.split(' '))
            for i in range(len(lona[0])):
                open('words/lina['+ str(i) +']', 'a+').write(lona[0][i] + '\n')

def gen():
    try:
        ques = []
        len_word = random.randint(4, 52)
        for i in range(len_word):
            with open('words/lina['+ str(i) +']', 'r') as file:
                lines = file.readlines()
                word = random.randint(1, len(open('words/lina['+ str(i) +']').readlines()))
                ques.append(lines[int(word)].replace('\n', ''))
        print ques
    except IndexError:
        gen()
    open('wwwwwww', 'w')
    for i in range(len(ques)):
        open('wwwwwww', 'a+').write(ques[i] + ' ')

def vk_memes():
    citatnik = []
    page = []
    pages = []
    headers = { 
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    req0 = requests.get('https://vk.com/topic-36717806_26897342?offset=1', headers=headers).text.encode('utf-8')
    page.append(req0.split('"'))
    for i in range(len(page[0])):
        if 'pg_lnk fl_l' in page[0][i]:
            pages.append(page[0][i+2])
    selection = random.randint(1, int(pages[2].split('=')[1]))
    page = []
    req0 = requests.get('https://vk.com/topic-36717806_26897342?offset=' + str(selection), headers=headers).text.encode('utf-8')
    page.append(req0.split('"'))
    for i in range(len(page[0])):
        if 'bp_text' in page[0][i]:
            citatnik.append(page[0][i+1].replace('<br>', ' ').split('<')[0].replace('>', ''))
    selection2 = random.randint(0, len(citatnik))
    print citatnik[selection2]

if __name__ == '__main__':
    vk_memes()