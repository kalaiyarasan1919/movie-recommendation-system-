# Movie Recommendation App

A Flask web application that provides movie recommendations based on genre preferences using content-based filtering with TF-IDF and cosine similarity.

## Features

- Genre-based movie filtering
- Content-based recommendation system using TF-IDF vectorization
- Cosine similarity for finding similar movies
- Modern, responsive web interface
- Movie poster display

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`

## Deployment Options

### Option 1: Heroku (Recommended for beginners)

1. Install Heroku CLI and create an account at [heroku.com](https://heroku.com)

2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-app-name
```

4. Deploy to Heroku:
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

5. Open your app:
```bash
heroku open
```

### Option 2: Railway

1. Go to [railway.app](https://railway.app) and create an account
2. Connect your GitHub repository
3. Railway will automatically detect your Flask app and deploy it
4. Your app will be available at the provided URL

### Option 3: Render

1. Go to [render.com](https://render.com) and create an account
2. Connect your GitHub repository
3. Create a new Web Service
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `gunicorn app:app`
6. Deploy your app

### Option 4: PythonAnywhere

1. Create an account at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your files via the Files tab
3. Create a new web app using the Web tab
4. Configure the WSGI file to point to your Flask app
5. Your app will be available at `yourusername.pythonanywhere.com`

### Option 5: VPS/Cloud Server

1. Rent a VPS (DigitalOcean, AWS EC2, Google Cloud, etc.)
2. Install Python, pip, and git
3. Clone your repository
4. Install dependencies: `pip install -r requirements.txt`
5. Use a process manager like PM2 or systemd to run your app
6. Set up a reverse proxy with Nginx

## Environment Variables

For production deployment, consider setting these environment variables:

- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key`

## File Structure

```
project/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
├── runtime.txt        # Python version specification
├── README.md          # This file
├── static/
│   └── imdb_top_1000.csv  # Movie dataset
└── templates/
    └── index.html     # Web interface
```

## Technologies Used

- **Backend**: Flask, Python
- **Data Processing**: Pandas, scikit-learn
- **ML/AI**: TF-IDF Vectorization, Cosine Similarity
- **Deployment**: Gunicorn (WSGI server)

## Dataset

The app uses the IMDB Top 1000 Movies dataset containing:
- Movie titles, genres, ratings
- Movie overviews for content-based filtering
- Poster links for visual display

## Troubleshooting

### Common Issues:

1. **Port already in use**: Change the port in `app.py` or kill the existing process
2. **Memory issues**: The dataset is loaded into memory, consider using a smaller dataset for production
3. **Deployment errors**: Ensure all files are committed to git before deploying

### Performance Tips:

- Consider caching the TF-IDF matrix for better performance
- Implement pagination for large result sets
- Use a production-grade database instead of CSV for large datasets

## License

This project is open source and available under the MIT License. 