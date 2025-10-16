import keyboard
import time

def on_tab_e():
    print("Tab+E pressed")

# register chord (works in either order)
keyboard.add_hotkey('tab+e', on_tab_e)

print("Listening")
