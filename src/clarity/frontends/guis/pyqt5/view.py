# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:50:17 2019

@author: User
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidget, QLineEdit, QGridLayout
#from right_panel import Right_Panel
from inputwithddanddelete import InputWithDropDownAndDelete

class Search_Input (QLineEdit):
    
    def __init__(self, parent):
        super().__init__(parent)
    
    
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Down:
            self.parent().suggestions.setFocus()
        
        if e.key() == Qt.Key_Left and self.cursorPosition() == 0:
            self.parent().tags_bar.setFocus()
        
        super().keyPressEvent(e)
    
    
class Main_View (QWidget):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        
        """ Tags Bar """
        self.tags_bar = InputWithDropDownAndDelete(self)
        #self.right_panel = Right_Panel(self)
        
        """ Search Input Text """
        self.search_input = Search_Input(self)
        self.search_input.setText('Tag..')
        self.search_input.setFixedWidth(150)
        
        def onSearchInput(self): # TODO
            if self.search_input == 'Tag..':
                self.search_input.setText('')
        
        
        """ Suggestions """
        self.suggestions = QListWidget(self)
        self.suggestions.addItems(['#Images',
                                   '#Holiday',
                                   '#Summer',
                                   '#Surfing',
                                   '#short',
                                   '#looooooooong'])
        self.suggestions.setFixedWidth(self.search_input.width())
        #self.suggestions.setSelection(0)
        self.suggestions.setStyleSheet("""
                                       border: 1px solid;
                                       border-radius: 10px;
                                       padding: 3px
                                       """)
        
        def onSuggestion(current):
            self.tags_bar.addItem(current.text())
        
        self.suggestions.itemClicked.connect(onSuggestion)
        
        """ Results """
        self.results = QListWidget(self)
        self.results.addItem('Results here')
        self.results.setFixedWidth(600)
        
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 2)
        layout.addWidget(self.tags_bar, 0, 0)
        layout.addWidget(self.search_input, 0, 1)
        layout.addWidget(self.results, 1, 0)
        layout.addWidget(self.suggestions, 1, 1)