# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:09:07 2025

@author: L1F22PACS0008
"""
from  flask import Flask, request
import sqlite3

app =Flask(__name__)

def init_db():
    conn = sqlite3.connect('simple.db')
    c = conn.cursor()
    c.execute('''
              CRETAE TABLE IF NOT EXISTS people (
                  id INTERGER PRIMARY KEY AUTOINCREAMENT ,
                  name TEXT NOT NULL
                  
                  )
              ''')
    conn.commit()
    conn.close()           

@app.route('/',method=['GET' , 'POST' ])

def home():
    if request.method== 'POST':
        name = request.form.get('name')
        if name:
            conn=sqlite3.connect('simple.db')
            c=conn.cursor()
            
            c.execute('INSERT INTO people (name) VALUES(?)' , (name))
            conn.commit()
            conn.close()
            
    conn.sqlite3.connect('simple.db')
    c = conn.cursor() 
    c.execute('SELECT * FROM people')
    rows = c.fetchall()
    conn.close() 
 
    page= "<h1>People List</h1><ul>"
    for row in rows:
      page += "</ul><h2>Add Person</h2><form method='POST'>"
      return page
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
        