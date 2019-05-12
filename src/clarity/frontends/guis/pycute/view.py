# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:50:17 2019

@author: User
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox,QVBoxLayout,QGroupBox,QHBoxLayout,QScrollArea, QWidget, QListWidget, QLineEdit, QGridLayout
from inputwithddanddelete import InputItemWithDelete
from FlowLayout import FlowLayout

class Search_Input (QLineEdit):
    
    def __init__(self, parent, onEnter):
        super().__init__(parent)
        self.onEnter = onEnter
    
    
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Down:
            self.parent().suggestions.setFocus()
        
        if e.key() == Qt.Key_Left and self.cursorPosition() == 0:
            self.parent().tags_bar.setFocus()
        
        if e.key() == Qt.Key_Return:
            self.onEnter()
        
        super().keyPressEvent(e)  
    
class Main_View (QWidget):
    
    def __init__(self, parent, api):
        
        super().__init__(parent)
        self.api = api
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        
        """ Tags Bar """
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setFixedHeight(120)
        self.scrollarea.setWidgetResizable(True)

        self.search_history_widget = QWidget()
        self.scrollarea.setWidget(self.search_history_widget)
        self.search_history_layout = QHBoxLayout(self.search_history_widget)
        #self.search_history_layout = FlowLayout(self.search_history_widget)

        
        
        #self.layout_SArea = QVBoxLayout(widget)
        #self.right_panel = Right_Panel(self)
        
        """ Search Input Text """
        def onEnter():
            item = self.suggestions.item(0)
            
            if not item or not item.text():
                return
            
            tag = api.get_tag_by_name(item.text())
            api.add_tag_to_search(tag)
            
            self.search_history_layout.addWidget(self.Item(item.text(), api))

            self.refresh_results()
        
        self.search_input = Search_Input(self, onEnter)
        self.search_input.setText('Tag..')
        self.search_input.setFixedWidth(150)  
        
        
        """ Suggestions """
        self.suggestions = QListWidget(self)
        self.suggestions.setFixedWidth(self.search_input.width())
        #self.suggestions.setSelection(0)
        self.suggestions.setStyleSheet("""
                                       border: 1px solid;
                                       border-radius: 10px;
                                       padding: 3px
                                       """)
        
        def onSuggestion(current):
            self.search_history_layout.addWidget(self.Item(current.text(), api))

            tag = api.get_tag_by_name(current.text())
            api.add_tag_to_search(tag)

            self.refresh_results()
        
        self.suggestions.itemClicked.connect(onSuggestion)
        
        """ Results """
        self.results = QListWidget(self)
        self.results.addItem('Results here')
        #self.results.setFixedWidth(600)

        def onOpenFile(current):
            text = current.text()
            file = '../files/' + text

            import webbrowser
            webbrowser.open(file)
        
        self.results.itemClicked.connect(onOpenFile)
        
        #layout.setColumnStretch(1, 2)
        #layout.setColumnStretch(2, 2)
        layout.addWidget(self.scrollarea, 0, 0)
        layout.addWidget(self.search_input, 0, 1)
        layout.addWidget(self.results, 1, 0)
        layout.addWidget(self.suggestions, 1, 1)
    
    def Item(self, text, api):
        
        def onRemove(text):
            tag = api.get_tag_by_name(text)
            api.remove_tag_from_search(tag)
            self.refresh_results()
        
        item = InputItemWithDelete(self, api, onRemove)
        item.setText(text)
        return item
    
    def refresh_results(self):
        try:
            tags = self.api.list_current_tags()
            items = self.api.list_storage_items_with_tags(tags)
            items = [item.name for item in items]

            print('Refresh!\n' + str(items))

            self.results.clear()
            self.results.addItems(items)
        
        except:
            pass