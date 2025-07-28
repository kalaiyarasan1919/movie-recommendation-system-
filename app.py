from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded test data with more movies and genres
test_movies = [
    # Drama Movies
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "poster": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNDAwMjU5NjY@._V1_.jpg"},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxOWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "poster": "https://m.media-amazon.com/images/M/MV5BNDIzNDU0YzEtYzE5Ni00ZjlkLTk5ZjgtNjM3NWE4YzA3Nzk3XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "poster": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
    {"title": "The Green Mile", "genre": "Drama", "rating": 8.6, "poster": "https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5Nl5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg"},
    {"title": "Goodfellas", "genre": "Drama", "rating": 8.7, "poster": "https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjIwYjFjNmI3ZGEwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    
    # Crime Movies
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "The Departed", "genre": "Crime", "rating": 8.5, "poster": "https://m.media-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_.jpg"},
    {"title": "Heat", "genre": "Crime", "rating": 8.2, "poster": "https://m.media-amazon.com/images/M/MV5BNGM0NzIxNmEtYzU3Zi00NzE2LTk3ZTgtNzM0MzFiYzQ1Mjc2XkEyXkFqcGdeQXVyMzU0NzkwNTg@._V1_.jpg"},
    {"title": "Scarface", "genre": "Crime", "rating": 8.3, "poster": "https://m.media-amazon.com/images/M/MV5BNjdjNGM4ZTUtN2M5YS00YzFjLTk1NDUtNTNhMzc1YjU1MjIyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "The Usual Suspects", "genre": "Crime", "rating": 8.5, "poster": "https://m.media-amazon.com/images/M/MV5BYTViNjMyNmUtNDFkNC00ZDRlLThmMDUtZDU2YWE4NGI2ZjVmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    {"title": "Reservoir Dogs", "genre": "Crime", "rating": 8.3, "poster": "https://m.media-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MTktY2VlMDVmNWFlNTQ2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    
    # Action Movies
    {"title": "Inception", "genre": "Action", "rating": 8.8, "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTcwYzFjOWM5NmJhXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"},
    {"title": "John Wick", "genre": "Action", "rating": 7.4, "poster": "https://m.media-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwNTM1MzAwNjE@._V1_.jpg"},
    {"title": "Mission: Impossible", "genre": "Action", "rating": 7.1, "poster": "https://m.media-amazon.com/images/M/MV5BMTc3NjI2MjU0Nl5BMl5BanBnXkFtZTgwNDk3ODYxMTE@._V1_.jpg"},
    {"title": "Die Hard", "genre": "Action", "rating": 8.2, "poster": "https://m.media-amazon.com/images/M/MV5BMzNmY2FkMjItNDExNy00ZTk2LTg3OTYtY2I3YzVjZjZkYjFjXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg"},
    
    # Romance Movies
    {"title": "Titanic", "genre": "Romance", "rating": 7.9, "poster": "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8, "poster": "https://m.media-amazon.com/images/M/MV5BMTk3OTM0NjA0NF5BMl5BanBnXkFtZTgxMzE1MjI5MzE@._V1_.jpg"},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0, "poster": "https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg"},
    {"title": "500 Days of Summer", "genre": "Romance", "rating": 7.7, "poster": "https://m.media-amazon.com/images/M/MV5BMTk5MjM4OTU1OV5BMl5BanBnXkFtZTcwOTkzODE2Mw@@._V1_.jpg"},
    {"title": "Eternal Sunshine of the Spotless Mind", "genre": "Romance", "rating": 8.3, "poster": "https://m.media-amazon.com/images/M/MV5BMjAxNDYxMjAwNV5BMl5BanBnXkFtZTYwNTk2ODM5._V1_.jpg"},
    {"title": "Before Sunrise", "genre": "Romance", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BZDdiZTAwYzAtMzQ0Yy00MjQ2LWI3YzQtMWRlNGMzYjA1ZTY2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    
    # Horror Movies
    {"title": "The Shining", "genre": "Horror", "rating": 8.4, "poster": "https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1YjViOTM5ZGRhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "A Nightmare on Elm Street", "genre": "Horror", "rating": 7.4, "poster": "https://m.media-amazon.com/images/M/MV5BNzFjNmM1OGYtMzZkMC00MzFiLWIzNGYtMzFiNzM0MjQ4ZWM3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
    {"title": "Halloween", "genre": "Horror", "rating": 7.7, "poster": "https://m.media-amazon.com/images/M/MV5BMzkzZmU1YTctNThhMi00MzE2LWIzYWYtOGQ1NDI2NThhMDk4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
    {"title": "The Exorcist", "genre": "Horror", "rating": 8.0, "poster": "https://m.media-amazon.com/images/M/MV5BYjhmMGMtZDgtY2ExYy00YzBjLThjODUtZGJhNWM0ZWQ4Y2FmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
    {"title": "Alien", "genre": "Horror", "rating": 8.4, "poster": "https://m.media-amazon.com/images/M/MV5BOGQzZTBjMjQtOTMwMC00MzE5LWIyZTAtMzhmZWYzZWI3ZmY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
    {"title": "The Silence of the Lambs", "genre": "Horror", "rating": 8.6, "poster": "https://m.media-amazon.com/images/M/MV5BNjNhZTk1ZmEtMzJhYi00ZWFhLTlmYyQtMWU1ZDFlMmQ1OGQwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    
    # Sci-Fi Movies
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "poster": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    {"title": "Blade Runner", "genre": "Sci-Fi", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    {"title": "2001: A Space Odyssey", "genre": "Sci-Fi", "rating": 8.3, "poster": "https://m.media-amazon.com/images/M/MV5BMmNlYzRiNDctZWNhMi00MzI4LThkZTctMTUzMmZkMmFmMWNhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "Back to the Future", "genre": "Sci-Fi", "rating": 8.5, "poster": "https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjQwLWNjNzZmZmM4NjU4N2I5NGMxXkEyXkFqcGdeQXVyMTUzMDUzNTI3._V1_.jpg"},
    {"title": "E.T. the Extra-Terrestrial", "genre": "Sci-Fi", "rating": 7.8, "poster": "https://m.media-amazon.com/images/M/MV5BMTQ2ODFlMDAtNzdhOC00ZDYzLWE3YzEtYzFiOGU2YzFiZDcyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
    
    # Comedy Movies
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BMzM5NjUxNDcwNl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_.jpg"},
    {"title": "Superbad", "genre": "Comedy", "rating": 7.6, "poster": "https://m.media-amazon.com/images/M/MV5BMjA0ODM5MDM0OF5BMl5BanBnXkFtZTcwMzA2ODg5OA@@._V1_.jpg"},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7, "poster": "https://m.media-amazon.com/images/M/MV5BNGQwZjg5YmYtY2VkNC00NzliLTljYTctNzJkODM3ZGUzNjQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "Bridesmaids", "genre": "Comedy", "rating": 6.8, "poster": "https://m.media-amazon.com/images/M/MV5BMjAyOTAyMzAxNV5BMl5BanBnXkFtZTcwMjM2MjQ5Nw@@._V1_.jpg"},
    {"title": "Shaun of the Dead", "genre": "Comedy", "rating": 7.9, "poster": "https://m.media-amazon.com/images/M/MV5BMTUxNjQxNTAzMl5BMl5BanBnXkFtZTYwNDk2Mjc3._V1_.jpg"},
    {"title": "The Big Lebowski", "genre": "Comedy", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_.jpg"},
    
    # Thriller Movies
    {"title": "Gone Girl", "genre": "Thriller", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE@._V1_.jpg"},
    {"title": "Shutter Island", "genre": "Thriller", "rating": 8.2, "poster": "https://m.media-amazon.com/images/M/MV5BYzhiNDkyNzktNTZmYS00ZTBkLTk2MDAtM2U0YjU1MzgxZjgzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    {"title": "Memento", "genre": "Thriller", "rating": 8.4, "poster": "https://m.media-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktYjFjM2FhOGYwYzI1XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
    {"title": "Se7en", "genre": "Thriller", "rating": 8.6, "poster": "https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjFkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"},
    {"title": "Zodiac", "genre": "Thriller", "rating": 7.7, "poster": "https://m.media-amazon.com/images/M/MV5BMTQyNzk0NTc0NF5BMl5BanBnXkFtZTcwMDU4NjU4OQ@@._V1_.jpg"},
    {"title": "The Sixth Sense", "genre": "Thriller", "rating": 8.1, "poster": "https://m.media-amazon.com/images/M/MV5BMWM4NTFhYjctNWU5Ni00YzQzLWI5NjItOTBlYzYyYTkyMDQ2XkEyXkFqcGdeQXVyODUxOTU0Nzg@._V1_.jpg"}
]

def filter_by_genre(genre):
    filtered = [movie for movie in test_movies if genre.lower() in movie["genre"].lower()]
    print(f"Filtering for genre '{genre}': found {len(filtered)} movies")
    print(f"Available genres: {list(set([movie['genre'] for movie in test_movies]))}")
    return filtered

def recommend_by_genre(genre):
    filtered_movies = filter_by_genre(genre)
    if not filtered_movies:
        return []  # Return empty list instead of string
    
    # Return top 6 by rating (increased from 5 to 6)
    sorted_movies = sorted(filtered_movies, key=lambda x: x["rating"], reverse=True)[:6]
    
    recommendations = []
    for movie in sorted_movies:
        recommendations.append({
            'title': str(movie['title']),  # Ensure it's a string
            'poster': str(movie['poster'])  # Ensure it's a string
        })
    
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        genre = request.form['genre']
        print(f"Received genre: '{genre}'")
        recommendations = recommend_by_genre(genre)
        print(f"Final recommendations: {recommendations}")
        print(f"Type of recommendations: {type(recommendations)}")
    return render_template('index.html', recommendations=recommendations)

# Test route to verify data
@app.route('/test')
def test():
    test_recs = recommend_by_genre('Drama')
    return {'recommendations': test_recs}

# Debug route to show all movies
@app.route('/debug')
def debug():
    return {
        'all_movies': test_movies,
        'available_genres': list(set([movie['genre'] for movie in test_movies])),
        'drama_movies': recommend_by_genre('Drama'),
        'crime_movies': recommend_by_genre('Crime'),
        'action_movies': recommend_by_genre('Action'),
        'romance_movies': recommend_by_genre('Romance'),
        'horror_movies': recommend_by_genre('Horror'),
        'scifi_movies': recommend_by_genre('Sci-Fi'),
        'comedy_movies': recommend_by_genre('Comedy'),
        'thriller_movies': recommend_by_genre('Thriller')
    }

# For deployment
app.debug = True

if __name__ == '__main__':
    app.run(debug=True) 