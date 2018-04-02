from selenium.webdriver.chrome.options import Options
from splinter import Browser
from selenium import webdriver
import os
import glob
import sys
import csv
import time
import random
##options = Options()
##options.add_argument('"excludeSwitches", ["ignore-certificate-errors"]')

##fp.set_preference("browser.download.dir","C:\Users\Oscar\Desktop\stock")


##with Browser('firefox', profile="C:\\Users\Oscar\AppData\Local\Mozilla\Firefox\Profiles") as browser:

##os.rmdir("C:\\Users\Oscar\Desktop\stockdata")
prof = {}
prof['browser.download.manager.showWhenStarting'] = 'false'
prof['browser.helperApps.alwaysAsk.force'] = 'false'
prof['browser.download.dir'] = "/home/ohan/Desktop/stockdata"
prof['browser.download.folderList'] = 2
prof['browser.helperApps.neverAsk.saveToDisk'] = 'text/csv, application/csv, text/html,application/xhtml+xml,application/xml, application/octet-stream, application/pdf, application/x-msexcel,application/excel,application/x-excel,application/excel,application/x-excel,application/excel, application/vnd.ms- excel,application/x-excel,application/x-msexcel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,application/excel,text/x-c'
prof['browser.download.manager.useWindow'] = 'false'
prof['browser.helperApps.useWindow'] = 'false'
prof['browser.helperApps.showAlertonComplete'] = 'false'
prof['browser.helperApps.alertOnEXEOpen'] = 'false'
prof['browser.download.manager.focusWhenStarting']= 'false'
path = '/home/ohan/Desktop/9900stock/codes.txt'
with open(path, 'w') as f:
    f.close()

skip_dict = {}

## delete previous csv        
##for infile in glob.glob(os.path.join(path, '*.csv') ):  
##    os.remove(infile)

with Browser('firefox',profile_preferences=prof) as browser:
    i = 1
    while(i<=373):
        # Visit URL

        url = 'https://xueqiu.com/hq#exchange=US&firstName=3&secondName=3_0&order=asc&orderby=symbol&page='
        browser.visit(url+str(i))
        time.sleep(random.randint(4, 5))

        if browser.is_element_present_by_css('.portfolio>tbody', wait_time=3000):
            print(i, 'got')
            l = browser.find_by_css('.portfolio>tbody')
        #     print(l.first.text)

            ll = (l.first.text).split()
            if(len(ll)==0):
                try:
                    skip_dict[str(i)]+=1
                except:
                    skip_dict[str(i)]=1
                if(skip_dict[str(i)]>3):
                    i += 1
                    print(i, 'pass!')
                continue

            j = 0
            code = [ll[0]]
            while j<len(ll):
                if(ll[j] == '关注'):
                    try:
                        code.append(ll[j+1])
                    except IndexError:

                        pass
                j+=1
            # print(len(l), '+++')
        i+=1
        with open(path, "a") as f:
            for elements in code:
                f.writelines(str(elements) + '\n')
            f.close()



