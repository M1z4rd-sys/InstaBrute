import os
import time
print("Kuruluma Hoşgeldiniz\nGerekli Mödüller İnerken Lütfen Kapatmayınız")
time.sleep(2)
pipversion_control = "python -m pip install --upgrade pip"
command_1 = "pip install selenium"
command_2 = "pip install pynput"
command_3 = "pip install termcolor"
command_4 = "pip install webdriver_manager"
os.system(pipversion_control)

os.system(command_1)

os.system(command_2)

os.system(command_3)

os.system(command_4)
time.sleep(2)
print("Kurulum Tamamlandı InstaBrute.py Çalıştırabilirsiniz.")

