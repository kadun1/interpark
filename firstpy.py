from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
from PIL import ImageGrab
import time

chrome_driver = 'C://02WorkSpaces/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)
driver.set_window_size(1400, 1200)
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')
driver.implicitly_wait(3)

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('fourbass8739') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('tlrnr1003@') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)



#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21002720')
driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21004910')
#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21005562')

MB = True
while MB:
    resbutton = driver.find_element_by_xpath('//*[@id="productSide"]/div/div[2]/a[1]')
    if(resbutton.text=='예매하기'):
        print('예매')
        resbutton.click()
        MB = False
        break
    else:
        print('새로고침')
        driver.refresh()


time.sleep(1)
# 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

pag.click(397, 475)

def color(RGB):  # RGB 값을 색깔 문자열로 반환하는 함수
    c_p = (124, 104, 238)
    c_g = (28, 168, 20)
    c_c = (23, 179, 255)
    c_o = (251, 126, 79)
    c_r = (255, 68, 15)
    if RGB == c_p: return "purple"
    elif RGB == c_g: return "green"
    elif RGB == c_c: return "cyan"
    elif RGB == c_o: return "orange"
    elif RGB == c_r: return "red"
    else: return "other"
SB=0
while SB==0:
    screen = ImageGrab.grab() # 화면 캡쳐
    for j in range(220, 733):
        for i in range(59, 602):
            A = color(screen.getpixel((i,j))) # 왼쪽 자리
            B = color(screen.getpixel((i+15,j))) # 오른쪽 자리
            if (A != "other") and (A == B): # 5색깔 중 하나 + 두 자리
                pag.click((i,j))
                pag.click((i+30,j+10))
                pag.click(871, 669)
                SB=1
                break
            if SB==1:
                break
        if SB==1:
            break