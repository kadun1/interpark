import time

import keyboard
import pyautogui as pag
from PIL import ImageGrab


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

def find():
    global SB
    SB = 0
    screen = ImageGrab.grab() # 화면 캡쳐
    for j in range(195, 299):
        for i in range(61, 680):
            A = color(screen.getpixel((i,j))) # 왼쪽 자리
            B = color(screen.getpixel((i+15,j))) # 오른쪽 자리
            if (A != "other") and (A == B): # 5색깔 중 하나 + 두 자리
                pag.click((i,j))
                pag.click((i+30,j+10))
                pag.click(835, 625)
                SB = 1
                break
            if SB == 1:
                break
        if SB == 1:
            break
SB = 0
while SB == 0 or SB is None :
    pag.click(180, 468) #A구역 클릭
    time.sleep(0.3)
    find()
    print("A구역반환", SB)
    if SB==1: break
    time.sleep(0.3)
    pag.click(791, 155) #좌석도 전체보기
    time.sleep(0.3)
    pag.click(865, 666) #다시선택 클릭
    time.sleep(0.5)
    pag.click(508, 463) #G구역 클릭
    time.sleep(0.3)
    find()
    print("G구역반환", SB)
    if SB==1: break
    time.sleep(0.3)
    pag.click(791, 155) #좌석도 전체보기
    time.sleep(0.3)
    pag.click(865, 666) #다시선택 클릭
    time.sleep(0.5)
    if keyboard.is_pressed('F3'): break
print('루프 탈출')



