# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:50:40 2019

@author: User
"""
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QLineEdit, QGridLayout, QVBoxLayout, QComboBox


class Right_Panel (QWidget):
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.search_input = QLineEdit(self)
        self.search_input.setText('#Tag')
        
        self.suggestions = QListWidget(self)
        self.suggestions.addItems(['#Images', '#Holiday', '#Summer', '#Surfing'])
        
        layout.addWidget(self.search_input, 0, 0)
        layout.addWidget(self.suggestions, 1, 0)