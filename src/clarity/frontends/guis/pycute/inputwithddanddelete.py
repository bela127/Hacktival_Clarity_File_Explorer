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
        self.text = ''
        
        self.setStyleSheet("""
                           border: 1px solid grey;
                           border-radius: 10px;
                           font-weight: bold;
                           """)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
        self.setGraphicsEffect(shadow)
        
        self.dropdown = QComboBox(self)
        self.dropdown.setStyleSheet("""
                                    border: none;
                                    border-radius: 2px;
                                    margin: 1px;
                                    padding: 1px;
                                    """)
        self.dropdown.adjustSize()
        
        self.cross = QPushButton('x', self)
        self.cross.setFixedWidth(20)


        def onSelect():
            text = self.dropdown.currentText()
            tag = api.get_tag_by_name(text)
            tags = api.list_all_tags()[:5] # TODO
            items = [tag.name for tag in tags]
            self.dropdown.clear()
            self.dropdown.addItem(text)
            self.dropdown.addItems(items)
        
        self.dropdown.highlighted.connect(onSelect)
        #self.dropdown.addItems(['xD', '^^', ':P'])

        def onChange():
            text = self.dropdown.currentText()
            new_tag = api.get_tag_by_name(text)
            to_replace = api.get_tag_by_name(self.text)
            if new_tag and to_replace:
                api.replace_search_tag(to_replace, new_tag)
                print('' + self.text + ' -> ' + text)
                self.text = text
        
        self.dropdown.activated.connect(onChange)


        """ Remove """
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
    
    
    def setText(self, value):
        self.dropdown.clear()
        self.dropdown.addItem(value)
        self.dropdown.setCurrentText(value)
        self.text = value
    