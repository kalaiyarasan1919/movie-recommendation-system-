from flask import Flask, render_template, request

app = Flask(__name__)

# Expanded test data with more movies and genres - Updated with reliable poster URLs
test_movies = [
    # Drama Movies
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "poster": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "poster": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "poster": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "poster": "https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg"},
    {"title": "The Green Mile", "genre": "Drama", "rating": 8.6, "poster": "https://image.tmdb.org/t/p/w500/velWPhVMQeQKcxggNEU8YmIo52R.jpg"},
    {"title": "Goodfellas", "genre": "Drama", "rating": 8.7, "poster": "https://image.tmdb.org/t/p/w500/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg"},
    
    # Crime Movies
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "poster": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg"},
    {"title": "The Departed", "genre": "Crime", "rating": 8.5, "poster": "https://image.tmdb.org/t/p/w500/n4H2v6NzqHuFvuT8ceRIve6mNqE.jpg"},
    {"title": "Heat", "genre": "Crime", "rating": 8.2, "poster": "https://image.tmdb.org/t/p/w500/umX3lBhHoN7zB6uWcj8d5cK1MvQ.jpg"},
    {"title": "Scarface", "genre": "Crime", "rating": 8.3, "poster": "https://image.tmdb.org/t/p/w500/zr2p353wrdbEQSMn8a4cOpxQWzL.jpg"},
    {"title": "The Usual Suspects", "genre": "Crime", "rating": 8.5, "poster": "https://image.tmdb.org/t/p/w500/joGgKynwSXONhp6Jar11tkbJ2Bo.jpg"},
    {"title": "Reservoir Dogs", "genre": "Crime", "rating": 8.3, "poster": "https://image.tmdb.org/t/p/w500/xi8Iu6qyTfyZVDVy60Ruw9lP6F8.jpg"},
    
    # Action Movies
    {"title": "Inception", "genre": "Action", "rating": 8.8, "poster": "https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/hA2ple9q4qnwxp3hKVNhroR2dfQ.jpg"},
    {"title": "John Wick", "genre": "Action", "rating": 7.4, "poster": "https://image.tmdb.org/t/p/w500/5vHssUeVe25bMrof1HyaPyWjPtt.jpg"},
    {"title": "Mission: Impossible", "genre": "Action", "rating": 7.1, "poster": "https://image.tmdb.org/t/p/w500/An9Dp3prmiG6P6S3KxAF1yYctzn.jpg"},
    {"title": "Die Hard", "genre": "Action", "rating": 8.2, "poster": "https://image.tmdb.org/t/p/w500/yFihWxQcmqF9NuOqE6vCH3H9QmH.jpg"},
    
    # Romance Movies
    {"title": "Titanic", "genre": "Romance", "rating": 7.9, "poster": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.8, "poster": "https://image.tmdb.org/t/p/w500/rMz2bJvUrTH9U48OSO4eIlV92iX.jpg"},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0, "poster": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg"},
    {"title": "500 Days of Summer", "genre": "Romance", "rating": 7.7, "poster": "https://image.tmdb.org/t/p/w500/f9mbM0YMLpYemcWx6M2yY3fTBBc.jpg"},
    {"title": "Eternal Sunshine of the Spotless Mind", "genre": "Romance", "rating": 8.3, "poster": "https://image.tmdb.org/t/p/w500/5y4k3rSjPLVbBWJ2cVuN2p5Jd5T.jpg"},
    {"title": "Before Sunrise", "genre": "Romance", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/kf9U5PR3OduC1yEKL1D2LQvcKv4.jpg"},
    
    # Horror Movies
    {"title": "The Shining", "genre": "Horror", "rating": 8.4, "poster": "https://image.tmdb.org/t/p/w500/b6ko0IKC8MdYBR1BA48nhwW1QWT.jpg"},
    {"title": "A Nightmare on Elm Street", "genre": "Horror", "rating": 7.4, "poster": "https://image.tmdb.org/t/p/w500/wMq9kQXTeQCHUZOG4fAWP5T6jOu.jpg"},
    {"title": "Halloween", "genre": "Horror", "rating": 7.7, "poster": "https://image.tmdb.org/t/p/w500/aLeyDoK6VR6Eya3YkP3j7LyQUUS.jpg"},
    {"title": "The Exorcist", "genre": "Horror", "rating": 8.0, "poster": "https://image.tmdb.org/t/p/w500/4ucLGcXVVSVnsfkG5y5xFK8Lq.jpg"},
    {"title": "Alien", "genre": "Horror", "rating": 8.4, "poster": "https://image.tmdb.org/t/p/w500/brAZ2xsiSc0Ijs2Xd2v2sIe8aQy.jpg"},
    {"title": "The Silence of the Lambs", "genre": "Horror", "rating": 8.6, "poster": "https://image.tmdb.org/t/p/w500/rplLJ2hPcOQmkFhTqUte0MkEaO2.jpg"},
    
    # Sci-Fi Movies
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "poster": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"title": "Blade Runner", "genre": "Sci-Fi", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/63N9uy8nd9j7Eog2YPQaiZ3Bq5q.jpg"},
    {"title": "2001: A Space Odyssey", "genre": "Sci-Fi", "rating": 8.3, "poster": "https://image.tmdb.org/t/p/w500/ve72VxNqjGM69Uky4WTo2FthIWF.jpg"},
    {"title": "Back to the Future", "genre": "Sci-Fi", "rating": 8.5, "poster": "https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sWOxbl4KjqN.jpg"},
    {"title": "E.T. the Extra-Terrestrial", "genre": "Sci-Fi", "rating": 7.8, "poster": "https://image.tmdb.org/t/p/w500/an0nD6uq9byQCsJlikKwmRkn8K.jpg"},
    
    # Comedy Movies
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/eWdyYQreja6LF6Q6h3rFJuLpvLb.jpg"},
    {"title": "Superbad", "genre": "Comedy", "rating": 7.6, "poster": "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg"},
    {"title": "The Hangover", "genre": "Comedy", "rating": 7.7, "poster": "https://image.tmdb.org/t/p/w500/ulXLATsSLwJx4KHF4JtDg0n0EdB.jpg"},
    {"title": "Bridesmaids", "genre": "Comedy", "rating": 6.8, "poster": "https://image.tmdb.org/t/p/w500/6aUWe0GSl69wMTSWex2BPIybp7h.jpg"},
    {"title": "Shaun of the Dead", "genre": "Comedy", "rating": 7.9, "poster": "https://image.tmdb.org/t/p/w500/7YwjaNLm9XGL5tUH0iDrwDlpMA6.jpg"},
    {"title": "The Big Lebowski", "genre": "Comedy", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/ruAZSnZNV3wMu1ixek1KbNxEfi6.jpg"},
    
    # Thriller Movies
    {"title": "Gone Girl", "genre": "Thriller", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/gdiLTof3rbPDAmPaCf4gRopMZju.jpg"},
    {"title": "Shutter Island", "genre": "Thriller", "rating": 8.2, "poster": "https://image.tmdb.org/t/p/w500/4GDy0PHYX3VRXkDlznd9T9mvTHO.jpg"},
    {"title": "Memento", "genre": "Thriller", "rating": 8.4, "poster": "https://image.tmdb.org/t/p/w500/fQMSaP88wf1VDzWt5Cb1Vbyb7pK.jpg"},
    {"title": "Se7en", "genre": "Thriller", "rating": 8.6, "poster": "https://image.tmdb.org/t/p/w500/6yOGkVvJipO2EOJmgQj3Fu2ZJ1C.jpg"},
    {"title": "Zodiac", "genre": "Thriller", "rating": 7.7, "poster": "https://image.tmdb.org/t/p/w500/6BxTdWx9dpzoOngqAGx3Q8s5fNf.jpg"},
    {"title": "The Sixth Sense", "genre": "Thriller", "rating": 8.1, "poster": "https://image.tmdb.org/t/p/w500/imps263dHNe3A4Jq1qO1T2IqSd.jpg"}
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