from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
df = pd.read_csv(r'C:/Users/kalaiyarasan/Desktop/project/static/imdb_top_1000.csv')

def filter_by_genre(df, genre):
    return df[df['Genre'].str.contains(genre, case=False, na=False)]

def highest_rated_movie(genre_filtered):
    highest_rated = genre_filtered.loc[genre_filtered['IMDB_Rating'].idxmax()]
    return highest_rated['Series_Title'], highest_rated['IMDB_Rating']

def recommend_by_genre(genres):
    genre_filtered_df = filter_by_genre(df, genres)
    if genre_filtered_df.empty:
        return f"No movies found for the genre: {genres}"

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Overview'])
    
    similarity = cosine_similarity(tfidf_matrix)

    random_movie_index = genre_filtered_df.index[0]
    distances = sorted(list(enumerate(similarity[random_movie_index])), reverse=True, key=lambda x: x[1])

    recommendations = []
    for i in distances[1:6]:
        movie = df.iloc[i[0]]
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

if __name__ == '__main__':
    app.run(debug=True)
