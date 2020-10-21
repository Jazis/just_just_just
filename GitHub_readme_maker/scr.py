from selenium import webdriver
import time

class chva_chva():
    def name_take():
        counter = 0
        print("Lets go")
        open("ReadMe.md", 'a+').write("""
        # My repo 0_o\n
        All my trash and some more<br><br>\n
            """)
        for i in range(len(driver.page_source.split('"'))):
            # print("check")
            if "rowheader" in driver.page_source.split('"')[i]:
                counter += 1
                name = driver.page_source.split('"')[i+8]
                url = "https://github.com" + driver.page_source.split('"')[i+10]
                open("ReadMe.md", 'a+').write("""- {} - [{}]({})\n""".format(str(counter), str(name), str(url)))
                print("- {} - [{}]({}) ".format(str(counter), str(name), str(url)))

    def page_check():
        while True:
            if "Go to file" in driver.page_source:
                print ("[+] Ok")
                break
            else:
                time.sleep(0.2)
    def git_find():
        driver.get("https://github.com/")

if __name__ == "__main__":
    open("ReadMe.md", 'w')
    path = "chromedriver.exe"
    driver = webdriver.Chrome()
    chva_chva.git_find()
    chva_chva.page_check()
    chva_chva.name_take()
    print("Done")
