from flask import Flask, jsonify, request

app = Flask(__name__)

# Модели
class Movie:
    def __init__(self, id, title, release_year):
        self.id = id
        self.title = title
        self.release_year = release_year

class Actor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Пример данных
movies = [
    Movie(1, "The Matrix", 1999),
    Movie(2, "Inception", 2010)
]

actors = [
    Actor(1, "Keanu Reeves"),
    Actor(2, "Leonardo DiCaprio")
]

# Контроллеры
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify([{"id": movie.id, "title": movie.title, "release_year": movie.release_year} for movie in movies])

@app.route('/actors', methods=['GET'])
def get_actors():
    return jsonify([{"id": actor.id, "name": actor.name} for actor in actors])

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)
