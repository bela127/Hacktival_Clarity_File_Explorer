# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:55:05 2019

@author: User
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QComboBox, QFrame, QGraphicsDropShadowEffect, QScrollArea
from FlowLayout import FlowLayout

class InputItemWithDelete (QFrame):
    
    def __init__(self, parent, api, onRemove):
        
        super().__init__(parent)
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.setStyleSheet("""
                           border: 1px solid grey;
                           border-radius: 10px;
                           font-weight: bold;
                           """)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.setGraphicsEffect(shadow)
        
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(['suggest1', 'suggest2'])
        self.dropdown.setStyleSheet("""
                                    border: none;
                                    border-radius: 2px;
                                    margin: 1px;
                                    padding: 1px;
                                    """)
        self.dropdown.adjustSize()
        
        self.cross = QPushButton('x', self)
        self.cross.setFixedWidth(20)

        def onCross():
            text = self.dropdown.currentText()
            onRemove(text)
            self.setParent(None)

        self.cross.clicked.connect(onCross)
        self.cross.setStyleSheet("""
                                 border: none;
                                 border-radius: 5px;
                                 color: black;
                                 background: #8888ff;
                                 margin: 0px;
                                 padding: 2px
                                 """)
        
        layout.addWidget(self.dropdown)
        layout.addWidget(self.cross)
        self.adjustSize()
    
    
    def setText(self, value):
        self.dropdown.setItemText(self.dropdown.currentIndex(), value)
    


class SearchHistory (QFrame):
    
    def __init__(self, parent, api):
        
        super().__init__(parent)
        self.api = api
        
        self.layout = FlowLayout()
        self.setLayout(self.layout)
        self.setFixedHeight(100)
        
        self._items = []
    
    
    def addItem(self, value, api):
        item = InputItemWithDelete(self, api)
        item.setText(value)
        self.layout.addWidget(item)
        self._items.append(item)
    
    
    def remove(self, item):
        
        text = item.text()
        tag = self.api.tag_by_name(text)
        self.api.remove_tag_from_search(tag)
        self.parent().refresh_results()
        
        self.layout.removeWidget(item)
        item.setParent(None)
    
    
    def setFocus(self):
        print('Receive Focus')
    
    
    def keyPressEvent(self, e):
        
        print('Key hit')
        
        if e.key() == Qt.Key_Left:
            print('left')
        if e.key() == Qt.Key_Right:
            print('right')
        
        super().keyPressEvent(e)