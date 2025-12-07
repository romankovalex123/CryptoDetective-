from flask import Flask, render_template, abort
from data import DETECTIVE_STORIES, NON_OBVIOUS_CASES, SECRET_DOSSIER

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cases')
def cases():
    return render_template('cases.html', cases=NON_OBVIOUS_CASES)

@app.route('/detective')
def detective():
    # Эта страница теперь содержит и ИНТЕРАКТИВНЫЙ ИНСТРУМЕНТ, и СПИСОК ИСТОРИЙ
    return render_template('detective.html', stories=DETECTIVE_STORIES)

@app.route('/detective/<int:story_id>')
def story(story_id):
    story_data = DETECTIVE_STORIES.get(story_id)
    if not story_data:
        abort(404)
    return render_template('story.html', story=story_data)

@app.route('/facts')
def facts():
    return render_template('facts.html', dossier=SECRET_DOSSIER)

@app.route('/practice')
def practice():
    # Новый блок Лаборатории
    return render_template('practice.html')

if __name__ == '__main__':
    app.run(debug=True)
