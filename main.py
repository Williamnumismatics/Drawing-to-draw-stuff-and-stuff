import keyboard

def on_tab_e():
    print("Tab+E pressed")

keyboard.add_hotkey('tab+e', on_tab_e)

while True:
    on_tab_e
