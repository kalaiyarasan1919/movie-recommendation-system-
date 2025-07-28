from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded test data with more movies and genres - Updated with reliable poster URLs
test_movies = [
    # Drama Movies
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "poster": "https://picsum.photos/300/450?random=1"},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "poster": "https://picsum.photos/300/450?random=2"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "poster": "https://picsum.photos/300/450?random=3"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "poster": "https://picsum.photos/300/450?random=4"},
    {"title": "The Green Mile", "genre": "Drama", "rating": 8.6, "poster": "https://picsum.photos/300/450?random=5"},
    {"title": "Goodfellas", "genre": "Drama", "rating": 8.7, "poster": "https://picsum.photos/300/450?random=6"},
    
    # Crime Movies
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "poster": "https://picsum.photos/300/450?random=7"},
    {"title": "The Departed", "genre": "Crime", "rating": 8.5, "poster": "https://picsum.photos/300/450?random=8"},
    {"title": "Heat", "genre": "Crime", "rating": 8.2, "poster": "https://picsum.photos/300/450?random=9"},
    {"title": "Scarface", "genre": "Crime", "rating": 8.3, "poster": "https://picsum.photos/300/450?random=10"},
    {"title": "The Usual Suspects", "genre": "Crime", "rating": 8.5, "poster": "https://picsum.photos/300/450?random=11"},
    {"title": "Reservoir Dogs", "genre": "Crime", "rating": 8.3, "poster": "https://picsum.photos/300/450?random=12"},
    
    # Action Movies
    {"title": "Inception", "genre": "Action", "rating": 8.8, "poster": "https://picsum.photos/300/450?random=13"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "poster": "https://picsum.photos/300/450?random=14"},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=15"},
    {"title": "John Wick", "genre": "Action", "rating": 7.4, "poster": "https://picsum.photos/300/450?random=16"},
    {"title": "Mission: Impossible", "genre": "Action", "rating": 7.1, "poster": "https://picsum.photos/300/450?random=17"},
    {"title": "Die Hard", "genre": "Action", "rating": 8.2, "poster": "https://picsum.photos/300/450?random=18"},
    
    # Romance Movies
    {"title": "Titanic", "genre": "Romance", "rating": 7.9, "poster": "https://picsum.photos/300/450?random=19"},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8, "poster": "https://picsum.photos/300/450?random=20"},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0, "poster": "https://picsum.photos/300/450?random=21"},
    {"title": "500 Days of Summer", "genre": "Romance", "rating": 7.7, "poster": "https://picsum.photos/300/450?random=22"},
    {"title": "Eternal Sunshine of the Spotless Mind", "genre": "Romance", "rating": 8.3, "poster": "https://picsum.photos/300/450?random=23"},
    {"title": "Before Sunrise", "genre": "Romance", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=24"},
    
    # Horror Movies
    {"title": "The Shining", "genre": "Horror", "rating": 8.4, "poster": "https://picsum.photos/300/450?random=25"},
    {"title": "A Nightmare on Elm Street", "genre": "Horror", "rating": 7.4, "poster": "https://picsum.photos/300/450?random=26"},
    {"title": "Halloween", "genre": "Horror", "rating": 7.7, "poster": "https://picsum.photos/300/450?random=27"},
    {"title": "The Exorcist", "genre": "Horror", "rating": 8.0, "poster": "https://picsum.photos/300/450?random=28"},
    {"title": "Alien", "genre": "Horror", "rating": 8.4, "poster": "https://picsum.photos/300/450?random=29"},
    {"title": "The Silence of the Lambs", "genre": "Horror", "rating": 8.6, "poster": "https://picsum.photos/300/450?random=30"},
    
    # Sci-Fi Movies
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster": "https://picsum.photos/300/450?random=31"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "poster": "https://picsum.photos/300/450?random=32"},
    {"title": "Blade Runner", "genre": "Sci-Fi", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=33"},
    {"title": "2001: A Space Odyssey", "genre": "Sci-Fi", "rating": 8.3, "poster": "https://picsum.photos/300/450?random=34"},
    {"title": "Back to the Future", "genre": "Sci-Fi", "rating": 8.5, "poster": "https://picsum.photos/300/450?random=35"},
    {"title": "E.T. the Extra-Terrestrial", "genre": "Sci-Fi", "rating": 7.8, "poster": "https://picsum.photos/300/450?random=36"},
    
    # Comedy Movies
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=37"},
    {"title": "Superbad", "genre": "Comedy", "rating": 7.6, "poster": "https://picsum.photos/300/450?random=38"},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7, "poster": "https://picsum.photos/300/450?random=39"},
    {"title": "Bridesmaids", "genre": "Comedy", "rating": 6.8, "poster": "https://picsum.photos/300/450?random=40"},
    {"title": "Shaun of the Dead", "genre": "Comedy", "rating": 7.9, "poster": "https://picsum.photos/300/450?random=41"},
    {"title": "The Big Lebowski", "genre": "Comedy", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=42"},
    
    # Thriller Movies
    {"title": "Gone Girl", "genre": "Thriller", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=43"},
    {"title": "Shutter Island", "genre": "Thriller", "rating": 8.2, "poster": "https://picsum.photos/300/450?random=44"},
    {"title": "Memento", "genre": "Thriller", "rating": 8.4, "poster": "https://picsum.photos/300/450?random=45"},
    {"title": "Se7en", "genre": "Thriller", "rating": 8.6, "poster": "https://picsum.photos/300/450?random=46"},
    {"title": "Zodiac", "genre": "Thriller", "rating": 7.7, "poster": "https://picsum.photos/300/450?random=47"},
    {"title": "The Sixth Sense", "genre": "Thriller", "rating": 8.1, "poster": "https://picsum.photos/300/450?random=48"}
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