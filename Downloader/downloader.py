import os
import requests

class temp():
    proxy = ''
    unique_value = "NcyaGVDZJH_"
    file_date = ''
    
def version_check():
    files = []
    url = 'https://memberlikefull.000webhostapp.com/files_/'
    req0 = requests.get(url).text.encode('utf-8')
    for i in range(len(req0.split('"'))):
        files.append(req0.split('"')[i])
    for j in range(len(files)):
        if 'NcyaGVDZJH_' in files[j] and '>' not in files[j]:
            unique_value = files[j+3].replace('  </td><td align=', '').replace('>','').replace(' ', '').replace('-', '').replace(':', '')
    file_path = os.path.abspath(__file__)
    print os.listdir(file_path.replace(file_path.split('/')[-1], ''))
    index = []
    file_path = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1], '')
    for i in range(len(file_path)):
        try:
            if temp.unique_value in os.listdir(file_path)[i]:
                print "good " + os.listdir(file_path)[i]
                old_file_date = os.listdir(file_path)[i].split('_')[0]
                file_name = os.listdir(file_path)[i].split('_')[1]
                if '.' in file_name:
                    downloader()
                if old_file_date != file_date:
                    downloader()
                print old_file_date, file_name   
        except IndexError:
            pass
    if temp.unique_value not in os.listdir(file_path):
        downloader()

def downloader():
    files = []
    url = 'https://memberlikefull.000webhostapp.com/files_/'
    req0 = requests.get(url).text.encode('utf-8')
    for i in range(len(req0.split('"'))):
        files.append(req0.split('"')[i])
    for j in range(len(files)):
        if 'NcyaGVDZJH_' in files[j] and '>' not in files[j]:
            loaded_file = open(files[j+3].replace('  </td><td align=', '').replace('>','').replace(' ', '').replace('-', '').replace(':', '') + '_' + files[j].replace(temp.unique_value, ''), 'wb')
            req1 = requests.get(url + files[j])
            loaded_file.write(req1.content)
            loaded_file.close
            print "downloaded"
    print "Error code 404"
    time.sleep(1)
    exit()

if __name__ == "__main__":
    version_check()