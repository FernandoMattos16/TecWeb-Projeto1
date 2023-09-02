from database import Database,Note

db = Database('data/database_projeto')
db.add(Note(title='Vavazin', content='Melhor game'))
db.add(Note(title="Teste", content='Testando'))

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')