import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        clear_screen()
        print(f"倒计时: {seconds // 60:02d}:{seconds % 60:02d}")
        time.sleep(1)
        seconds -= 1

    clear_screen()
    print("时间到！")

def focus_timer():
    clear_screen()
    print("欢迎使用专注时钟！")
    while True:
        try:
            minutes = int(input("请输入专注时长（分钟）: "))
            break
        except ValueError:
            print("请输入一个有效的数字！")

    countdown(minutes)

focus_timer()
