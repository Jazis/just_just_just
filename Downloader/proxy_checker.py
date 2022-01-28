def proxy_useless():
    good_proxys = []
    proxys_page = []
    req0 = requests.get('http://www.proxyserverlist24.top/search/label/Free%20Proxy%20Server%20List').text.encode('utf-8')
    for i in range(len(req0.split("'"))):
        if 'proxyserverlist24' in req0.split("'")[i] and '-free-proxy-server-list-' in req0.split("'")[i]:
            proxys_page.append(req0.split("'")[i])
    i = 0
    proxys_trash = []
    proxys = []
    next_level = requests.get(proxys_page[0]).text.encode('utf-8')
    for i in range(len(next_level.split(">"))):
        if "." in next_level.split(">")[i] and ':' in next_level.split(">")[i]:
            proxys_trash.append(next_level.split(">")[i])
    for j in range(len(proxys_trash)):
        if '.' in proxys_trash[j] and ':' in proxys_trash[j]:
            if [s for s in proxys_trash[j][0] if s in '0123456789']: 
                # print proxys_trash[j]
                proxy_trash_list = proxys_trash[j]
    for k in range(len(proxy_trash_list.split('\n'))):
        proxys.append(proxy_trash_list.split('\n'))
    del proxys[0][-1]
    i = 0   
    for i in range(len(proxys[0])):
        # print proxys[0][i]
        proxies = {"http": proxys[0][i]}
        req0 = requests.get('https://ru.infobyip.com/', proxies=proxies)
        if proxys[0][i].split(':')[0] in req0.text.encode('utf-8') and req0.status_code == 200:
            good_proxys.append(proxys[0][i])
            telegram_sender()
            print good_proxys
            pass
        req0 = requests.get('http://myip.ru/')
        if proxys[0][i].split(':')[0] in req0.text.encode('utf-8') and req0.status_code == 200:
            good_proxys.append(proxys[0][i])
            proxy = proxys[0][i]
            telegram_sender()
            print good_proxys
            pass
        else:
            pass
    # print proxys_trash