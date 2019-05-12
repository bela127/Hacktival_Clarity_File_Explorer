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


class App_View (QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        #self.setFixedHeight(500)
        #self.setFixedWidth(1000)
        
        layout = QtWidgets.QGridLayout()
        #layout.setColumnStretch(1, 2)
        self.setLayout(layout)
        
        """ Burger Menu """
        left_menu = QtWidgets.QListWidget(self)
        left_menu.addItems(['Files', 'Favorites', 'Images', 'Music', 'Movies'])
        left_menu.setFixedWidth(200)
        layout.addWidget(left_menu, 0, 0)
        
        
        """ Area to contain Main View """
        area = Main_View(self, api)
        layout.addWidget(area, 0,1)
        
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
        
        suggestions = [tag.name for tag in api.list_all_tags() if tag]
        area.suggestions.addItems(suggestions)

        def onSearchInput(text):
            area.suggestions.clear()
            suggestions = [tag.name for tag in api.list_tags_with_text(text)]
            area.suggestions.addItems(suggestions)
        
        area.search_input.textEdited.connect(onSearchInput)


if __name__ == '__main__':
    
    app = QtWidgets.QApplication([])
    window = App_View()
    
    window.show()
    app.exec_()