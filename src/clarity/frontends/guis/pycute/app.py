from clarity.api.api import API
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:53:11 2019

@author: User
"""

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QListWidget, QGridLayout
from view import Main_View


api = API()


class App_View (QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super().__init__()

        self.setFixedHeight(500)
        self.setFixedWidth(1000)
        
        layout = QtWidgets.QGridLayout()
        layout.setColumnStretch(1, 2)
        self.setLayout(layout)
        
        """ Burger Menu """
        left_menu = QtWidgets.QListWidget(self)
        left_menu.addItems(['Files', 'Favorites', 'Images', 'Music', 'Movies'])
        left_menu.setFixedWidth(150)
        layout.addWidget(left_menu)
        
        
        """ Area to contain Main View """
        area = Main_View(self)
        layout.addWidget(area)
        
        #app.setStyle('Fusion')
        self.setStyleSheet("""
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
    
    app = QtWidgets.QApplication([])
    window = App_View()
    
    window.show()
    app.exec_()