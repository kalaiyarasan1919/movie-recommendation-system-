from setuptools import setup, find_packages

setup(
    name="movie-recommendation-system",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.2.5",
        "pandas==1.5.3",
        "scikit-learn==1.1.3",
        "gunicorn==20.1.0",
    ],
    python_requires=">=3.8",
) 