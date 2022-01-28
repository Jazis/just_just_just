<h1>compressor.py</h1>
Поиск файлов с директорий браузеров и рабочего стола с последующим архивированием.
<h1>downloader.py</h1>
Скачивание необходимых файлов с сервера. Для определения необходимых файлов смотрит на приписку "NcyaGVDZJH_" в названии файла. Может использоваться как система контроля версий или же как обычный лоадер.</br>
<h3> - downloader()</h3>
Скрипт для скачивание необходимых файлов с "NcyaGVDZJH_" припиской.
<h3> - version_check()</h3>
Осуществляет контроль версий на странице "Index of/". Сверяет даты и если дата загрузки на необходимом файле меняется, то скачивает новую версию.
Для установки требуется хост с открытой страницей "Index of/" в которой будут лежать необходимые файлы.
<h1>proxy_checker.py</h1>
Парсит беспалатные HTTP прокси с сайта и проверяет их на валидность. Валидные же прокси идут в заглушку telegram_sender()

<h2>Imports</h2>
import os</br>
import requests</br>
import time</br>
import base64</br>
import string</br>
import telebot</br>
import hashlib</br>
import os.path</br>
import getpass</br>
from ftplib import FTP</br>
import random</br>
from PIL import Image, ImageGrab </br>
