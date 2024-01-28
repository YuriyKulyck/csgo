import json

from PyQt5.QtGui import QPixmap
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

b1 = QPushButton("Запуск.")
bchange = QPushButton("Змінити.")
skin007 = QLabel("Картинка")
skinimg = QPixmap("ufo.png")
skinimg = skinimg.scaledToWidth(128)
skin007.setPixmap(skinimg)
buyskin = QPushButton("Купити цей образ.")
Ledit = QLineEdit(settings["skin"])

Lvmain = QVBoxLayout()

Lvmain.addWidget(Ledit)
Lvmain.addWidget(bchange)
Lvmain.addWidget(b1)
Lvmain.addWidget(skin007)
Lvmain.addWidget(buyskin)

window.setLayout(Lvmain)

def buyskinimg():
    if settings["money"] >= 10:
        settings["money"] -= 10
        settings["skin"] = "ufo.png"
        write_data()
    else:
        print("Покупка не буде виконана, якщо баланс нищий, аніж ціна.")


def change_data():
    settings["skin"] = Ledit.text()
    write_data()

bchange.clicked.connect(change_data)
buyskin.clicked.connect(buyskinimg)

b1.clicked.connect(startgame)
window.show()
app.exec()
