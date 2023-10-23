#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ama
#
# Created:     21/10/2023
# Copyright:   (c) ama 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys; sys.path.append(r"C:\pymodules")
from question import *
from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename

from tkmenu import Menu
import yaml
import data

settings = data.YAMLDataFile("settings.yaml")

root = Window()


style = Style()
style.load_user_themes("themes.json")
style.theme_use(settings["theme"])
root.option_add("*tearOff", FALSE)
root.state("zoomed")
root.title("mcq")
QUESTIONS_NB = Notebook(root)
QUESTIONS_NB.grid(row=1, column=1, sticky="nsew")
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
data.root, data.style = root, style
#https://cameroongcerevision.com/cameroon-gce-a-level-june-2023-chemistry-1/

def M_open(*_):
    if not (file_url := askopenfilename()): return

    with open(file_url, encoding="utf-8") as file:

        data = yaml.safe_load_all(file.read())
        for x in data:
            q_frm = Paper(QUESTIONS_NB, x)




menu, _ = Menu(root, {
    "m-File": {
        "c-&Open": {
            "command": M_open,
            "accelerator": "Ctrl+o",
            "bind": "<Control-o>"
        }
    }
})
root["menu"] = menu

root.mainloop()