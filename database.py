import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    
    def __init__(self,name) -> None:
        self.name = name
        self.conn = sqlite3.connect(name +".db")
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)"
        )
        self.conn.commit()

    def add(self, note):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO note VALUES (?, ?, ?)", (note.id,note.title,note.content))
        self.conn.commit()

    def get(self, note_id):
        cur = self.conn.cursor()
        cursor = cur.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
        note = [(Note(linha[0], linha[1], linha[2])) for linha in cursor]
        return note[0]

    def get_all(self):
        notes = []
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM note")
        rows = cursor.fetchall()
        for row in rows:
            notes.append(Note(*row))
        return notes
    
    def update(self,entry):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE note SET title = ?, content = ? WHERE id = ?" , (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self,note_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))
        self.conn.commit()




