from clarity.api.api import API
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:53:11 2019

@author: User
"""

from PyQt5.QtGui import QGuiApplication, QWindow
from PyQt5.QtWidgets import QApplication, QWindow, QWidget, QListWidget, QGridLayout
from view import Main_View


api = API()


class App_View (QWindow):
    
    def __init__(self, parent):
        
        super().__init__()

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


if __name__ == '__main__':
    
    app = QApplication([])
    window = App_View(app)
    
    window.show()
    app.exec_()