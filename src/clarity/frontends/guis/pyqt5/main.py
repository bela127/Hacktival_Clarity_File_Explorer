# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:53:11 2019

@author: User
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QLineEdit, QGridLayout, QVBoxLayout, QComboBox
from view import Main_View

"""
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()
"""


app = QApplication([])
window = QWidget()
window.setFixedHeight(500)
window.setFixedWidth(1000)

layout = QGridLayout()
layout.setColumnStretch(1, 2)
window.setLayout(layout)

""" Burger Menu """
left_menu = QListWidget(window)
left_menu.addItems(['Files', 'Favorites', 'Images', 'Music', 'Movies'])
left_menu.setFixedWidth(150)
layout.addWidget(left_menu)


""" Area to contain Main View """
area = Main_View(window)
layout.addWidget(area)

#app.setStyle('Fusion')
window.setStyleSheet("""
                     background-color: #B0BEC5
                     """)
area.setStyleSheet("""
                  margin: 2px;
                  padding: 2px;
                  border: 1px solid black;
                  border-radius: 2px;
                  background: white
                  """)


window.show()
app.exec_()