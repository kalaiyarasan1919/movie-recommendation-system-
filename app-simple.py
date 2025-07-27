from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('static/imdb_top_1000.csv')

def filter_by_genre(df, genre):
    return df[df['Genre'].str.contains(genre, case=False, na=False)]

def highest_rated_movie(genre_filtered):
    highest_rated = genre_filtered.loc[genre_filtered['IMDB_Rating'].idxmax()]
    return highest_rated['Series_Title'], highest_rated['IMDB_Rating']

def recommend_by_genre(genres):
    genre_filtered_df = filter_by_genre(df, genres)
    if genre_filtered_df.empty:
        return f"No movies found for the genre: {genres}"

    # Simple recommendation: return top 5 highest rated movies in the genre
    top_movies = genre_filtered_df.nlargest(5, 'IMDB_Rating')
    
    recommendations = []
    for _, movie in top_movies.iterrows():
        recommendations.append({
            'title': movie['Series_Title'],
            'poster': movie['Poster_Link']
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