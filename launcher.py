import json

from PyQt5.QtWidgets import *

from main import startgame

app = QApplication([])

settings = {}

window = QWidget()

def read_data():
    global settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        settings = json.dump(settings, file)
read_data()

print(settings)

b1 = QPushButton("Меню.")
bchange = QPushButton("Змінити.")
Ledit = QLineEdit(settings["skin"])

Lvmain = QVBoxLayout()

Lvmain.addWidget(Ledit)
Lvmain.addWidget(bchange)
Lvmain.addWidget(b1)

window.setLayout(Lvmain)

def change_data():
    settings["skin"] = Ledit.text()
    write_data()

bchange.clicked.connect(change_data)

b1.clicked.connect(startgame)
window.show()
app.exec()
