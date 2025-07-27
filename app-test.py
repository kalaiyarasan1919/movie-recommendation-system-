from flask import Flask, render_template, request

app = Flask(__name__)

# Simple test data instead of CSV
test_movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "poster": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNDAwMjU5NjY@._V1_.jpg"},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2, "poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxOWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "poster": "https://m.media-amazon.com/images/M/MV5BNDIzNDU0YzEtYzE5Ni00ZjlkLTk5ZjgtNjM3NWE4YzA3Nzk3XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg"},
    {"title": "Inception", "genre": "Action", "rating": 8.8, "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg"},
]

def filter_by_genre(genre):
    return [movie for movie in test_movies if genre.lower() in movie["genre"].lower()]

def recommend_by_genre(genre):
    filtered_movies = filter_by_genre(genre)
    if not filtered_movies:
        return f"No movies found for the genre: {genre}"
    
    # Return top 5 by rating
    sorted_movies = sorted(filtered_movies, key=lambda x: x["rating"], reverse=True)[:5]
    
    recommendations = []
    for movie in sorted_movies:
        recommendations.append({
            'title': movie['title'],
            'poster': movie['poster']
        })
    
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        genre = request.form['genre']
        recommendations = recommend_by_genre(genre)
    return render_template('index.html', recommendations=recommendations)

# For deployment
app.debug = True

if __name__ == '__main__':
    app.run(debug=True) 