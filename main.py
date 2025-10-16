import keyboard
import tkinter as Tk

root = tk.TK()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'white')
root.config(bg='white')

def on_tab_e():
    print("Tab+E pressed")
    

keyboard.add_hotkey('tab+e', on_tab_e)

while True:
    on_tab_e
