import sqlite3

class Test_init:
    # Öffnen von Datenbank
    db = sqlite3.connect("test_db.db")
    cursor = db.cursor()
    # Kommando
    sql_command = """
    CREATE TABLE employee ( 
    id INTEGER PRIMARY KEY, 
    fname VARCHAR(20), 
    lname VARCHAR(30));"""
    # Ausführen        
    cursor.execute(sql_command)
    # Speichern
    db.commit()
    # Schließen
    db.close()