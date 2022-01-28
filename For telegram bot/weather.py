# coding=utf-8
import telebot
import requests
from telebot.types import InputMediaPhoto

class temp():
    command = ''
    country = ''
    time_now = ''
    weather = ''
    temprature = ''

def weather_parse():
    try:
        command = temp.command.split(' ')[1]
    except IndexError:
        
        booting()
    page = []
    req0 = requests.get('https://pogoda.mail.ru/prognoz/' + command + '/').text.encode('utf-8')
    page.append(req0.split('"'))
    for i in range(len(page[0])):
        if 'information__header__left__place__city' in page[0][i]:
            temp.country = page[0][i+1].split('>')[1].split('<')[0].replace('\n', '').replace('\t', '')
        if 'information__header__left__date' in page[0][i]:
            temp.time_now = page[0][i+1].split('>')[1].split('<')[0].replace('\n', '').replace('\t', '')
        if 'information__content__temperature' in page[0][i]:
            temp.weather = page[0][i+4].replace('\n', '').replace('\t', '')
            temp.temprature = page[0][i+5].replace('></span>', '').replace('</div>', '').replace('<div class=', '').replace('\n', '').replace('\t', '').replace('&deg;', '')

