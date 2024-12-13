import pyautogui as pt
import time

limit = input("Enter limit: ")
massage = input("Enter massage: ")

time.sleep(3)

i = 0

while i < int(limit):
    pt.typewrite(massage)
    pt.press("enter")

    i += 1