from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
# Enter installed Path of goolge chrome here
options.add_argument("--user-data-dir=C:\Program Files\Google\Chrome Dev\Application")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
#declare colors
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# File having text message template goes here
f = open("mytext.txt", "r", encoding="utf8")
message = f.read()
f.close()

print(style.WHITE + '\n message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
# File having Gentrated Numbers  goes here
f = open("phone.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.MAGENTA + 'list of numbers extracted ' + str(total_number)  + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.WHITE + "Log in to whatsapp web when Browser and press ENTER... if already logged in, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("check internet connection(both your phone and computer must be connected to internet) .")
					print("please cancel alert box." + style.RESET)
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Whatsapp Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message whatsapp number : ' + number + str(e) + style.RESET)
driver.close()
