from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded test data with more movies and genres - Updated with reliable poster URLs
test_movies = [
    # Drama Movies
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Shawshank+Redemption"},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Godfather"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Fight+Club"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Forrest+Gump"},
    {"title": "The Green Mile", "genre": "Drama", "rating": 8.6, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Green+Mile"},
    {"title": "Goodfellas", "genre": "Drama", "rating": 8.7, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Goodfellas"},
    
    # Crime Movies
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Pulp+Fiction"},
    {"title": "The Departed", "genre": "Crime", "rating": 8.5, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Departed"},
    {"title": "Heat", "genre": "Crime", "rating": 8.2, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Heat"},
    {"title": "Scarface", "genre": "Crime", "rating": 8.3, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Scarface"},
    {"title": "The Usual Suspects", "genre": "Crime", "rating": 8.5, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Usual+Suspects"},
    {"title": "Reservoir Dogs", "genre": "Crime", "rating": 8.3, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Reservoir+Dogs"},
    
    # Action Movies
    {"title": "Inception", "genre": "Action", "rating": 8.8, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Inception"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Dark+Knight"},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Mad+Max+Fury+Road"},
    {"title": "John Wick", "genre": "Action", "rating": 7.4, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=John+Wick"},
    {"title": "Mission: Impossible", "genre": "Action", "rating": 7.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Mission+Impossible"},
    {"title": "Die Hard", "genre": "Action", "rating": 8.2, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Die+Hard"},
    
    # Romance Movies
    {"title": "Titanic", "genre": "Romance", "rating": 7.9, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Titanic"},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Notebook"},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=La+La+Land"},
    {"title": "500 Days of Summer", "genre": "Romance", "rating": 7.7, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=500+Days+of+Summer"},
    {"title": "Eternal Sunshine of the Spotless Mind", "genre": "Romance", "rating": 8.3, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Eternal+Sunshine"},
    {"title": "Before Sunrise", "genre": "Romance", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Before+Sunrise"},
    
    # Horror Movies
    {"title": "The Shining", "genre": "Horror", "rating": 8.4, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Shining"},
    {"title": "A Nightmare on Elm Street", "genre": "Horror", "rating": 7.4, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Nightmare+on+Elm+Street"},
    {"title": "Halloween", "genre": "Horror", "rating": 7.7, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Halloween"},
    {"title": "The Exorcist", "genre": "Horror", "rating": 8.0, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Exorcist"},
    {"title": "Alien", "genre": "Horror", "rating": 8.4, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Alien"},
    {"title": "The Silence of the Lambs", "genre": "Horror", "rating": 8.6, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Silence+of+the+Lambs"},
    
    # Sci-Fi Movies
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Interstellar"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Matrix"},
    {"title": "Blade Runner", "genre": "Sci-Fi", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Blade+Runner"},
    {"title": "2001: A Space Odyssey", "genre": "Sci-Fi", "rating": 8.3, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=2001+Space+Odyssey"},
    {"title": "Back to the Future", "genre": "Sci-Fi", "rating": 8.5, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Back+to+the+Future"},
    {"title": "E.T. the Extra-Terrestrial", "genre": "Sci-Fi", "rating": 7.8, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=E.T.+Extra+Terrestrial"},
    
    # Comedy Movies
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Grand+Budapest+Hotel"},
    {"title": "Superbad", "genre": "Comedy", "rating": 7.6, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Superbad"},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Hangover"},
    {"title": "Bridesmaids", "genre": "Comedy", "rating": 6.8, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Bridesmaids"},
    {"title": "Shaun of the Dead", "genre": "Comedy", "rating": 7.9, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Shaun+of+the+Dead"},
    {"title": "The Big Lebowski", "genre": "Comedy", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Big+Lebowski"},
    
    # Thriller Movies
    {"title": "Gone Girl", "genre": "Thriller", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Gone+Girl"},
    {"title": "Shutter Island", "genre": "Thriller", "rating": 8.2, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Shutter+Island"},
    {"title": "Memento", "genre": "Thriller", "rating": 8.4, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Memento"},
    {"title": "Se7en", "genre": "Thriller", "rating": 8.6, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Se7en"},
    {"title": "Zodiac", "genre": "Thriller", "rating": 7.7, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=Zodiac"},
    {"title": "The Sixth Sense", "genre": "Thriller", "rating": 8.1, "poster": "https://via.placeholder.com/300x450/1f2937/ffffff?text=The+Sixth+Sense"}
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