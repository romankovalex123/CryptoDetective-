# app.py
from flask import Flask, render_template, abort
from data import DETECTIVE_STORIES, NON_OBVIOUS_CASES, SECRET_DOSSIER

app = Flask(__name__)

@app.route('/')
def index():
    """Главная страница: Теория и введение"""
    return render_template('index.html')

@app.route('/cases')
def cases():
    """Страница: Неочевидные применения"""
    return render_template('cases.html', cases=NON_OBVIOUS_CASES)

@app.route('/detective')
def detective():
    """Страница: Список расследований"""
    return render_template('detective.html', stories=DETECTIVE_STORIES)

@app.route('/detective/<int:story_id>')
def story(story_id):
    """Страница: Конкретное дело"""
    story_data = DETECTIVE_STORIES.get(story_id)
    if not story_data:
        abort(404)
    return render_template('story.html', story=story_data)

@app.route('/facts')
def facts():
    """Страница: Секретный Архив"""
    return render_template('facts.html', dossier=SECRET_DOSSIER)

if __name__ == '__main__':
    app.run(debug=True)