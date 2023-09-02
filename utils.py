from pathlib import Path
import json
from database import Database, Note

db = Database('data/database_projeto')
CUR_DIR = Path(__file__).parent

def extract_route(string):
    return string.split()[1][1:] if len(string.split()) > 1 else ""

def read_file(path):
    with open(path,'rb') as file:
        content = file.read()
        return content
    
def load_data():
    notes = db.get_all()
    return notes

def load_data_id(id):
    note = db.get(id)
    return note.title, note.content
    
def load_template(name):
    path = CUR_DIR / "Templates"
    file = open(path / name, 'r',  encoding='utf-8')
    data = file.read()
    return data

def build_response(body='',code=200,reason='OK',headers=''):
    if headers == '':
        headers = 'Content-Type: text/html; charset=utf-8'
    response = f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}".encode()
    return response

def add_data(item):
    db.add(Note(
        title = item[0],
        content = item[1]
    ))

def update_data(item):
    db.update(Note(
        id = item[0],
        title = item[1],
        content = item[2]
    ))

def delete_data(id):
    db.delete(id)
