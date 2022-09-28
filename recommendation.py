import csv

import pandas
import json
from tmdbv3api import TMDb, Movie

# os, multiprocessing as mp

# from itertools import count
# from multiprocessing import process

listOfMovies = []
listOfRecommendations = []


def getListOfMovies():
    global listOfMovies
    df = pandas.read_csv('data/movie_titles_quotes.csv', quotechar="|",  engine='python')
    return df.to_json(orient="values")

def getMovie(movie_index):
    df = pandas.read_csv('data/movie_titles_quotes.csv', quotechar="|",  engine='python')
    searchvalue = [int(movie_index)]
    print(searchvalue)
    return df.loc[df['Index'].isin(searchvalue)].to_json(orient="values")

def getMovieDescription(movie_index):
    #Settings for Movie Database API
    tmdb = TMDb()
    tmdb.api_key = "5c8fd8b1305a68eec72b4bd6cf0edbfb"
    tmdb.language = "de"

    #Search for current movie in csv
    df = pandas.read_csv('data/movie_titles_quotes.csv', quotechar="|",  engine='python')
    searchvalue = [int(movie_index)]
    current_movie_title = ""
    try:
        current_movie_title = df.loc[df['Index'].isin(searchvalue)]["Name"].array[0]
    except:
        print("Error: Movie doesn't exist.")
    print(current_movie_title)

    #Get the description of movie title
    description = ""
    if current_movie_title != "":
        movie = Movie()
        try:
            description = movie.search(current_movie_title)[0].overview
        except:
            print("Error: Could not get description for movie from database.")
    
    return json.dumps(description)

def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None
