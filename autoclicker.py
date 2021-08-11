import mouse
import keyboard
from time import sleep

def autoclick():
    mouse.click(button= 'left')
    mouse.click(button= 'left')
    mouse.click(button= 'left')
    mouse.click(button= 'left')


print('Autoclicker made by Lk_Gd#0848')
print('HOW TO USE: click middle button one time: 4 clicks. To close application press the backspace key')
print('Join here for support: https://discord.gg/6C9gSVJjrp')

sleep(1)

mouse.on_middle_click(autoclick)
keyboard.wait('backspace')