import pyautogui
import time

#time to tab out of wherever ur running this from:
time.sleep(3)

#a tiny program to send messages in discord. replace x and y with the coordinates of where the message box is.
#replace "example message" with whatever message u want to spam
x=768
y=1032
pyautogui.click(x, y)
ur_message = "example message"
while True:
    #this waits 2 seconds in between each message, u can adjust this aswell if u want
    time.sleep(2)
    pyautogui.write(ur_message)
    pyautogui.keyDown('Enter')