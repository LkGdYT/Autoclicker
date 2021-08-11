import mouse
import keyboard
from time import sleep

def autoclick():
    keyboard.press_and_release('p')
    keyboard.press_and_release('p')
    keyboard.press_and_release('p')
    keyboard.press_and_release('p')


print('Autoclicker made by Lk_Gd#0848')
print('READ HOW TO USE FILE')
print('Join here for support: https://discord.gg/6C9gSVJjrp')

sleep(1)

mouse.on_click(autoclick)
keyboard.wait('backspace')