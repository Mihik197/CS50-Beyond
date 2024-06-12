import sqlite3
import csv

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open("books.csv", "r") as file:
    csv_reader = csv.reader(file)
    authors = []
    for row in csv_reader:
        isbn = row[0]
        title = row[1]
        author = row[2]
        year = row[3]

        cursor.execute('SELECT id FROM authors WHERE name = ?', (author,))
        author_id = cursor.fetchone()

        if author_id is None:
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (author,))
            author_id = cursor.lastrowid
        else:
            author_id = author_id[0]
        
        cursor.execute('INSERT INTO books (isbn, title, year, author_id) VALUES (?, ?, ?, ?)', (isbn, title, year, author_id))            

conn.commit()
conn.close()


'''
temp storage:
CREATE TABLE authors (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    isbn TEXT NOT NULL,
    year INTEGER NOT NULL,
    author_id INTEGER REFERENCES authors(id)
);
'''